;continuation passing style 的理解

(define last-function
  (lambda (x y)
    (length x)))

(define when-match
  (lambda (newlat seen)
    (col newlat (cons (car lat) seen))))

(define when-differ
  (lambda (newlat seen) 
    (col (cons (car lat) newlat) seen)))

(define multirember&co
  (lambda (a lat col)
    (cond
      ((null? lat)
       (col '() '()))
      ((eq? (car lat) a)
       (multirember&co a
                       (cdr lat)
                       (when-match)))
      (else
       (multirember&co a
                      (cdr lat)
                      (when-differ))))))
    