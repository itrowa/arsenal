;; 求数a 的b次幂

(define (expr a b)
  (if (= b 0 )
        1
        (* a (expr a (- b 1)))))

;; 迭代版. scheme没有循环, 只能用递归代替.
;; counter是循环计数器, product是当前的计算结果.
(define (expr-iter counter a b product)
    (if (> counter b)
        product
        (expr-iter (+ counter 1) a b (* product a) )))

(define (three-to-two) (expr-iter 1 2 3 1))