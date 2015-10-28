;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; list-ref过程: 返回list的n个元素值
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 参数是一个list和数字n，返回这个list的第n项.
(define (list-ref-1 items n)
  (if (= n 0)
      (car items)
      (list-ref (cdr items) (- n 1))))

;; @test
(define squares (list 1 4 9 16 25))
(list-ref-1 squares 3)
; 16

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; length过程: 返回list的长度
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 返回sequence的长度.
;; 递归版
(define (length-1 items)
  (if (null? items)
      0
      (+ 1 (length (cdr items)))))

;; 返回sequence的长度.
;; 迭代版
(define (length-1-iter items)
  (length-1-iter-core items 0))

(define (length-1-iter-core items cnt)
  (if (null? items)
      cnt
      (length-1-iter-core (cdr items) (+ 1 cnt))))

;; @test
(define odds (list 1 3 5 7))

(length-1 odds)
;4
(length-1-iter odds)
;4

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; append: 将两个list的元素组合在一起形成新list
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (append-1 list1 list2)
  (if (null? list1)
      list2
      (cons (car list1) (append-1 (cdr list1) list2))))

;; @test
(append-1 squares odds)
; (1 4 9 16 25 1 3 5 7)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; last-pair: 返回非空list中最后一个元素(以list的形式)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (last-pair items)
  (if (= (length items) 1)
      items
      (last-pair (cdr items))))

;; @test
(last-pair odds)
; (7)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; reverse: 以list为参数 返回的list元素顺序刚好是反的.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;(define (reverse-1 list)
;  (if (= 1 (length list))
;      (cons (car list) nil)
;      (cons (reverse (cdr list)) (car list))))
(define (reverse-1 items)
  (if (null? items)
      items
      (append-1 (reverse-1 (cdr items)) (list (car items)))))

;; @test
(reverse-1 odds)
; (7 5 3 1)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; deep-reverse
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (deep-reverse items)
  (if (null? items)
      items
      (append-1 (deep-reverse (cdr items)) (list (deep-reverse (car items))))))

;; @ test
;; reverse 和deep-reverse的区别:
(define x (list (list 1 2) (list 3 4)))
x
;; ((1 2) (3 4))
(reverse x)
(deep-reverse x)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; map
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (map-1 proc items)
  (if (null? items)
      nil
      (cons (proc (car items)) (map proc (cdr items)))))

;; @test
(map-1 abs (list -10 2.5 -11.6 17))
; (10 2.5 11.6 17)