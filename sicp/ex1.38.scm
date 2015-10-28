(load "ex1.37.scm")

(define N (lambda (i) 1.0))

;; 想了半天都想不起来这个通项的求法.
(define (D i)
  (if (= 0 (remainder (+ i 1) 3))
            (* 2 (/ (+ i 1) 3))
            1))

;; apply the calculation.
(cont-frac N D 20)
;; 结果应该是0.71, 因为这是e-2的值(e=2.71)