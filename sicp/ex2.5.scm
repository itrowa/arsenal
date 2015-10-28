(define (cons-2 x y)
  (* (expt 2 x) (expt 3 y)))

(define (car-2 p)
  (if (= (remainder p 2) 0)
      (+ 1 (car-2 (/ p 2)))
      0))

(define (cdr-2 p)
  (if (= (remainder p 3) 0)
      (+ 1 (cdr-2 (/ p 3)))
      0))

;; test & usage:
(define p-1 (cons-2 3 2))
(car-2 p-1)
(cdr-2 p-1)
