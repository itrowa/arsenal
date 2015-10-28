(load "ex1.37.scm")

;; 正切函数连分式计算程序
(define (tan-cf x k) 
    (define N (lambda (i) 
                (if (= i 1) x
                    (-(* x x)))))
    (define D (lambda (i) 
                (- (* i 2.0) 1)))
    (cont-frac N D k))

;; test pi/4 = 1?
(define pi 3.141592654)
(tan-cf (/ pi 4.0) 200)