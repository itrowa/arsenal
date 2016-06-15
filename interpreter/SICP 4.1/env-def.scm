;; sicp教材第四章环境部分. 单独拿出来, 做研究和测试.
;; all tests passed!

;; 定义个空环境
(define the-empty-environment '())

;; first-frame指的就是环境中的第一个frame, 而所谓的"外围环境"就是env的cdr.
(define (first-frame env) (car env))
(define (enclosing-environment env)(cdr env))

;; 给环境添加一个新框架, 以扩充这个环境.
(define (extend-environment vars vals base-env)
  (if (= (length vars) (length vals))
      (cons (make-frame vars vals) base-env)
      (if (< (length vars) (length vals))
          (error "Too many args supplied" vars vals)
          (error "Too few args supplied" vars vals))))

;; 在环境中查找一个变量:
(define (lookup-variables-value var env)
  (define(env-loop env)
    (define (scan vars vals)
      (cond ((null? vars)         (env-loop (enclosing-environment env)))
            ((eq? var (car vars)) (car vals))
            (else                 (scan (cdr vars) (cdr vals)))))
    ;; 前面都是局部定义的函数. 这里才是函数body.
    (if (eq? env the-empty-environment)
        (error "Unbound variable" var)
        (let ((frame (first-frame env)))
          (scan (frame-variables frame)
                (frame-values frame)))))
  ;; 调用刚才定义的函数.
  (env-loop env))

;; 改变某个变量的值.
(define (set-variable-value! var val env)
  (define (env-loop env)
    (define (scan vars vals)
      (cond ((null? vars)         (env-loop (enclosing-environment env)))
            ((eq? var (car vars)) (set-car! vals val))
            (else                 (scan (cdr vars) (cdr vals)))))
    (if (eq? env the-empty-environment)
       (error "Unbound variable -- SET!" var)
       (let ((frame (first-frame env)))
         (scan (frame-variables frame)
               (frame-values frame)))))
  (env-loop env))

;; 定义一个变量
(define (define-variable! var val env)
  (let ((frame (first-frame env)))
    (define (scan vars vals)
      (cond ((null? vars)         (add-binding-to-frame! var val frame))
            ((eq? var (car vars)) (setcar! vals val))
            (else                 (scan (cdr vars) (cdr vals)))))
    (scan (frame-variables frame)
          (frame-values frame))))
    

;;;;;;;;;;;;;;;;;;;;;;
;; 关于frame的操作
(define (make-frame variables values)
  (cons variables values))

(define (frame-variables frame) (car frame))

(define (frame-values frame) (cdr frame))

(define (add-binding-to-frame! var val frame)
  (set-car! frame (cons var (car frame)))
  (set-cdr! frame (cons val (cdr frame))))
;;@note: 检查set-car!的定义


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; env setup
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 返回一个初始的环境. 包含了几本过程的定义, 初始的基本变量.
(define (setup-environment)
  (let ((initial-env
         (extend-environment (primitive-procedure-names)
                             (primitive-procedure-objects)
                             the-empty-environment)))
    (define-variable! 'true #t initial-env)
    (define-variable! 'false #f initial-env)
    initial-env))

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

;; 最后运行setup-environment, 得到解释器所用的环境.
(define the-global-environment (setup-environment))
;; @note: 这个只能放在最后. 因为(setup-environment)是一句函数调用.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;test
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(define test-env '(((a b c) 1 2 3 )
                   ((x y z) 4 5 6 )))

(define frame1 (make-frame '(aa bb) '(11 22)))
(frame-variables frame1)
(frame-values frame1)

(define-variable! 'd 4 test-env)
(set-variable-value! 'd 5 test-env)
(set-variable-value! 'z 7 test-env)
(extend-environment '(alpha beta charlie)  '(100 101 102) test-env)