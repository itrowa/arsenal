;; 定义和执行, 谁在前? 我有点一脸懵逼了.
;; 函数定义中, 调用其它函数的语句完全可以不按照顺序来, 但是, 一旦开始运行程序了, 程序就会在运行时检查name是否有对应的定义. 所以, 只要在函数
;; 运行之前把所有的定义全部定义完即可. 

(define (setup)
  (let ((l (primitive-procedure-names)))
    l))

;; help:定义一个基本过程的name-object查找表.
(define primitive-procedures
  '((car car)
    (cdr cdr)
    (null? null?)))

;; help:从primitive-procedures取出names做成列表.
(define (primitive-procedure-names)
  (map car
       primitive-procedures))
