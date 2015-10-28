(define (f g)
    (g 2))

;; supplement func
(define (square a) * a a)

;; test
(f square)
(f (lambda (z) (* z (+ z 1))))

;; here is the question: what's the output?
;(f f)