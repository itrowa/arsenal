; a set is a lat with no atom appear more than once.

;;
(define set?
  (lambda (lat)
    (cond
      ((null? lat) #t)
      ((member? (car lat) (cdr lat)) #f)
      (else
        (set? (cdr lat))))))
; 鉴于member?函数是用equal?而不是eq?写的所以可以处理里面的atom是数字的情形

;makeset函数用于从一个lat创建set.(清除冗余的atom)
(define makeset
  (lambda (lat)
    (cond
      ((null? lat) (quote()))
      ((member? (car lat)(cdr lat))
        (makeset (cdr lat)))
      (else (cons (car lat)
                  (makeset (cdr lat)))))))

;
;试写subset?函数
(define subset?
  (lambda (set1 set2)
    (cond
      ((null? set1) #t)
      (else
        (cond
          ((member? (car set1) set2) subset? (cdr set1) set2)
          (else #f))))))

;现在用and重写subset?函数
(define subset?
  (lambda (set1 set2)
    (cond
      ((null? set1) #t)
      (else
        (and (member? (car set1) set2)
             (subset? (cdr set1) set2))))));不太理解为什么不写#f的情况了?

;eqset?
(define eqset?
  (lambda (set1 set2)
    (cond
      ((subset? set1 set2)
       (subset? set2 set1))
    (else #f))))


;define eqset? using only one cond-line
(define eqset?
  (lambda (set1 set2)
    (cond
      (else
        (and (subset? set1 set2)
             (subset? set2 set1))))))

;再简化
(define eqset?
  (lambda (set1 set2)
    (and (subset? set1 set2)
             (subset? set2 set1))))

;---------------------------------------------------

;if at least one atom in set1 is in set2 ,(intersect? set1 set2) is true
(define intersect?
  (lambda(set1 set2)
    (cond
      ((null? set1) #t)
      (else
        (cond
          ((member? (car set1) set2) #t)
          (else 
            (member? (intersect (cdr set1) set2))))))))

;简写(intersect? set1 set2)
(define intersect?
  (lambda(set1 set2)
    (cond
      ((null? set1) #t)
      ((member? (car set1) set2) #t)
      (else 
        (member? (intersect (cdr set1) set2))))))

;用or简写intersetct
(define intersect?
  (lambda(set1 set2)
    (cond
      ((null? set1) #t)
      (else 
        (or (member? (car set1) set2) #t)
            (member? (intersect (cdr set1) set2))))))

;写一下intersect函数,他把set2中有set1的atom去掉了
(define intersect
  (lambda(set1 set2)
    (cond 
      ((null? set1)(quote()))
      ((member?(car set1) set2)
        (cons (intersect (cdr set1)) set2)
      (else (intersect (cdr set1) set2))))))

;union函数完成取交集的功能:
;set1 is (stewed tomatoes and macaroni casserole)
;set2 is (macaroni and cheese)
;result is (stewed tomatoes casserole macaroni and cheese)
(define union
  (lambda(set1 set2)
    (cond
      ((null? set1) set2)
      ((member?(car set1) set2)
        (union(cdr set1) set2))
      (else
        (cons (car set1)
              (union (cdr set1) set2))))))

(define xxx)
;

;写一个intersectall 函数
;这里假定(l-set不是空的)
(define intersectall
  (lambda (l-set)
    (cond
      ((null?(cdr lat)) (car lat))
      (else (intersect (car l-set))
                       (intersectall(cdr l-set))))));还未完全理解