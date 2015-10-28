;; church num 0
(define zero (lambda (f) 
               (lambda (x) 
                 x)))

;; church add 1
(define (add-1 n)
  (lambda (f) 
    (lambda (x) 
      (f ((n f) x)))))

;; 直接定义 church num 1, 应用代换模型展开(add-1 zero)即可.
(define one
  (lambda (f)
    (lambda (x)
      (f x))))

;; 直接定义 church num 2, 应用代换模型展开(add-1 one)即可.
(define two
  (lambda (f)
    (lambda (x) (f (f x)))))
