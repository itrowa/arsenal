;; 采用应用序求值的四则运算器.
;; (operator (operand1, operand2,...))
(define (eval-1 exp)
  (cond ((number? exp) exp)          
        ((op? exp) exp)             
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

(define (eval-operands operands)
  (cond ((null? operands) '())
        (else (cons (eval-1 (car operands))
                    (eval-operands (cdr operands))))))

(define (apply-1 func args)
  (cond ((eq? func '+) (+ (car args) (cadr args)))
        ((eq? func '-) (- (car args) (cadr args)))
        ((eq? func '*) (* (car args) (cadr args)))
        ((eq? func '/) (/ (car args) (cadr args)))))


