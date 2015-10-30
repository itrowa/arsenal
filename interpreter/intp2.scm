;; 支持递归的四则运算,
;; 支持变量绑定, 
;; 支持lambda calculus的解释器

;; (operator (operand1, operand2,...))
(define (eval-1 exp env)
  (cond ((number? exp) exp )          
        ((math-op? exp) exp )             
        ((variable? exp) (lookup-variable exp env))
        ((lambda? exp) (make-lambda (lambda-parameters exp)
                                    (lambda-body exp)
                                    env))
        ((application? exp) (apply-1 (eval-1 (operator exp) env)   
                                     (eval-operands (operands exp) env)))))
;; note: 匹配以下模式: 
;; 数字? 
;; +,-,*,/之一的atom? 
;; 变量?
;; 以及(op operands)这种形式

;; help 

(define operator car)
(define operands cdr)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 模式匹配相关函数
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; exp是+,-,*,/之一的atom吗?
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



;; exp是lambda表达式ma?
(define (lambda? exp)
  (if (not (atom? exp))
      (if (= 'lambda (car exp))
          #t
          #f)
      #f))

(define (application? exp)
  (if (not (atom? exp))
      (cond ((math-op? (car exp)) #t)
            ((variable? (car exp)) #t)
            (else #f))
      #f))

;; exp是一个变量吗?
(define (variable? exp)
  (symbol? exp))                ;; 总感觉这个判断条件可要可不要.
;; note: variable? 必须放在eval的后面, 因为要知
;; 道一个atom, 不是数字，也不是+-*/之一后,才可能是变量.



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; actions for  matched mattern.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (make-procedure P body env)
  (list 'CLOSURE P body env))
;; 把'procedure, lambda表达式参数, 和lambda body, 和其携带的环境一起做成一个闭包.

;; help
(define (lambda-parameters p) (cadr p))
(define (lambda-body p) (caddr p))
(define (lambda-environment p) (cadddr p))

;; 查找变量在某个环境中对应的值
(define (lookup-variable exp env)
  (let ((record (lookup exp env)))
      (if (null? record)
       (display "Unbound variable")
       (cdr record))))


(define (eval-operands operands env)
  (cond ((null? operands) '())
        (else (cons (eval-1 (car operands) env)
                    (eval-operands (cdr operands) env)))))

(define (apply-1 func args)
  (cond ((eq? func '+) (+ (car args) (cadr args)))
        ((eq? func '-) (- (car args) (cadr args)))
        ((eq? func '*) (* (car args) (cadr args)))
        ((eq? func '/) (/ (car args) (cadr args)))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 环境
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 环境模型:就是一个table, 里面每个box都是一个pair.
;; ()
;; ((a . 3))
;; ((b . 4) (a . 3))

(define global-env '())
(define (extend-env name value env)
  (cons (cons name value) env))

; 返回环境中name所在的pair.
(define (lookup name env)
  (cond ((null? env) '())
        ((eq? name (car (car env))) (car env))
        (else (lookup name (cdr env)))))

; just for test
(define env1 '((a . 1) (b . 2) (c . 3)))



;基本的test
(eval-1 '+ env1)
(eval-1 '4 env1)
(eval-1 '(+ 1 2) env1)

(eval-1 '(+ a 1) env1)
(eval-1 '(lambda (x) (* x x)) ) env1)