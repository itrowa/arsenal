(load "ch1_utility.scm")

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 求函数的不动点(可以打印中中间计算过程)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define tolerance 0.00001)

(define (fixed-point f first-guess)
  ; 判断v1是否足够接近v2
  (define (close-enough? v1 v2)
    (< (abs (- v1 v2 )) tolerance))
  ; 优化guess值，直到guess值已经成为f的不动点
  (define (try guess)
    ;; 新添加的部分
    (display guess)
    (newline)
    (let ((next (f guess)))
      (if (close-enough? guess next)
            next
          (try next))))
  (try first-guess)
  (display "Done!")
  (newline))

;; test
(fixed-point cos 1.0)

;; 计算x^x=1000的根(通过寻找f(x)=log(1000)/log(x)的不动点)

;; f(x)=1og(1000)/log(x)
(define (target-func x)
  (/ (log 1000) (log x)))

;; f(x) = (1/2)(log1000/logx + x)
(define (target-func-with-avg x)
(* (/ 1 2)(+ (/ (log 1000) (log x)) x)))


;; 计算不带平均阻尼的方程对应的函数的不动点
(display "--- fixed-point without avg ---")
(newline)
(fixed-point target-func 1.2)
;; 计算带平均阻尼的方程对应的函数的不动点
(display "--- fixed-point with avg ---")
(newline)
(fixed-point target-func-with-avg 1.2)