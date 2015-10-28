;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 用升序的list表示集合
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; is x a member of set?
(define (element-of-set? x set)
  (cond ((null? set) #F)
        ((= x (car set)) #T)
        ((< x (car set)) #F)
        (else (element-of-set? x (cdr set)))))

;; return a intersection set of set1 and set2
(define (intersection-set set1 set2)
  (if (or (null? set1) (null? set2)) ;; 这一行不能放在let中,因为let中有(car set1).如果set1为空,car过程将引发错误.
      '()
      (let ( (x1 (car set1))
             (x2 (car set2)))
         (cond ((= x1 x2)
                (cons x1
                      (intersection-set (cdr set1) (cdr set2))))
               ((< x1 x2)
                      (intersection-set (cdr set1) set2))
               ((> x1 x2)
                      (intersection-set set1 (cdr set2)))))))

;; return a set with x joined with set.
(define (adjoin-set x set1)
  (cond ((null? set1) x)
        ((< x (car set1)) (cons x set1))
        ((= x (car set1)) set1)
        (else (cons (car set1) (adjoin-set x (cdr set1))))))

(define (union-set set1 set2)
  (cond ((and (null? set1) (null? set2)) '())
        ((null? set2) set1)
        ((null? set1) set2)
        (else       
          (let ((x1 (car set1))
                (x2 (car set2)))
               (cond ((< x1 x2) (cons x1 (union-set (cdr set1) set2)))
                     ((= x1 x2) (cons x1 (union-set (cdr set1) (cdr set2))))
                     ((< x2 x1) (cons x2 (union-set set1 (cdr set2)))))))))

;; test
(define s1 (list 1 2 3))
(define s2 (list 2 3 4))
(define s3 (list 7 8 9))

(element-of-set? 1 s1)
;#t
(element-of-set? 4 s1)
;#f
(adjoin-set 5 s2)
;(2 3 4 . 5)
(intersection-set s1 s2)
;(2 3)
(union-set s1 s2)
;(1 2 3 4)
(union-set s1 s3)
;(1 2 3 7 8 9)
(union-set '() s2)
;(2 3 4)
(union-set  s2 '())
;(2 3 4)
(union-set '() '())
;()


      