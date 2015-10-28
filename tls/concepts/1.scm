;part fun, total fun
;
;
;一个永远不会跳出的函数，因为它递归定义了自己：
;
(define eternity
  (lambda (x)
    (eternity x)))

;图灵的停机问题


;到底什么是define? 什么又是recursive definition?
;来看length函数：
(define length
  (lambda (l)
    (cond
      ((null? l) 0)
      (else (add1 (length (cdr l)))))))
;它可以正常地工作。但如果把第一行的define字样去掉？函数主体中的length就没有可以参考的length了。
;
;因为我们要研究到底什么是define，所以接下来都不能用define语句
;
;----------------------------------------------------------
;v1
;
;再看这个函数
(lambda (l)
  (cond
    ((null?? l) 0)
    (else (add1 (eternity (cdr l))))))
;如果给它的参数是非空的list，那么那么它肯定no answer.
;给他叫做length0好了。

;写一个能计算包含一个或一个以下元素的list的长度的函数
; length<=1
(lambda (l)
  (cond
    ((null? l) 0)
    (else (add1 (length0 (cdr l))))))

;因为我们要讨论啥是define所以不能像上面那样直接套定义好的length0，所以
;直接把length0的定义放进去
(lambda (l)
  (cond
    ((null? l) 0)
    (else (add1 
            ;;;;;;;
            (lambda (l)
              (cond
               ((null? l) 0)
               (else (add1 (eternity (cdr 1))))))
            ;;;;;;;
             (cdr l)))))

;照此写一个length<=2
(lambda (l)
  (cond
    ((null? l) 0)
    (else (add1 
            ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;; 
            (lambda (l)
              (cond
               ((null? l) 0)
               (else (add1 
                       ;;;;;;;;;;;;;;;;;;;;;
                       (lambda (l)
                         (cond
                           ((null? 1) 0)
                         (else (add1 (eternity (cdr 1))))))
                       ;;;;;;;;;;;;;;;;;;;;;
                         (cdr 1))))))
            ;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
             (cdr l))))

;  现在考虑优化：
;  不可能写出无穷长度的程序来满足各种数目的lat长度的需要；
;  这种程序结构具有自相似性；
;  所以应用 9th commandment 把有same nature的地方提炼出来重构

; --------------------------------------------------------
; v2
;
; 写一个很像v1中的函数,但是要以(lambda (length)..开头,而且
; 把eternity作为参数传入lambda函数中..
;
;   ((lambda (length) ...)   eternity)
;
((lambda (length)
   (lambda(l)
     (cond
       ((null? l) 0)
       (else (add1 (length (cdr l)))))))        
 
 eternity)
;注意eternity带入后，其实就和v1版本的一模一样了

;length<=1
; 注意这次定义的时候我们连lambda申明的形式参数都换了一个名字
; 但是换个名字 不影响本质
;
; ( (lambda (f) ...) ((lambda (g) ...) eternity) )
;          ↑          --------------------------
;          ----------------参数
;
; eval过程：
; 要计算(lambda (f)) 就要计算后面的参数，即
;  ((lambda (g) ...) eternity)
;  而这个东西求值又需要把eternity带入到lambda(g)中..
;
((lambda (f)
   (lambda(l)
     (cond
       ((null? l) 0)
       (else (add1 (f (cdr l)))))))        

    ((lambda (g)
      (lambda(l)
        (cond
          ((null? l) 0)
          (else (add1 (g (cdr l)))))))

     eternity) 
 )

;length<=2
;; omitted
;;

;------------------------------------------------------
;ver3
;P164
;length<=0
;
;又重构..这个和ver2有什么区别？
;留意到ver2中还是有不少重复书写的部分.
;所以再优化，把重复的部分写成lambda函数，作为参数传入。
;
; ((lambda (mk-length) ...)(lambda (length) ...))
;
((lambda (mk-length)
   (mk-length eternity))
 (lambda (length)
   (lambda(l)
     (cond
       ((null? l) 0)
     (else (add1 (length (cdr l))))))))


;from length 1
((lambda (mk-length)
   (mk-length 
     (mk-length eternity) );这一行是作为上一行的参数
   ;解释一下：eternity传到最内层的mk-length,然后结果又作为参数
   ;传到外面一层的mk-length.
 (lambda (length)
   (lambda(l)
     (cond
       ((null? l) 0)
     (else (add1 (length (cdr l))))))))

 ;length2,3,4 省略了
 ;
 ;---------------------------------------
 ;ver4
 ;
 ;length0
 ((lambda(mk-length)
    (mk-length mk-length)) 
  ;以下是作为参数传入到上面的lambda函数
  (lambda (length)
    (lambda(l)
      (cond
        ((null? l) 0)
        (else (add1 (length (cdr l))))))))

;length<=1
 ((lambda(mk-length)
    (mk-length mk-length)) 
  (lambda (length)
    (lambda(l)
      (cond
        ((null? l) 0)
        (else (add1 ((mk-length eternity) (cdr l))))))))
