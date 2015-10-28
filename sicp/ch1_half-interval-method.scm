;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 区间折半法
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 利用区间折半法 在一个指定的负数和正数的区间内求f的零点

(load "ch1_utility.scm")

;; 只是一个壳，包装了search过程。
;; 它包装了search过程，并处理了数范围的几种情况.
(define (half-interval-method f a b)
  (let ((a-value (f a))
        (b-value (f b)))
    (cond ((and (negative? a-value) (positive? b-value))
                (search f a b))
          ((and (positive? a-value) (negative? b-value))
                (search f b a))
          (else
                (error "Values are not of opposite sign" a b)))))


;; 在一个指定的负数和正数的区间内求f的零点
(define (search f neg-point pos-point)
  (let ((midpoint (average neg-point pos-point)))
    (if (close-enough? neg-point pos-point)
        ; consequence
        midpoint
        ; alternative
        (let ((test-value (f midpoint)))
          (cond ((positive? test-value)
                        (search f neg-point midpoint))
                 ((negative? test-value)
                        (search f midpoint pos-point))
                 (else midpoint))))))

;; help func.
(define (close-enough? x y)
  (< (abs (- x y)) 0.001))


;; usage ex:
;(half-interval-method sin 2.0 4.0)


