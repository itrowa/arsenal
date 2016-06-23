; 处理length<=0的函数
;
((lambda (mk-length)
   (mk-length ???))
 (lambda (length)
   (lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 (length (cdr list))))))))

; 处理length<=1的函数
;
((lambda (mk-length)
   (mk-length          
     (mk-length ???))) ;
 (lambda (length)
   (lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 (length (cdr list))))))))

; eval过程：
; 先计算(mk-length (mk-length ???)), 其中mk-length要被实际参数来代替
; 先代换第1个mk-length
   ((lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 (length-1 (cdr list)))))) (mk-length ???))

; 代换后length-1还需要被实际参数，也就是(mk-length ???)的值代替
; 所以先来计算一下(mk-length ???),首先把它写全
   ((lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 (length-1 (cdr list))))))

          ((lambda (length)
            (lambda (list)
              (cond
                ((null? list) 0)
                (else
                 (add1 (length (cdr list))))))) ???))  ;*

;在*处传入???以计算这个lambda函数:
;
   ((lambda (list)     ;*
     (cond
       ((null? list) 0)
       (else
        (add1 (length-1 (cdr list))))))

            (lambda (list)          ;**
              (cond
                ((null? list) 0)
                (else
                 (add1 (??? (cdr list))))))) 
;**处的Lambda函数是作为*处的lambda函数的参数的，所以再代入*

   ((lambda (list)   
     (cond
       ((null? list) 0)
       (else
        (add1 (
             ;;;;;    套了一层，而已
            (lambda (list)         
              (cond
                ((null? list) 0)
                (else
                 (add1 (??? (cdr list)))))) 
              ;;;;;;;;; 
               (cdr list)))))))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;改进版

((lambda (mk-length)
   (mk-length          
     (mk-length mk-length))) ;把???变成mk-length
 (lambda (length)
   (lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 (length (cdr list))))))))

;如果验证一下就可以发现，没什么问题，就是计算结果???的地方被以下函数代替了：
;
(lambda (length)
  (lambda (list)
    (cond
      ((null? list) 0)
      (else
       (add1 (length (cdr list)))))))

;再改进这个函数;
;如果注意到刚才版本的写法中，mk-length是作为lambda(mk-length)的参数，而且
;length是作为lambda(length)中的参数，而且这两个参数相互没关系，那干脆把length写成
;mk-length
;
((lambda (mk-length)
          ;  1
   (mk-length          
     ;2
     (mk-length mk-length))) 
    ;    3           4
 (lambda (make-length)
   (lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 (mk-length (cdr list))))))))

; 再抽象一下。这里有个神来之笔，不过还没到key-trick

((lambda (mk-length)
   (mk-length          
     ;;1
     (mk-length mk-length))) 
         ;2          ;3
 (lambda (make-length) ;
   (lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 ((mk-length eternity) (cdr list))))))))


; 怎么理解这个函数呢;
;以下先来看一个只能处理<=0的情况的函数吧..
;eval过程：
;
(((lambda (mk-length)
     (mk-length mk-length)) 
 (lambda (make-length) ;
   (lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 ((mk-length eternity) (cdr list)))))))) '(apple))

;首先，用
 (lambda (make-length) ;
   (lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 ((mk-length eternity) (cdr list)))))))
;传入   
((lambda (mk-length) ...)   '(apple))

;成为
;
   ((((lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 ((mk-length eternity) (cdr list))))))) mk-length) '(apple))
                  ; 1
                  
;1处的mk-length还需要再把实代带进来

   ((((lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 ((

                 (lambda (list)
                  (cond
                    ((null? list) 0)
                    (else
                     (add1 ((mk-length eternity) (cdr list))))))
                eternity) (cdr list))))))) 
   
                                                                 ) '(apple))
;现在apple可作为参数传入(lambda (list))！ 调用一下发现，这个求值过程将一直持续。除非传入的l是'()

;现在真正的key-trick来了。我们把lambda(mk-length)中的(mk-length eternity)用一个self-application
;(mk-length mk-length)代替.为什么这样做？因为其实最后那个函数无论是eternity或者是mk-length，
;代码都能自己调用自己了.


((lambda (mk-length)
   (mk-length          
     ;;1
     (mk-length mk-length))) 
         ;2          ;3
 (lambda (make-length) ;
   (lambda (list)
     (cond
       ((null? list) 0)
       (else
        (add1 ((mk-length mk-length) (cdr list))))))))



; 上面的代码确实能工作,但问题是，它不太像原来的lambda(length)了.
; 干脆想办法把(mk-length mk-length)弄出去
; 再抽象
;
((lambda (mk-length)
   (mk-length mk-length))
 (lambda (mk-length)
   ;;;;;;;;
   ((lambda (length)
      (lambda (list)
        (cond
          ((null? list) 0)
          (else
           (add1 (length (cdr list)))))))
   ;;;;;;;;;
   (lambda (x)
     ((mk-length mk-length) x)))))

; 刚刚用注释括起来的部分很像是~ 现在把它也拿到外面去

((lambda (le)
   ((lambda (mk-length)
      (mk-length mk-length))
    (lambda (mk-length)
      (le (lambda (x)
            ((mk-length mk-length) x))))))
 ;;;;;;;;;;;;;;;;
 (lambda (length)
    (lambda (list)
      (cond
        ((null? list) 0)
        (else
         (add1 (length (cdr list))))))))

; 现在lambda(length)函数成功和mk-length的自调用分离了!
; 而且注释分隔的上半部分就是y-combinator
;
; 现在把mk-length写为f 更简洁些:

((lambda (le)
   ((lambda (f) (f f))
    (lambda (f)
      (le (lambda (x) ((f f) x))))))
 ;;;;;;;;;;;;;;;;
 (lambda (length)
    (lambda (list)
      (cond
        ((null? list) 0)
        (else
         (add1 (length (cdr list))))))))

; 现在用define语句定义y-combinator
;
(define Y
  (lambda (le)
   ((lambda (f) (f f))
    (lambda (f)
      (le (lambda (x) ((f f) x)))))))

;用Y来递归调用匿名函数简直不能再简洁：
;
((Y (lambda (length)
     (lambda (list)
       (cond
         ((null? list) 0)
         (else
          (add1 (length (cdr list))))))))

 '(a b c d e f g h i j))

; ==> 10
