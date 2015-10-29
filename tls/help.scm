

;; 这里组织了会被程序用到的最多的集合和数据测试过程.
(load "atom.scm")
(load "lat.scm")
;(load "set.scm")
(load "pair.scm")
(load "entry.scm")
(load "table.scm")

;; curried version of eq.
(define eq?-c
  (lambda (a)
    (lambda (x)
      (eq? x a))))

;; 适用于所有atom类型的比较:数字和其它类型.P78
;; 为什么要有这个过程?: eq? 不适合比较两个数字, 如果用1和2来比较, 输出绝对是#f.
;; eqan->test eq? for atom and number
(define eqan?
  (lambda (a1 a2)
    (cond
      ((and (number? a1) (number? a2)) (= a1 a2))
      ((or (number? a1) (number? a2)) #f)
      (else (eq? a1 a2)))))

;; to test if 2 s-expressions are equal.
;; 作为eqlist?的辅助函数存在.
(define equal/my?
  (lambda (s1 s2)
    (cond
      ((and (atom? s1) (atom? s2)) (eqan? s1 s2))
      ((or (atom? s1) (atom? s1)) #f)
      (else (eqlist? s1 s2)))))

;; eqlist? test if two list are equal
(define eqlist?
  (lambda (l1 l2)
    (cond
      ((and (null? l1) (null? l2)) #t)
      ((or  (null? l1) (null? l2)) #f)
      (else
        (and (equal/my?  (car l1)(car l2))
             (eqlist? (car l1)(car l2)))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; test part
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(display "start help.scm test...")
(newline)

;; s-expression test
(equal? '(apple tuna) '(apple tuna)) ;;#t



;; lat test
(define l '(2 3 4 5 6))
(lat? l) ;;#t

;; pair test
(define tp (build 2 3 ))
(first tp)
(second tp)

;(lookup-in-entry 'entree
;                 '((appetizer entree beverage)
;                   (food      tasts  good    )))

