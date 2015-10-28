(define (make-frame origin edge1 edge2)
  (list origin edge1 edge2))

;; selector的实现
(define (origin-frame frame)
  (car frame))
(define (edge1-frame frame)
  (cadr frame))
(define (edge2-frame frame)
  (cadr (cdr frame)))

;; test


(define (make-frame-1 origin edge1 edge2)
  (cons origin (cons edge1 edge2)))

;; selector的实现
(define (origin-frame frame)
  (car frame))
(define (edge1-frame frame)
  (cadr frame))
(define (edge2-frame frame)
  (cadr (cdr frame)))