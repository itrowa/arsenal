

;
; build an entry from a set of names and a list of values.(name sugar)
(define new-entry build)


;lookup-in-entry的功能是,在entry中查找list1是否有等于name的,如果有,
;那么把list2中对应的元素返回出来。
;
(define lookup-in-entry
  (lambda (name entry entry-f)
    ;就是调用另外一个函数啊
    (lookup-in-entry-help name
                          (first entry)
                          (second entry)
                          (entry-f))))

; 被lookup-in-entry调用的过程
; entry-f是当name在entry的list1中找不到时调用的。
(define lookup-in-entry-help
  (lambda (name names values entry-f)
    (cond
      ((null? names) (entry-f name))
      ((eq? (car names) name) (car values))
      (else (lookup-in-entry-help name
                                  (cdr names)
                                  (cdr values)
                                  (entry-f))))))

