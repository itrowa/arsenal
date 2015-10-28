;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 用未排序的list表示集合
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; is x a member of set?
(define (element-of-set? x set)
  (cond ((null? set) #F)
        ((equal? x (car set)) #T)
        (else (element-of-set? x (cdr set)))))

;; return a set with x joined with set.
(define (adjoin-set x set)
  (if (element-of-set? x set)
      set
      (cons x set)))

;; return a intersection set of set1 and set2
(define (intersection-set set1 set2)
  (cond ((or (null? set1) (null? set2)) '())
        ((element-of-set? (car set1) set2)
          (cons (car set1)
                (intersection-set (cdr set1) set2)))
        (else (intersection-set (cdr set1) set2))))

;; return a union set of set1 and set2.
(define (union-set set1 set2)
  (cond ((and (null? set1) (null? set2)) '())
        ((null? set2) set1)
        ((null? set1) set2)
        ((element-of-set? (car set1) set2)
          (union-set (cdr set1) set2))
        (else (cons (car set1)(union-set (cdr set1) set2)))))

;; test
(define s1 (list 1 2 3))
(define s2 (list 2 3 4))
(define s3 (list 7 8 9))

(element-of-set? 1 s1)
(element-of-set? 4 s1)
(adjoin-set 5 s2)
(intersection-set s1 s2)
(union-set s1 s2)
(union-set s1 s3)
(union-set '() s2)
(union-set  s2 '())
(union-set '() '())