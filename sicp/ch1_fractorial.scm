;计算阶乘的2个函数
;
(define (factorial n)
  ; 递归式计算阶乘
  (if (= n 1) 1
    (* n (factorial (- n 1)))))

(define (factorial_iter n)
  ; 迭代形式的函数. 虽然用到了递归, 但是计算过程是迭代式的, 一定要注意这一点.
  (if (= n 1) 1
    (* n (factorial (- n 1)))))




