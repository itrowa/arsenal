;; 支持变量绑定, lambda calculus的解释器
;; (operator (operand1, operand2,...))
(define (eval-1 exp)
  (cond ((number? exp) exp)          
        ((op? exp) exp)             
        ((variable? exp) (lookup-variable exp))
        ((application? exp) (apply-1 (eval-1 (operator exp))   
                                     (eval-operands (operands exp))))))
;; note: 匹配3种模式: 
;; 数字? 
;; +,-,*,/之一的atom? 
;; 以及(op e1 e2这种形式)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 模式匹配相关函数
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


;; exp是+,-,*,/之一的atom吗?
(define (op? exp)
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

(define operator car)
(define operands cdr)

(define (application? exp)
  (if (not (atom? exp))
      (if (op? (car exp))
          #t
          #f)
      #f))

;; exp是一个变量吗?
(define (variable? exp)
  (symbol? exp))                ;; 总感觉这个判断条件可要可不要.
;; note: variable? 必须放在eval的后面, 因为要知
;; 道一个atom, 不是数字，也不是+-*/之一后,才可能是变量.
;;
;;


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; actions for  matched mattern.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (lookup-variables exp)
  (let ((record (lookup exp env)))
      (if (null? record)
       (display "Unbound variable")
       (else (car record)))))


(define (eval-operands operands)
  (cond ((null? operands) '())
        (else (cons (eval-1 (car operands))
                    (eval-operands (cdr operands))))))

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
