;; ***************************************
;;  SCHEME INTERPRETER TYPE2.
;; ***************************************

;; 支持递归的四则运算,
;; 支持lambda calculus的解释器
;; 支持查找symbol的值, 但不支持绑定.
;; @todo: 以下special form待完善: define ; cond; 以及研究递归; Y-Combinator.


(define (eval-1 exp env)
  (cond ((number? exp) exp )          
        ((math-op? exp) exp )
        ((symbol? exp) (lookup exp env))
        ;((variable? exp) (lookup-variable exp env))
        ;;((cond? exp) do sth..)
        ((quote? exp) (quoted-content exp))
        ((lambda? exp) (list 'CLOSURE (cdr exp) env)) ; 做成闭包
        
        ;; 组合式的求值
        (else (apply-1 (eval-1 (operator exp) env)   
                       (evlist (operands exp) env)))))


;; 把'procedure, lambda表达式参数, 和lambda body, 和其携带的环境一起做成一个闭包.
;; 之所以在列表前添加'CLOSURE的标识符是为了让apply可以将其识别为复合过程.

;; help 
(define operator car)
(define operands cdr)
(define quoted-content cadr)
;; help
;(define (lambda-parameters p) (cadr p))
;(define (lambda-body p) (caddr p))
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



;; exp是一个变量吗?
;; ---------------------------
(define (variable? exp)
  (symbol? exp))                ;; 总感觉这个判断条件可要可不要.
;; note: variable? 必须放在eval的后面, 因为要知
;; 道一个atom, 不是数字，也不是+-*/之一后,才可能是变量.


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; actions for  matched mattern.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; 在环境中查找某个symbol的值.
;; symbol: atom
;; ---------------------------
(define (lookup symbol env)
  (cond ((eq? env '()) "Unbound Variable")
        (else
         (get-value-in-frame symbol (car env) env))))
 

;;在frame中查找含有symbol的pair.
(define (get-value-in-frame symbol frame env)
  (cond ((null? frame) (lookup symbol (cdr env)))
        ((eq? (car (car frame)) symbol) (cdr (car frame)))
        (else
         (get-value-in-frame symbol (cdr frame) env))))

;; 对operands的列表中元素依次调用eval-1过程求值.
;; operands: 一个list
;; ---------------------------
(define (evlist operands env)
  (cond ((null? operands) '())
        ;((atom? operands) (cons operands '()))
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

; 环境的组成: 
; ( ((d . 4) (e . 5) (f . 6)) ((z . 9))    )
;        frame1                  frame2

; 实际上是个list list中每一个list表示一个frame,每个frame又有若干个pair组成.


; 把形参和实参作为一条list追加到环境里去.(增加一个frame)
; vars: list
; vals: list
; env: ((pair)(pair))
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

; atom测试
(eval-1 '+ env1)
(eval-1 '4 env1)

; primitive procedure
(evlist '(1 2) env1)
(evlist '(b c) env1)
(apply-1 '+   
         '(1 2))
(primitive-proc? '+)

(eval-1 '(+ 1 2) env1)
(eval-1 '(+ a 2) env1)

;  lambda expression
(eval-1 '(lambda (x) (* x x)) env1)    ;;
; (closure (x) (* x x) (((a . 1) (b . 2) (c . 3)) (('+ . +) ('- . -) ('* . *) ('/ . /))))

; compound procedure test
(eval-1 '((lambda (x) (* x x)) 2)  env1)
; 4

; compound procedure test
(eval-1 '((lambda (x) (lambda (y) (* x y))) 3) env1)
(eval-1 '(((lambda (x) (lambda (y) (* x y))) 3)2) env1)

; environment test
(define global-env '())
(define env1 '(((a . 1) 
                (b . 2) 
                (c . 3)) 
               (('+ . +) 
                ('- . -)
                ('* . *)
                ('/ . /))))
(define env2 '(((y . 2))
               ((x . 3))       
               ((a . 1) (b . 2) (c . 3))                 
               (('+ . +) ('- . -) ('* . *) ('/ . /))))
(lookup 'x env2)
