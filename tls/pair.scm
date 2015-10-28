;----------------------------------------------
; 开始研究pair了
;
;a pair is a list with only 2 atoms.
;like(pear pear), (3 7),((2) (pair)), (full (house))
(define a-pair?
  (lambda (x)
    (cond
      ((atom? x) #f)
      ((null? x) #f)
      ((null? (cdr x)) #f)
      ((null? (cdr (cdr x))) #t)
      (else #f))))

; constructor: 用两个atom build一个pair
(define build
  (lambda (s1 s2)
    (cond
      (else (cons s1
                  (cons s2 (quote())))))))     
; selector
(define first
  (lambda (p)
    (cond
      (else (car p)))))

(define second
  (lambda (p)
    (cond
      (else (car (cdr p))))))
; 取出第三个元素, 又叫做cadr
(define third
  (lambda (l)
    (car (cdr (cdr l)))))

