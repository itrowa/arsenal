;; 采用应用序求值的四则运算器.
;; (operator (operand1, operand2,...))
(define (eval-1 exp)
  (cond ((number? exp) exp)          
        ((op? exp) exp)             
        ((application? exp) (apply-1 (eval-1 (operator exp))   
                                     (evlist (operands exp))))))
;; note: 匹配3种模式: 
;; 数字? 
;; +,-,*,/之一的atom? 
;; 以及(op e1 e2这种形式)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 模式匹配相关函数
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; exp是+,-,*,/之一的atom吗?
;; -----------------------------
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

;; exp是一个组合式吗?
;; -----------------------------
(define (application? exp)
  (if (not (atom? exp))
      (if (op? (car exp))
          #t
          #f)
      #f))

;; 对operands求值
;; -----------------------------
(define (evlist operands)
  (cond ((null? operands) '())
        (else (cons (eval-1 (car operands))
                    (evlist (cdr operands))))))

;; 对组合式的操作, 那就是应用参数到过程上.
;; -----------------------------
(define (apply-1 proc args)
  (cond ((eq? proc '+) (+ (car args) (cadr args)))
        ((eq? proc '-) (- (car args) (cadr args)))
        ((eq? proc '*) (* (car args) (cadr args)))
        ((eq? proc '/) (/ (car args) (cadr args)))))

;; test
(define e1 '(+ 1 2))
(eval-1 e1)
(operator e1)            ;; +
(eval-1 (operator e1))   ;; +
(operands e1)            ;; (1 2)
(evlist (operands e1))   ;; (1 2)

(apply-1 (eval-1 (operator e1))   
         (evlist (operands e1)))   ;; 3

(apply-1 '+ '(1 2))