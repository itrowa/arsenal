;; constructor & selecor
(define (make-vect x y) (cons x y))
(define (xcor-vect v) (car v))
(define (ycor-vect v) (cdr v))

;; 两个向量相加
(define (add-vect v1 v2)
  (make-vect 
    (+ (xcor-vect v1)
       (xcor-vect v2))
    (+ (ycor-vect v1)
       (ycor-vect v2))))
     
;; 两个向量相减(v1-v2)
(define (sub-vect v1 v2)
    (make-vect 
    (- (xcor-vect v1)
       (xcor-vect v2))
    (- (ycor-vect v1)
       (ycor-vect v2))))

;; 对向量的伸缩: 返回s 倍的v向量
(define (scale-vect s v)
  (make-vect
    (* s (xcor-vect v))
    (* s (ycor-vect v))))

;; test
(define v1 (make-vect 1 2))
(define v2 (make-vect 2 3))
(xcor-vect v1)
(ycor-vect v1)

(add-vect v1 v2)
(sub-vect v1 v2)

(scale-vect 10 v1)
