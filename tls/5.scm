; 5. *Oh my Gawd*: it's full of stars
; 写了一大堆带*的函数

;构造函数rember*
(define rember*
  (lambda (a l)
    (cond
      ;Q1 always ask null?
      ((null? l)(quote()))
      ;Q2 如果car l是atom
      (atom? (car l))
        ((eq? (car l) a) (rember* a (cdr l)))
        (else (cons (car l) (rember* a (cdr l))))
      ;Q3 如果car l 不是atom
      (else (cons (rember* (car l) (rember* (cdr l))))))))

;构造函数insertR*
;它的作用是把把new插入到l中old的右边
(define insertR*
  (lambda (old new l)
    (cond
      ;Q1 always ask..
      ((null? l)(quote()))
      ;Q2 car l 是不是atom
      (atom? (car l))
        (cond
          ;car l是atom
          (eq? (car l ) old) 
            ;如果l的第一个atom和old相等
            (cons (car l) (cons new (insertR* old new (cdr l))))
            ;如果l的第一个atom和old不等
            (else (cons (car l) (insertR* old new (cdr l)))))
        ;car l不是atom
        (else (cons (insertR* (car l) (insertR* (cdr l))))))))

;构造函数occur*
;它的作用是计算l中a出现的次数
(define occcur*
  (lambda (a l)
    (cond
      ((null? l) 0)
      (atom? (car l))
      ;是atom 进入cond这个分支
      (cond
        (eq?(car l) a)
          (add1(occur* a (cdr l)))
          (else (occur* a (cdr l))))
      ;不是atom 进入下面这个分支
      (else (plus (occur* a (car l)) (occur* a (cdr l)))))))

;构造函数subst*
;它替换l中的old为new
(define subst*
  (lambda (old new l)
    (cond
      ((null? l)(quote()))
      (atom? (car l))
        (cond
          ;car l是atom
          (eq? (car l ) old) 
            ;如果l的第一个atom和old相等
            (cons new (subst* old new (cdr l)))
            ;如果l的第一个atom和old不等
            (else (cons (car l) (subst* old new (cdr l)))))
        ;car l不是atom
        (else (cons (subst* old new (car l) (subst* old new (cdr l))))))))

;构造函数insertL*
;它的作用是把把new插入到l中old的左边
(define insertL*
  (lambda (old new l)
    (cond
      ((null? l)(quote()))
      (atom? (car l))
        (cond
          ;car l是atom
          (eq? (car l ) old) 
            ;如果l的第一个atom和old相等
            (cons new (cons (car l)  (insertR* old new (cdr l))))
            ;如果l的第一个atom和old不等
            (else (cons (car l) (insertL* old new (cdr l)))))
        ;car l不是atom
        (else (cons (insertL* (car l) (insertL* (cdr l))))))))

;试写出member*函数，它判断l中是否含有a
;??????? or 是什么 意思？？？
(define member*
  (lambda (a l)
    (cond
      ;Q1
      ((null? l) #f)
      ;Q2
      ((atom? (car l))
       (or (eq?(car l) a) (member* a (cdr l))))
      ;Q3
      (else (or(member* a (car l))(member* a (cdr l)))))

;leftmost
;it finds the leftmost atom in a non-empty list of S-expressions that does not contain the empty list.
;
(define leftmost
  (lambda (l)
    (cond
      (atom? (car l))(car l)
     (else(leftmost(cdr l))) ;原文写成car l 了 是不是错了啊

; eq? 貌似只能测试非数字的atom是否相等
; 
; ------
;
; eqan? 可测试两个数字/非数字的atom是否相等
;
; ------
; 
; eqlist? 
; 
; (strawberry ice cream)
; (strawberry ice cream)
; yes
; 
; (strawberry ice cream)
; (strawberry cream ice)
; no
; 
; (beef ((sausage))(and(soda)))
; (beef ((sausage))(and(soda)))
; yes
; 
; ------ 
;
; equal?
; 用来测试两个s-exp是否相等的。s-exp可以是atom，,也可以是由list 构成的s-exp。
; lista
; (a1 (a2) ((a3)) a4)
; (a1 (a2) ((a3)) (a4 (a5))) 这种不是s-exp?

 ;(eqlist l1 l2) tests if 2 lists are equal.
 ;(eqlist l1 l2)居然要问9个问题！
 ;为什么？因为l1可能是empty / list中的atom / list中的list, l2同理，所以3*3=9种情况
 (define eqlist?
   (lambda (l1 l2)
     (cond
       ;Q1 对于l1来说，是null, l2是null
       ((and(null? l1)(null? l2)) #t)
       ;Q2 l1是null, car l2是atom
       ((and(null? l1)(atom? (car l2))) #f)
       ;Q3 l1是null, car l2是list
       ((null? l1) #f)
       ;Q4 car l1是atom, l2是null
       ((and(atom?(car l1))(null? l2)) #f)
       ;Q5 car l1是atom, l2是atom
       ((and(atom?(car l1))(atom?(car l2)))
        (and(eqan?(car l1)(car l2))(eqlist?(cdr l1)(cdr l2))));这句意思是，
         ;car l1和car l2相等，且cdr l1和cdr l2相等，就输出#t
       ;Q6 car l1是atom, car l2是list
       ((atom?(car l1)) #f)
       ;Q7 l1是list,l2是null
       ((null? l2) #f)
       ;Q8 l1是list,car l2是atom
       ((atom? (car l2)) #f)
       ;Q9 l1是list l2是list
       (else
         (and(eqlist?(car l1)(car l2))
           (eqlist?(cdr l1)(cdr l2)))))))
 ;注意逻辑判断的写法：
 ;为什么Q2里面不验证l2为非null?了？因为不需要验证了，如果l2为null那么Q1就成立了。
 ;为什么Q3里面不写关于car l2是list的判断句了？因为car l2
 ;只有3中可能，其它两种可能都在Q1,Q2写出来了，剩下的肯定是Q3了
 ;
 ;上面写的判断条件太复杂了。事实上，问题可以简化:
 ; l1和l2都null #t
 ; l1和l2只有一个是null #f
 ; car l1 和car l2都是atom
 ; car l1和car l2只有一个是atom
 ; 只剩下最后一种：car l1和car l2都是list
 ;
 ; 判断条件的写法比上面的写法还简单，主要是因为最先开始的问句问的是最特殊的，后面的问句因为情况快被穷举完了，有的判断句都可以省略不少。
 (define eqlist?
   (lambda (l1 l2)
     (cond
       ;Q1 
       ((and(null? l1)(null? l2)) #t)
       ;Q2 
       ((or(null? l1)(null? (car l2))) #f)
       ;Q3 
       (and(atom? (car l1))(atom?(car l2)))
         ((and(eqan? (car l1) (car l2))(eqlist? (cdr l1)(cdr l2)));这个还能再优化
       ;Q4
       ((or(atom? (car l1))(atom?(car l2))) #f)
       ;Q5
       (else
         (and(eqlist?(car l1)(car l2))
           (eqlist?(cdr l1)(cdr l2))))))))

 ;equal?用来判断两个s-exp是否相等
 (define equal?
   (lambda (s1 s2)
     (cond
        ((and (atom? s1)(atom? s2))(eqan? s1 s2))
        ((atom? s1) #f)
        ((atom? s2) #f)
        (else (eqlist? s1 s2)))))
       )))

; simplify it!
 (define equal?
   (lambda (s1 s2)
     (cond
        ((and (atom? s1)(atom? s2))(eqan? s1 s2))
        (or((atom? s1) (atom? s2)) #f)
        (else (eqlist? s1 s2)))))

;rewrite eqlist using equal
 (define eqlist?
   (lambda (l1 l2)
     (cond
       ;Q1  两个都是null
       ((and(null? l1)(null? l2)) #t)
       ;Q2  只有其中一个是null
       ((or(null? l1)(null? (car l2))) #f)
       ;Q3 原先的atom，list的情况，其实都可以包含在是不是s-exp的情况中。
       (else
         (and(equal? (car l1)(car l2))
           (eqlist? (cdr l1)(cdr l2))))))))
  ;; eqlist和equal到底什么区别啊:w
  ;;
