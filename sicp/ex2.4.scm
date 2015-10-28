;; ex2.4 
;; 习题解答见onenote.这里给出解题完成后所得到的一种定义pair的方式:


;; constructor:
(define (cons-1 x y)
  (lambda (m) (m x y)))

;; selector:
(define (car-1 z)
  (z (lambda (p q) p)))

(define (cdr-1 z)
  (z (lambda (p q) q)))


;; test & usage:
(define p-1 (cons-1 1 2))
(car-1 p-1)
(cdr-1 p-1)
