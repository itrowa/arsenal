; a set is a lat with no atom appear more than once.
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

;writing makeset using multirember
(define makeset
  (lambda(lat)
    (cond
      ((null? lat) (quote()))
      (else
        (cons (car lat)
              (makeset (multirember(car lat) (cdr lat))))))))
;describe how it works?
;它把car lat和后面的剩余部分的makeset递归后的结果连接起来.
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
             (subset? (cdr set1) set2))))));不太理解为什么不写#f的情况了？

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

;写一下intersect函数，他把set2中有set1的atom去掉了
(define intersect
  (lambda(set1 set2)
    (cond 
      ((null? set1)(quote()))
      ((member?(car set1) set2)
        (cons (intersect (cdr set1)) set2)
      (else (intersect (cdr set1) set2))))))

;union函数完成取交集的功能：
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

;----------------------------------------------
; 开始研究pair了
;
;a pair is a list with only 2 atoms.
;like(pear pear), (3 7),((2) (pair)), (full (house))
(define a-pair?
  (lambda (x)
    (cond
      ((atom? x) #f)
      ((null? x) #f)
      ((null? (cdr x)) #f)
      ((null? (cdr (cdr x))) #t)
      (else #f))))
      
; 为提高可读性设置以下3个函数
(define first
  (lambda (p)
    (cond
      (else (car p)))))

(define second
  (lambda (p)
    (cond
      (else (car (cdr p))))))

;用两个atom build一个pair
(define build
  (lambda (s1 s2)
    (cond
      (else (cons s1
                  (cons s2 (quote())))))))

(define third
  (lambda (l)
    (car (cdr (cdr l)))))

; rel概念: rel 表示"relation"
; (apple peaches pumpkin pie) NO
; ((apples peaches) (pumpkin pie) (apples peaches)) No!
; ((apples peaches) (pumpkin pie)) yes!
; ((4 3)(4 2)(7 5)(3 4)) yes!
;
;
;


;如果说(firsts rel)是set的话那么rel就是fun.
;例如((8 3)(4 2)(7 6)(6 2)(3 4))就是一个fun
;例如((d 4)(b 0)(b 9)(e 5)(g 4))不是，因为b重复了
(define fun?
  (lambda(rel)
    (set? (firsts rel))))

;我们是如何表达一个finite function的？
;现在来看，一个finite function 是由若干个pair组成的list，这些
;pair的第一个atom都和其它pair的第一个atom不一样.
;

;考虑这样一个revrel函数
;他把((8 a)(pumpkin pie)(got sick))变成·
;((a 8)(pie pumpkin)(sick got))
(define revrel
  (lambda rel)
    (cond
      ((null? rel)(quote()))
      (else(cons (build (second (car rel))
                        (first (car rel))
                 (revrel (cdr rel)))))))
;由于使用了build, second, first，可读性大增。

;再写一个revpair来继续增强可读性
(define revpair
  (lambda (pair)
    (build (second pair) (first pair))))

;于是重写revrel
(define revrel
  (lambda rel)
    (cond
      ((null? rel)(quote()))
      (else(cons (revpair (car rel))
                 (revrel (cdr rel))))))

;fullfun概念
;((8 3)(4 2)(7 6)(6 2)(3 4)) 不是fullfun因为在pair的第二个atom中2出现了多次
;((8 3)(4 8)(7 6)(6 2)(3 4)) 就是，因为(3 8 6 2 4)是一个set
(define fullfun?
  (lambda (fun)
    (set? (seconds fun))))
;seconds定义和firsts一样··

;fullfun 可以改名叫one-to-one, 试着重写一下它，用另外一个方式
(define one-to-one?
  (lambda (fun)
    (fun?(revrel fun))))

