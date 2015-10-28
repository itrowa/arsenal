
(add-1 zero)

;->
(add-1 (lambda (f)
         (lambda (x)
           x)))
;->
(lambda (n) 
  (lambda (f)
    (lambda (x)
      (f ((n f) x)))); 过程
  (lambda (f)        ; 参数
    (lambda (x) x)))

;->
(lambda (f)
  (lambda (x)
    (f (
        ;;
        ( (lambda (f)       ;原来的n变成这里替换后的结果
            (lambda (x) x))
        ;;
         f)x)))

;; 搞清楚这一步每个括号的operator是什么，operand是什么，然后应用即可.
;; 如果很难看得清楚，就可以画一颗求值树.


 (add-1 one)
