;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; program from ch 1.3.1 求和
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 计算从a加到b的所有整数之和：
;; ex: (sum-of-integers 3 5)
;; 3+4+5
(define (sum-of-integers a b)
  (if (> a b)
      0
      (+ a (sum-of-integers (+ a 1) b))))

;; 取得cube过程的定义
(load "ch1_utility.scm")

;; 计算从a到b所有整数的立方和.
;; eg:
;; (sum-cube 3 5)
;; 3*3*3 + 5*5*5
(define (sum-cube a b)
  (if (> a b)
      0
      (+ (cube a) (sum-cube (+ a 1) b))))

;;     1       1       1
;;   ----- + ----- + ----- etc.
;;    1*3     5*7     9*11
(define (pi-sum a b)
  (if (> a b) 
      0
      (+ (/ 1.0 (*a (+ a 2))) (pi-sum (+ a 4) b))))
        ;    1
        ;--------   +   (pi-sum (+ a 4) b) 
        ;a*(a+2)
        
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 统一的写法
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (sum term a next b)
    ;; sum: 通用求和函数.
    ;; term: 每次要求和的内容. 如果是累加的情况 term就是当前的a值.
    ;; a: 求和下限
    ;; b: 求和上限.
    ;; next:  一个函数, 他给出a递增后下一个数是多少.
    (if (> a b)
        0
        (+ term (sum (next a) next b) 
        )

        
;; 利用新定义好的过程重构sum-cube

;; 定义一个函数, 输入n返回n+1
(define (inc1 num)
  (+ 1 num))

;; 利用抽象的方式来重新定义计算a到b的所有整数的立方和的函数.
(define (sum-cubes-high a b)
(sum a inc1 b))