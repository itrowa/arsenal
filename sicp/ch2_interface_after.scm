;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 1. map 实现对list中元素的映射
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

; (map square (list 1 2 3 4 5))
; (1 4 9 16 25)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 2.过滤一个sequence: 选出其中满足给定谓词的元素
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (filter predicate sequence)
  (cond ((null? sequence)'())
        ((predicate (car sequence))
         (cons (car sequence)
               (filter predicate (cdr sequence))))
        (else (filter predicate (cdr sequence)))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 3. 累积所有元素的工作
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; op: 一个过程:表示积累的方式
;; initial: 从哪一个开始
;; sequence 要积累的所有元素
(define (accumulate op initial sequence)
  (if (null? sequence)
      initial
      (op (car sequence)
          (accumulate op initial (cdr sequence)))))

;; eg
(accumulate + 0 (list 1 2 3 4 5))
; 15
(accumulate cons '() (list 1 2 3 4 5))
; (1 2 3 4 5)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; enumerate applications
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (enumerate-interval low high)
  (if (> low high)
      '()
      (cons low (enumerate-interval (+ low 1) high))))

;; eg: 从2枚举到7形成sequence
(enumerate-interval 2 7)
;; (2 3 4 5 6 7)

(define (enumerate-tree tree)
  (cond ((null? tree) '())
        ((not (pair? tree)) (list tree))
        (else (append (enumerate-tree (car tree))
                      (enumerate-tree (cdr tree))))))

;; eg
(enumerate-tree (list 1 (list 2 (list 3 4)) 5))
; (1 2 3 4 5)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 完整的信号流
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; enumerate -> filter -> map -> accumulate

;; eg: 枚举tree中所有的leaf做成序列，然后过滤出奇数数列，最后求每个元素的平方和.
(load "ch1_utility.scm") ;; square的定义

(define (sum-odd-squares tree)
  (accumulate
    +
    0
    (map square 
      (filter odd?
              (enumerate-tree tree)))))
;; test
(sum-odd-squares (list 1 (list 2 (list 3 4)) 5))
; 35