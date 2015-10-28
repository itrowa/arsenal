(load "1.1.7 newton.scm")

(define (cube_root x)
  (if (good-enough? guess x)
    ; !yes  
    guess
    ; otherwise
    (cube_root (improve guess x))
  ))

(define (improve guess x)
  (/ (+ (/ x (* y y)) (* 2 y)) 3)
  )