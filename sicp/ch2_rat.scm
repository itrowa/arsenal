;;; assume we have make-rat, numer, denom functions.

;; 定义有理数的四则运算过程.

(define (add-rat x y)
  (make-rat (+ (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (demon x) (denom y)) ) )

(define (sub-rat x y)
  (make-rat (- (* (numer x) (denom y))
               (* (numer y) (denom x)))
            (* (demon x) (denom y)) ) )

(define (mul-rat x y)
  (make-rat (* (numer x) (numer y))
            (* (denom x) (denom y))))

(define (div-rat x y)
  (make-rat (* (numer x) (denom y))
            (* (denom x) (numer y))))


(define (equal-rat? x y)
  (= (* (numer x) (denom y))
     (* (numer y) (denom x))))


;; ++++++++++++++++++++++++++++++++++++++++++++++++++
;; abstractction barrier
;; ++++++++++++++++++++++++++++++++++++++++++++++++++

;; implement constructor and selector.

;; constructor
;; 特点: 1.将分数归约至最简形式;
;;       2.正确处理负数: 当分子分母都是负时, 构造出的应该
;;       分子分母都处理为正. 只有一个为负时,只让分子为负.
;; @todo 这个判断条件还可以继续优化.
(define (make-rat n d)
  (let ((g (gcd (abs n) (abs d))))
    (cond ((and (< n 0) (< d 0))
              (cons (/ (- n) g) (/ (- d) g)))           
          ((< d 0)
              (cons (/ (- n) g) (/ (- d) g)))
          (else (cons (/ n g) (/ d g))))))

;; selector
(define (numer x) (car x))
(define (denom x) (cdr x))

;; 辅助函数, 用于方便浏览
(define (print-rat x) 
	(newline) ; 随后的打印会在新的一行产生
	(display (numer x))
	(display "/")
	(display (denom x)))



;; example
;;
(define one-half (make-rat 1 2))
(define one-third (make-rat 1 3))
(print-rat one-half)
(print-rat one-third)
(newline)
(display "below are some rational nums with positive components:")
(define rat-1 (make-rat -1 -2))
(define rat-2 (make-rat 1 -2))
(define rat-3 (make-rat -1 2))
(print-rat rat-1)
(print-rat rat-2)
(print-rat rat-3)

