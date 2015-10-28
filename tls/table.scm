; 实现table,存储上下文(环境)的东西

;putting an new antry in front of an old table
(define extend-table cons)



; 最重要的函数就是lookup-in-table,它调用 lookup-in-entry
;
; 在table 中找哪个set的第一个list是否有等于name的,如果
; 找到了就输出这个set对应第二个list的元素.
(define lookup-in-table
  (lambda (name table table-f)
    (cond
      ((null? table) (table-f name))
      (else (lookup-in-entry name
                             (car table)
                             (lambda (name)
                               (lookup-in-table name
                                                (cdr table)
                                                table-f)))))))