(define (setup-environment)
  (let ((initial-env
         (cons (primitive-procedure-names)
                             (primitive-procedure-objects)
                             the-empty-environment)))
    (define-variable! 'true #t initial-env)
    (define-variable! 'false #f initial-env)
    initial-env))
;; @note: 从理解的角度来说, 这个函数的定义应该放在最前面. 但是因为函数内部, 最后一句initial-env, 调用了(primitive-procedure-names)这样的过程,
;; 因此必须把它调用的那些过程的定于放到前面?.

;; 全局环境的定义
(define the-global-environment (setup-environment))

;; help:定义一个基本过程的name-object查找表.
(define primitive-procedures
  '((car car)
    (cdr cdr)
    (null? null?)))

;; help:从primitive-procedures取出names做成列表.
(define (primitive-procedure-names)
  (map car
       primitive-procedures))
;; help:从primitive-procedures取出objects做成列表.
(define (primitive-procedure-objects)
  (map (lambda (proc) (list 'primitive (cadr proc)))
       primitive-procedures))
