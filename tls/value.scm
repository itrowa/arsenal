

(load "help.scm")


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; 解释器的顶层部分
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; 解释器就是要对输入的表达式e进行处理.
;;; e有两种,一种是atom,另外一种是list
;;; 所以要分为两种情况

(define expression-to-action
  (lambda (e)
    (cond
      ((atom? e)(atom-to-action e))
      (else (list-to-action e)))))

; take e return function *xxx
; 现在已经知道e是atom了.但具体是哪种atom? 不同的atom调用不同的函数.
;
(define atom-to-action
  (lambda (e)
    (cond
      ((number? e) *const)
      ((eq? e #t) *const)
      ((eq? e #f) *const)
      ((eq? e (quote cons)) *const)
      ((eq? e (quote car)) *const)
      ((eq? e (quote cdr)) *const)
      ((eq? e (quote null?)) *const)
      ((eq? e (quote eq?)) *const)
      ((eq? e (quote atom?)) *const)
      ((eq? e (quote zero?)) *const)
      ((eq? e (quote add1)) *const)
      ((eq? e (quote sub1)) *const)
      ((eq? e (quote number?)) *const)
      (else *identifier))))  ; 例如e是 z, abc123 这种atom, 会走到这一分支

; 通过express-to-action,这里的e是个list
; 但不同的list调用不同的 *xxx函数.
(define list-to-action
  (lambda (e)
    (cond
       ;1 (如果car e是atom则再分为如下情况
      ((atom? (car e))
        (cond
          ((eq? (car e)(quote quote)) *quote)
          ((eq? (car e)(quote lambda)) *lambda)
          ((eq? (car e)(quote cond)) *cond)
          (else *application)))
       ;2 (car e)不是atom
      (else *application))))
;先假设所有带*的函数都能正常工作,我们继续设计解释器的顶层,再填入细节.


; 解释器入口: (等价于eval函数)
(define value
  (lambda (e)
    (meaning e '() )))
;note: quote()创建一个空的table.
;如果把value做成带table参数的也可以,但是像上面这样封装一下不是
;更好吗. 这样每次调用value就直接一个e参数输入就行了


; 被入口函数调用的meaning函数:
; 参数:一个表达式 和 用于表示环境的table.
(define meaning
  (lambda (e table)
    ((expression-to-action e) e table)))
; 它的作用是对表达式进行分类,其构造就是对表达式的语法类型分情况分析.
; meaning e table 会归约为如下之一:
; (*const e table)
; (*identifier e table)
; (*quote e table)
; (*lambda e table)
; (*application e table)




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 针对每种情况的求值
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; *const
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define *const
  (lambda (e table)
    (cond
      ((number? e) e)
      ((eq? e #t) #t)
      ((eq? e #f) #f)
      (else (build 'primitive e)))))
;; 对数字, 直接返回其字面的值
;; 对#t, #f, 返回lisp中的true和false
;; 对其他常量的atom, 返回primitive e

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;         *quote
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;
(define *quote
  (lambda (e table)
    (text-of e)))

(define text-of second)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;       *identifier
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; 已知table中能查找的e的value时才生效.
(define *identifier
  (lambda (e table)
    (lookup-in-table e table initial-table)))

; 产生一个空的table
(define initial-table
  (lambda (name)
    (car '())))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;     *lambda
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; 根据输入的lambda表达式e和输入的table
; 输出一个list: 扩展了env.
; (   non-primitive  (table)     (formals)       (body))
;                    输入的表   lambda函数的形参  函数body
(define *lambda
  (lambda (e table)
    (build 'non-primitive (cons table (cdr e)))))

; help func for evaluating lambda exp
(define table-of first)
(define formals-of second)
(define body-of third)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;  cond
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; 
; 实现cond的功能
; 它处理的是为
; (cond (...)) 这样的形式的e
; 例如
; (cond (coffee klatsch)
;       (else party))
(define *cond
  (lambda (e table)
    (evcon (cond-lines-of e) table)))


;以下都是辅助函数
;lines一般是两部分
; ((question?) (then do..))
(define evcon
  (lambda (lines table)
    (cond
      ((else? (question-of (car lines)))
         (meaning (answer-of (car lines)) table))
      ((meaning (question-of (car lines)) table)
         (meaning (answer-of (car lines)) table))
      (else (evcon (cdr lines) table)))))

;用于evcon的help function
(define question-of first)
(define answer-of second)

;用于evcon的help function
;它判断输入的参数是否等于字面意义上的 else
;如果是else那么返回#t
(define else?
  (lambda (x)
    (cond
      ((atom? x) (eq? x (quote else)))
      (else #f))))


(define cond-lines-of cdr)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;   *application
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;这里的e是类似于这样的形式
;;;(function-name arg1 arg2 ..)
;; 用car可以把e中的func name取出，cdr则取出args的列表.
;; 功能： 先对函数名求值 再对起参数求值 最后执行apply函数
(define *application
  (lambda(e table)
    (apply-it
      (meaning (function-of e) table)
      (evlis (arguments-of e) table))))

;;;辅助函数
; 参数: 一个表示args的列表和一个table
; 返回一个列表, 里面装个每个arg的meaning
(define evlis
  (lambda (args table)
    (cond
      ((null? args) (quote()))
      (else
        (cons (meaning (car args) table)
              (evlis (cdr args) table))))))

;两个辅助函数
(define function-of car)
(define arguments-of cdr)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;           apply
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; func have 2 representations.
; (primitive primitive-name)
; (non-primitive (table formals body))
; (table formals body) : a closure record.

;; 判断函数是primitive还是非primitive.
(define primitive?
  (lambda (l)
    (eq? (first l) (quote primitive))))

(define non-primitive?
  (lambda (l)
    (eq? (first l) (quote non-primitive))))

    
;
; 具体要做的事情
; 是对于fun 和vals而言, func是primitive? 还是non-primitive? 分情况处理.
(define apply-it
  (lambda (fun vals)
    (cond 
      ((primitive? fun)
       (apply-primitive (second fun) vals))
      ((non-primitive? fun)
       (apply-closure (second fun) vals)))))

(define apply-primitive
  (lambda (name vals)
    (cond
      ((eq? name (quote cons))
            (cons (first vals) (second vals)))
      ((eq? name (quote car))
       (car (first vals)))
      ((eq? name (quote cdr))
       (cdr (first vals)))
      ((eq? name (quote null?))
       (null? (first vals)))
      ((eq? name (quote eq?))
       (eq? (first vals) (second vals)))
      ((eq? name (quote atom?))
       (:atom? (first vals)))
      ((eq? name (quote zero?))
       (zero? (first vals)))
      ((eq? name (quote add1))
       (add1 (first vals)))
      ((eq? name (quote sub1))
       (sub1 (first vals)))
      ((eq? name (quote number?))
       (number? (first vals))))))

;其中:atom?是
(define :atom?
  (lambda (x)
    (cond
      ((atom? x) #t)
      ((null? x) #f)
      ((eq? (car x) (quote primitive)) #t)
      ((eq? (car x) (quote non-primitive)) #t)
      (else #f))))

(define apply-closure
  (lambda (closure vals)
          (meaning (body-of closure)
                   (extend-table
                     (new-entry (formals-of closure) vals)
                     (table-of closure)))))
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
; 用以下参数试一下:
(display "start interpreter test...")
(newline)

; 定义一个环境
(define env1            ;; 由3个entry组成
        '(((x y)
          ((a b c)(d e f))
          ((u v w)
           (1 2 3))
          ((x y z)
           (4 5 6)))))

; (*const e table) test
(*const 2 '()) 
(*const #t '())

; (*quote e table) test
(*quote '(quote hehehe) '())
(*quote '(quote (1 2 3 4 (5 6))) '())

; (*identifier e table) test
;(*identifier 'x env1)          ;失败

; (*lambda e table) test
;(*lambda '(lambda (x) (add x x)) env1) 失败


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(display (value '(cons 6 (quote (a b c)))))
(newline)

;(meaning '(cons z x) env1)

;(meaning 'x env1)