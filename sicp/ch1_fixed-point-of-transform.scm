;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 最后的抽象
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 考虑到无论是“平滑阻尼的不动点程序”，还是“牛顿法”求根的程序，
;; 两种方法都是从一个函数除法，找出这个函数在某种变换（从f(x)变换
;; 为(x+f(x)/2,或者f(x)变换为Df(x)）下的不动点，所以又可以把这种
;; 普遍性的思想表述为一个过程.

(load "ch1_utility.scm")
(load "ch1_fixed-point.scm")

;; 对函数g进行变换 然后进行不动点猜测,这是本章抽象级别最高的一个过程.
(define (fixed-point-of-transform g transform guess)
  (fixed-point (transform g) guess))

;; 例子
;; 求平方根(寻找y|->x/y在平均阻尼下的不动点)
(define (sqrt-4 x)
  (fixed-point-of-transform (lambda (y) (/ x y)) average-damp 1.0))

;; 求平方根(用牛顿法找y|->y^2-x的牛顿变换的不动点)
(define (sqrt-5 x)
  (fixed-point-of-transform (lambda (y) (- (* y y) x)) newton-transform 1.0))
