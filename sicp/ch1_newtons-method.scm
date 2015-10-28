;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 牛顿法
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 利用牛顿法求g(x)=0的解。其应用有：求一个数的平方根.

(load "ch1_utility.scm")
(load "ch1_fixed-point.scm")

;; 定义函数的导数(本质是从一个函数到另一个函数的变换，因此返回的是一个过程)
;;  对输入的g返回 g(x+dx)-g(x)/dx
(define (deriv g)
  (lambda (x)
    (/ (- (g (+ x dx)) (g x)) dx)))

(define dx 0.00001)

;; eg: 求函数f(x)=x^3zl 5处的导数
;((deriv cube) 5)


;; 牛顿法
;; 如果关于x的函数=g(x)可微，那么方程g(x)=0的解就是以下关于x的函数的不动点：
;; f(x)=x-g(x)/Dg(x)
;; 其中Dg(x)是g(x)的导数
;; 因此：
;; 求f(x)的不动点就能求得g(x)=0的解了

;; 把函数g转换成f,以作为要求不动点的那个函数
(define (newton-transform g)
  (lambda (x)
    (- x (/ (g x) ((deriv g) x)))))

;; 对函数g用牛顿法求g=0的解。
(define (newtons-method g guess)
  (fixed-point (newton-transform g) guess))


;; 实例：利用牛顿法求x的平方根：利用y|-> y^2 - x 的零点就是x的平方根
(define (sqrt-3 x)
  (newtons-method (lambda (y) (- (square y) x)) 1.0))

;; test
;(cube-root 8)