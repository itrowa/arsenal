; it works!
(define multirember&co
  (lambda(a lat col)
    (cond
      ;1
      ((null? lat) 
       (col(quote())(quote())))
      ;2
      ((eq?(car lat) a)
       (multirember&co a (cdr lat)
         (lambda(newlat seen)
           (col newlat (cons (car lat) seen)))))
      ;3
      (else
        (multirember&co a (cdr lat)
          (lambda(newlat seen)
            (col (cons (car lat) newlat) seen )))))))

;现在再定义collector
(define a-friend
  (lambda(x y)
    (null? y)))
;note: y是空的时候返回#t,否则#f

;当理解了函数的工作原理以后，试着套一下这样的参数：
; a is tuna
; lat is ()
; col is a-friene
; #t
;
; -----
;
; a is tuna
; lat is (tuna)
; col is a-friend
; #f
;
; 总结一下
; (multirember&co a lat col)这个函数通过在cond中问问题，逐个比对lat中的元素
; 是否等于a，如果等于(分支2)那么递归调用自己，但是同时完成一件额外的事情：第3个参数传入一个包含col(有两个参数)的lambda函数
; 它负责把等于a的lat元素放到seen这一支；  如果不等于a,那么执行else中的，把不等于a的lat元素放到newlat这一支。
; 函数完成后，调用 col(ls1 ls2),其中前ls1是newlat那一支，后一个元素是seen那一支。
;
;col叫做collector，也叫continuation


; 书上还有两个例子来让我们练习如何写&co的函数，一个是
; multiinserrtLR&co
; 另一个是
; (evens-only*&co



