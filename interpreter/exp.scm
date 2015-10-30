(define x 5)

(lambda (x) (* x x))

(define sq
  (lambda (x) (* x x)))

(define sum-of-squares
  (lambda (x y) 
    (+ (sq x) (sq y))))

(define f
  (lambda (a)
    (sum-of-squares (+ a 1) (* a 2))))

;; test

;; 1. 普通的call exp
(sq x)
(f 5)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(lambda (x) 2)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define foo
  (lambda (y)
    (lambda (x)
      (+ x y))))

(define b (foo 1))
(b 2)
((foo 1) 2)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (make-withdraw balance)
  (lambda (amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        ("Insufficient funds"))))

(define W1 (make-withdraw 100))
(W1 50)

