;; 支持递归的四则运算,
;; 支持变量绑定, 
;; 支持lambda calculus的解释器


(define (eval-1 exp env)
  (cond ((number? exp) exp )          
        ((math-op? exp) exp )
        ((symbol? exp) (lookup exp env))
        ((primitive? exp))
        ;((variable? exp) (lookup-variable exp env))
        ((quote? exp) (quoted-content exp))
        ((lambda? exp) (make-procedure (lambda-parameters exp)
                                       (lambda-body exp)
                                        env))
        ;;((cond? exp) do sth..)
        ((application? exp) (apply-1 (eval-1 (operator exp) env)   ;; 组合式的求值
                                     (evlist (operands exp) env)))
        (else "unknown expression")))
;; note: 匹配以下模式: 
;; 数字? 
;; +,-,*,/之一的atom? 
;; 变量?
;; 以及(op operands)这种形式

;; help 
(define operator car)
(define operands cdr)
(define quoted-content cadr)
;; help
(define (lambda-parameters p) (cadr p))
(define (lambda-body p) (caddr p))
;(define (lambda-environment p) (cadddr p))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 模式匹配的谓词过程
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; exp是+,-,*,/之一的atom吗?
;; ---------------------------
(define (math-op? exp)
  (if (atom? exp)
      (cond ((eq? exp '+) #t)
            ((eq? exp '-) #t)
            ((eq? exp '*) #t)
            ((eq? exp '/) #t)
            (else #f))
      #f))

(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))

(define (quote? exp)
  (eq? (car exp) 'quote))

;; exp是lambda表达式?
;; ---------------------------
(define (lambda? exp)
  (if (not (atom? exp))
      (if (eq? 'lambda (car exp))
          #t
          #f)
      #f))

;; exp是一个(<operator> <operand>)形式的组合式(call exp)吗?
;; ---------------------------
(define (application? exp)
  (if (not (atom? exp))
      (cond ((math-op? (car exp)) #t)
            ((variable? (car exp)) #t)
            (else #f))
      #f))

;; exp是一个变量吗?
;; ---------------------------
(define (variable? exp)
  (symbol? exp))                ;; 总感觉这个判断条件可要可不要.
;; note: variable? 必须放在eval的后面, 因为要知
;; 道一个atom, 不是数字，也不是+-*/之一后,才可能是变量.


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; actions for  matched mattern.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 对lambda表达式的操作
;; ---------------------------
(define (make-procedure p body env)
  (list 'CLOSURE p body env))
;; 把'procedure, lambda表达式参数, 和lambda body, 和其携带的环境一起做成一个闭包.
;; 之所以在列表前添加'CLOSURE的标识符是为了让apply可以将其识别为复合过程.

;; 在环境中查找某个symbol的值.
;; ---------------------------
(define (lookup symbol env)
  (cond ((eq? env '()) "unbound variable")
        (else
          (get-value (get-pair symbol (car env)) env))))

;; help:对于一个pair, 返回其value部分 
(define (get-value vcell env)
 (cond ((eq? vcell '())
        (lookup symbol (cdr env)))
       (else (cdr vcell))))

;; help:返回一个frame中包含的要查找的变量名的pair
(define (get-pair symbol alist)
  (cond ((eq? alist '()) '())
        ((eq? symbol (caar alist))
         (car alist))
        (else
         (assq symbol (cdr alist)))))

;; 对operands求值.
;; ---------------------------
(define (evlist operands env)
  (cond ((null? operands) '())
        (else (cons (eval-1 (car operands) env)
                    (evlist (cdr operands) env)))))

;; 应用一些参数到一个过程上.
;; ---------------------------
(define (apply-1 proc args)
  (cond ((primitive-proc? proc)
          (apply-primitive proc args))
        ((compound-proc? proc)
          (apply-compound proc args))
        (else '(procedure has error) )))
;; note: 分为基本过程的apply和复合过程的apply.

;; help
(define (primitive-proc? proc)
  (primitive-proc?-core proc 
                        primitive-proc-list))

(define (primitive-proc?-core proc plist)
  (cond ((null? plist) #f)
        ((eq? (car plist) proc) #t)
        (else (primitive-proc?-core proc (cdr plist)))))

(define (compound-proc? proc)
  (if (eq? (car proc) 'CLOSURE)
      #t
      #f))

(define primitive-proc-list
  '(+ - * / car cdr cons list))


;; help
(define (apply-primitive proc args)
  (cond ((eq? proc '+) (+ (car args) (cadr args)))
        ((eq? proc '-) (- (car args) (cadr args)))
        ((eq? proc '*) (* (car args) (cadr args)))
        ((eq? proc '/) (/ (car args) (cadr args)))))
; @todo:  (proc (car args) (cadr args))) 这样不行.. 得研究下为什么?


;; help
(define (apply-compound proc args)
  (eval-1 (cadadr proc)        ;; 闭包的body
         (bind (caadr proc)    ;; 闭包的形参
               args            ;; 实参
               (caddr proc)))) ;; 闭包的env


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 环境
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 环境模型:就是一个table, 里面每个box都是一个pair.
;; ()
;; ((a . 3))
;; ((b . 4) (a . 3))
  

; 这个只支持单参数
;(define (extend-env name value env)
;  (cons (cons name value) env))

; 返回环境中name所在的pair.
;(define (lookup name env)
;  (cond ((null? env) '())
;        ((eq? name (car (car env))) (car env))
;        (else (lookup name (cdr env)))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; 环境的组成: 
; ( ((d . 4) (e . 5) (f . 6)) ((z . 9))    )
;        frame1                  frame2


; 把形参和实参作为一条list追加到环境里去.(增加一个frame)
;; ---------------------------
(define (bind vars vals env)
  (cons (pair-up vars vals)
        env))

; help
(define (pair-up vars vals)
  (cond
    ((eq? vars '())
      (cond ((eq? vals '()) '())
            (else "Too much args")))
    ((eq? vals '()) ("Too few args"))
    (else
      (cons (cons (car vars)
                  (car vals))
            (pair-up (cdr vars)
                     (cdr vals))))))


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; test
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; just for test
(define global-env '())
;(define env1 '((a . 1) (b . 2) (c . 3)))
(define env1 '(((a . 1) 
                (b . 2) 
                (c . 3)) 
               (('+ . +) 
                ('- . -)
                ('* . *)
                ('/ . /))))



; test
; atom
(eval-1 '+ env1)
(eval-1 '4 env1)

; primitive procedure求值
;(eval-1 '(+ 1 2) env1)
(evlist '(1 2) env1)
(evlist '(b c) env1)
(eval-1 (operator '(+ 1 2)) env1)


; Q:如何检测一个primitive procedure? 以及Primitive procedure的求值
(apply-1 '+   
         '(1 2))
(primitive-proc? '+)

;(eval-1 '(+ a 1) env1)
;(eval-1 '(lambda (x) (* x x)) ) env1)
