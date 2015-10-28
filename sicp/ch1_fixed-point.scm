(load "ch1_utility.scm")

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 求函数的不动点
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 数学原理：对函数f(x)从某个猜测值出发，反复应用f,得到
;; f(x), f(f(x)), f(f(f(x))), ... 
;; 多次以后就能得到f(x)的不动点。
(define tolerance 0.00001)

(define (fixed-point f first-guess)
  ; 判断v1是否足够接近v2
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2 )) tolerance))
  ; 优化guess值，直到guess值已经成为f的不动点
  (define (try guess)
    (let ((next (f guess)))
      (if (close-enough? guess next)
            next
          (try next))))
  (try first-guess))

;; test
(fixed-point cos 1.0)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 不动点的应用：利用不动点思想求一个数的平方根
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;
;; 求x的平方根，就是对于已知的x求y^2=x的y.
;;  而求 y^2=x中的y就是计算f(y)=x/y 的不动点. 
;; 而y=x/y 由于算法的原因不收敛(见书),所以改写表达式成为
;; y = (1/2)(y+x/y). (在方程两边都加y，然后两边都处以2)
;; 这种把f(x)变成“x和f(x)的平均值”的方法叫"平滑阻尼"技术。
(define (sqrt-1 x)
  (fixed-point (lambda (y) (average y  (/ x y))) 1.0 ))

;; test
;(sqrt-1 4)

;; 求一个函数的“平均阻尼”后的函数就是求x和f(x)的平均值.
;; 可以写为一个形式化的过程.
;; 这个过程返回的是另一个过程。
(define (avearge-damp f)
  (lambda (x) (average x (f x))))

;; 不动点+平滑阻尼：可以重新定义平方根过程：
(define (sqrt-2 x) 
  (fixed-point (average-damp (lambda (y) (/ x y))) 1.0))

;; test
;(sqrt-2 4)


;; 不动点+平滑阻尼：求立方根过程： 利用“函数f(y) = x/y^2 的不动点是x的立方根”
(define (cube-root x)
  (fixed-point (average-dump (lambda (y) (/ x (square y)))) 1.0))

;; test
;(cube-root 8)
