;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 向量相关
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 框架 (frame)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 为画家的外框.画家的画将画在frame所表示的四边形中.

;; constructor: 三个向量创造一个矩形或者平行四边形作为外框.
;; ---------------------
(define (make-frame origin edge1 edge2)
  (list origin edge1 edge2))

;; selector
;; ---------------------
;; 表示框架原点的向量
(define (origin-frame frame)
  (car frame))
;; 表示框架第一条边的向量
(define (edge1-frame frame)
  (cadr frame))
;; 表示框架第二条边的向量
(define (edge2-frame frame)
  (cadr (cdr frame)))

;; 框架的坐标映射
;; 
;; 它使用一个向量frame 然后返回一个过程, 这个过程使用v向量为参数返回
;; 另一个向量,返回的新向量正是映射后的向量.
(define (frame-coord-map frame)
  (lambda (v)
    (add-vect
     (origin-frame frame)
     (add-vect (scale-vect (xcor-vect v)
                           (edge1-frame frame))
               (scale-vect (ycor-vect v)
                           (edge2-frame frame))))))
;; eg:
((frame-coord-map a-frame) (make-vect 0 0))
;; (origin-frame a-frame)



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 画家 (painter)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define wave2 (beside wave (flip-vert wave)))

(define wave4 (below wave2 wave2))

(