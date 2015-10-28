;; k项有限连分式计算过程
;; n: 只有一个参数的函数，返回一个数
;; d: 只有一个参数的函数,返回一个数
;; k: 要计算连分式的项数
(define (cont-frac n d k)
  (cont-frac-core n d 1 k))

(define (cont-frac-core n d current k) 
    (if (= current k) 
            (/ (n current) 
               (d current))
        (/ (n current) 
           (+ (d current) 
              (cont-frac-core n d (+ current 1) k)))))

;; 检查函数对于顺序的k值是否逼近1/φ
(cont-frac (lambda (i) 1.0) (lambda (i) 1.0) 20)

;; 题目问题：k需要取多大才能保证得到的近似值具有十进制的4位精度？