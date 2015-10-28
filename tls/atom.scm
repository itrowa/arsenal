;; see pg10
(define atom?
  (lambda (x)
    (and (not (pair? x)) (not (null? x)))))
