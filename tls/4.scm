;4. number games

(define add1 
  (lambda (n)
    (+ n 1)))

;thus, (add1 67) equals to 68

(define sub1
  (lambda (n)
    (- n 1)))

;现在考虑一个函数可以把两个整数加起来
; (plus 3 6) 等于9 这种
; 书里面是空心的+号
(define plus
  (lambda (n m)
    (cond
      ((zero? m) n)
;      (else (add1 n sub1(m)) 
;      (else (plus (add1 n) (sub1(m))) ))))
       (else (add1(plus n (sub1 m)))))))
; 这样解释：拿一组参数 3 3为例(n=3, m=3)
; 跟踪参数变化
; 原始:(plus 3 3)
; -> (add1(plus 3 2))
; 注意上面(plus 3 2) 还没求值出来，还需要递归)
; -> (add1(add1(plus 3 1)))
; 注意上面(plus 3 1) 还没求值出来，还需要递归)
; -> (add1(add1(add1(plus 3 0))))
; 注意上面(plus 3 0) 还没求值出来，还需要递归，递归后发现值就是3)
; = 1 + 1+ 1 +3
 

;现在考虑一个函数可以把把第二个数从第一个减去
; (minus 4 3) 等于1 这种
; 书里面是空心的-号
(define minus
  (lambda (n m)
    (cond
      ((zero? m) n)
       (else (sub1(minus n (sub1 m)))))))

;现在考虑一个addup函数，它可以处理一个列表中的数，把所有的数全部加起来
;例如 (addup 3 4 5) 等于 12
(define addup
  (lambda (tup)
    (cond
      ((null? tup) 0)
      (else(plus (car tup) (addup(cdr tup)))))))

;现在考虑一个mtply函数，
;例如 (mtply 4 5) 等于 20
;书里面的x号
(define mtply
  (lambda (n m)
    (cond
      ((zero? m) 0)
      (else
        ;采用把乘法化成加法的方法
        ;4*5
        ;5 + 4*4
        ;5 + 5 + 4*3
        ;..
        (plus n (mtply n (sub1 m)))))))
       ;上面这一句算下来
       ;(mtply 4 5)
       ;(plus 4 (mtply 4 4))
       ;再递归， 
       ;(plus 4 ((plus 4 (mtply 4 3))))
       ;...


; eqan?比较a1和a2是否为同样的原子。
; eqan?很大程度上可以替代eq?了
(define eqan?
  (lambda(a1 a2)
    (cond
      ((and(number? a1)(number? a2))(= a1 a2))
      ((or(number? a1)(number? a2)) #f)
      (else(eq? a1 a2))
      ;仔细思考为什么问这三个问题而且排布顺序是这样的？
      ;Q1要两个都是数才进入
      ;能进入Q2的肯定只有一个是数，如果两个都是数那肯定进Q1了
      ;能进Q3的肯定两个都不是数
      ;根据是不是数，从上到下条件变宽。
    )
  )
)

