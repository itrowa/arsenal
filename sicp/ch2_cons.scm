;; 自定义的constructor: cons
;;
;; 返回一个高阶过程.
(define (cons/my x y)
  (define (dispatch m)
    (cond ((= m 0) x)
          ((= m 1) y)
          (else (error "Argument not 0 or 1 -- CONS"))))
  dispatch)

;; 自定义的selector: car 和 cdr.
(define (car/my z) (z 0))
(define (cdr/my z) (z 1))


;; usage  && test:
(define d1 (cons/my 1 2))
(car/my d1)
(cdr/my d1)
