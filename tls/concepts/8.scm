;这一章研究返回函数的函数
;try to write rember-f
;rember-f是既可以使用eq?也可以使用equal?的函数。
(define rember-f
  (lambda (test? a l)
    ((null? l)(quote())
    (else (cond
            ((test? (car l) a)(cdr l))
            (else
              (cons (car l)
                    (rember-f test? a (cdr l)))))))))
;调整判断语句简化一下
(define rember-f
  (lambda (test? a l)
    (cond
      ((null? l)(quote())
      ((test? (car l) a)(cdr l))
      (else
        (cons (car l)
              (rember-f test? a (cdr l))))))))

;现在有4个几乎差不多的函数了
;rember with =
;rember with equal?
;rember with eq?
;rember-f
;rember-f是最强大的，可以generate其它几个。
;
;（自己总结：带f的函数是生成函数的函数,书中未明确给出其实它叫
;高阶函数）
;

;eq?-c带有一个参数a，它返回一个带参数x的函数，这个函数测试a是否等于x
(define eq?-c
  (lambda(a)
    (lambda(x)
      (eq? x a))))

;现在把rember-f写成只有一个arg, test?的形式
(define rember-f
  (lambda(test?)
    (lambda(a l)
      (cond
        ((null? l)(quote()))
        ((test?(car l) a)(cdr l))
        (else(cons (car l)
                   (rember-f test?) a (cdr l)))))))
                   ;和原来的函数相比就是rember-f这里只有一个参数了。

;现在用相同的方式来把把insertL处理成insertL-f
(define insertL-f
  (lambda test?
    (lambda(new old l)
      (cond
        ((null? l) quote())
        ((test? (car l) old) (cons new
                                   (cons old (cdr l))))
        (else
          (cons (car l)
                (insertL-f test?) new old (cdr l)))))))

;现在用相同的方式来把把insertR处理成insertR-f
(define insertR-f
  (lambda test?
    (lambda(new old l)
      (cond
        ((null? l) quote())
        ((test? (car l) old) (cons old
                                   (cons new (cdr l))))
        (else
          (cons (car l)
                (insertR-f test?) new old (cdr l)))))))

;考虑到insertR和insertF有相似的功能(函数定义中只有一点点区别)，写一个insert-g
;,使得这个函数既可以在左边插入又可以在右边插入。
; 注意这句：
; (cons new (cons old (cdr l)))
; (cons old (cons new (cdr l)))
; 也就是说：两个函数都要cons cdr l，不过new 和old的顺序不一样而已。
; 所以，定义两个函数
(define seqL
  (lambda(new old l)
    (cons new (cons old l))))

(define seqR
  (lambda(new old l)
    (cons old (cons new l))))

;现在可以写出insert-g了，但现在要求insert-g只接收一个参数seq,
;当seq是seqL时返回函数insertL
;当seq是seqR时返回函数insertR
(define insert-g
  (lambda (seq)
    (lambda(new old l)
      (cond
        ((null? l) quote())
        ((eq? (car l) old) (seq new old (cdr l)))
        (else
          (cons (car l)
                (insert-g seq?) new old (cdr l)))))))

;现在可以用insert-g来定义insertL和insertR了
(define insertL (insert-g seqL))
(define insertR (insert-g seqR))

;还可以用更简洁的方式定义insertL，这次传入的不是参数seqL
; 而是直接传入一个lambda：
(define insertL
  (insert-g 
    (lambda(new old l) 
      (cons new (cons old l)))))

;翻一下chpt3里面subst的定义，发现，其实和insertL，insertR差不多
;区别都在于cond那里
;写一个类似seqL,seqR的这种函数来简化subst
(define seqS
  (lambda(new old l)
    (cons new l)))

;现在可以用insert-g来定义subst了
(define subst (insert-g seqS))

;再来看一个yyy函数
;这就是我们的老朋友rember!!
;可以使用(yyy a l)来验证它。 其中 a是sausage, l是(pizza with salsage and bacon)
(define yyy
  (lambda (a l)
    ((insert-g seqrem) #f a l))) ;#f有点像是就是原来的new参数。不懂。
;其中
(define seqrem
  (lambda (new old l)
    l))

;---------------------------------------
;9th commandment
;abstract common pattens with a new funcion.
;---------------------------------------

;再把第6章的value函数抓出来抽象一下。
;先定义个辅助的函数atom-to-function，这个函数可以：
;接受参数x并且返回function plus，当 (eq? x quote(+))
;                 function mtply，当 (eq? x quote(*))
;                 function power，当 (eq? x quote(^))
(define atom-to-function
  (lambda(x)
    (cond
      ((eq? x (quote +)) plus)
      ((eq? x (quote *)) mtply)
      (else power))))
;检测一下，当nexp是(+ 5 3)时(atom-to-function (operator nexp))
;的值是 function plus.

;用atom-to-function重写value
(define value
  (lambda(nexp)
    (cond
      ((atom? nexp) nexp)
      (else
        ((atom-to-function (operator nexp)) 
          (value (1st-sub-exp nexp))
          (value (2nd-sub-exp nexp)))))))

;把multirember抽象一下
;(做笔记的时候记得把multirember的老版本也放出来。)
;multirember的定义里面有个eq? 在这里我们想要用参数test?来代替它
;multirember-f接受test?参数并返回multirember函数。
(define multirember-f
  (lambda(test?)
    (lambda(a lat)
      (cond
        ((null? lat)(quote()))
        ((test? a (car lat))
          ((multirember-f test?) a (cdr lat)))
        (else (cons (car lat)
                    ((multirember-f test?) a (cdr lat))))))))
;测试一下(multirember-f test?) a lat)
;其中test? is eq?
;a is tuna
;l is (shrimp salad tuna salad and tuna)
;结果是(shrimp salad salad and)


;现在可以定义multirember-eq?了
(define multirember-eq? 
  (multirember-f test?))
;;但要当test是eq?的时候。
;留意刚才的测试，在执行的时候，其实test?一直都是eq?，a一直都是tuna
;我们进一步考虑让test?成为一个函数，这个函数完成和luna比较的功能
(define eq?-tuna
  (eq?-c k))
;这里k是tuna
;这个函数不带参数，返回一个带x参数的函数(留意eq?-c定义),它测试x和k是否相等
;或者直接把k的值确定为tuna
(define eq?-tuna
  (eq?-c (quote tuna)))

;现在定义一个multiremberT，它接收两个参数，一个是
;test? 一个是lat。这里的test?就是前面定义好的函数eq?-tuna
(define multiremberT
  (lambda(test? lat)
    (cond
      ((null? lat)(quote()))
      ((test? (car lat))
       (multiremberT test?(cdr lat)))
      (else (cons (car lat)
                  (multiremberT test? (cdr lat)))))))

;再来一个新版的multirember
;后面会发现这就是所谓的CPS
(define multirember&co
  (lambda(a lat col)
    (cond
      ((null? lat) 
       (col(quote())(quote())))
      ((eq?(car lat) a)
       (multirember&co a (cdr lat)
         (lambda(newlat seen)
           (col newlat (cons (car lat) seen)))))
      (else
        (multirember&co a (cdr lat)
          (lambda(newlat seen)
            (col (cons (car lat) newlat) seen )))))))


