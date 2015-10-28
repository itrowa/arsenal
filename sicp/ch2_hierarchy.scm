(define aa (list 2 3 4))
(define bb (list 2 3))

aa
;(2 3 4)
bb
;(2 3)

(pair? aa)
;#t
(pair? bb)
;#t
(pair? 123)
;#f


;; (list 1 2)构造的数据和(cons 1 2)构造的数据是不同的
(define c1 (cons 1 2))

;; test
c1       ;; 是一个ill-form list
;(1 . 2)
(car c1) ;; 是一个atom
(cdr c1) ;; 是一个atom


(define c2 (list 1 2))
c2
(car c2)
(cdr c2)

;; 进一步探究(cdr c2)
(car (cdr c2))
(cdr (cdr c2))
;(car (cdr (cdr c2))) 求不出了. 因(cdr (dcr c2))元素是空.

;; ill-form list
(define i1 (cons 1 (cons 2 3)))
i1

;; tree
(define t1 (cons (list 1 2) (list 3 4)))
t1
