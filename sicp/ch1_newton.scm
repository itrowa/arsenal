#lang scheme

;; 牛顿迭代法求平方根的方法. 程序演示了如何把一个复杂程序化解为一系列基本的,简单的片段.

(define (sqrt-iter guess x)
; 牛顿迭代法求平方根的方法。 guess是猜测值， x要求平方根的那个数
	(if (good-enough? guess x)  ; 谓词判断
			; 1. 满足谓词，返回guess
			guess 
			; 2. 不满足, 继续递归计算
			(sqrt-iter (improve guess x) x)))

(define (improve guess x)
  ; 这个函数的目的是让返回的结果, 比现在的guess更接近x.
	(average guess (/x guess))
	)

(define (average x y) 
	; 求 x和y的平均数
	(/ (+ x y) 2)
	)

(define good-enough? guess x)
; 一个谓词, 判断guess的值是否足够接近x


;; ;;;;;;;;;;;;;
;; usage
;; ;;;;;;;;;;;;;

;; 求2的平方根, 初始猜测是1
(sqrt-iter 1 2)
