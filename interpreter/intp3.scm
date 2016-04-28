;; 判断是不是lambda表达式

;; 判断是不是if表达式

;; 判断是不是begin表达式
(define (begin? exp) (tagged-list? exp 'begin))
(define (begin-actions exp) (cdr exp))
(define (last-exp? seq) (null? (cdr seq)))
(define (first-exp seq) (car seq))
(define (rest-exps seq) (cdr seq))

;; 把一个序列变换为一个表达式
(define (sequence->exp seq)
  (cond ((null? seq) seq)
        ((last-exp? seq) (first-exp seq))
        (else (make-begin seq))))

(define (make-begin seq) (cons 'begin seq))

;; 判断一个表达式是不是application(组合式)
(define (application? exp) (pair? exp))

(define (operator exp) (car exp))
(define (operands exp) (cdr exp))
(define (no-operands? ops) (null? ops))
(define (first-operand ops) (car ops))
(define (rest-operands ops) (car ops))

;; 判断是不是cond表达式
;; exp:
;; (cond (<p1> <e1>)
;;       (<p2> <e2>)
;;         ..
;;       (<pn> <en>)
;;       (else <e-else>))
;; note: 搞清楚这里面exp, clause都代表什么.
(define (cond? exp) (tagged-list? exp 'cond))

(define (cond-clauses exp) (cdr exp))
(define (cond-else-clause? clause)
  (eq? (cond-predicate clause) 'else))

(define (cond-predicate clause) (car clause))
(define (cond-actions clause) (cdr clause))

(define (cond->if exp)
  (expand-clauses (cond-clauses exp)))

(define (expand-clauses clauses)
  (if (null? clauses)
    'false
    (let ((first (car clauses))
          (rest (cdr clauses)))
      (if (cond-else-clause? first)
        (if (null? rest)
          (sequence->exp (cond-actions first))
          (error "ELSE clause isn't last -- COND->IF" clauses))
        (make-if (cond-predicate first)
                 (sequence->exp(cond-actions first))
                 (expand-clauses rest))))))

;; 谓词检测
(define (true? x)
  (not (eq? x false)))

(define (false? x)
  (eq? x false))

;; 判断是不是基本过程
(define (primitive-procedure? proc)
  (tagged-list? proc 'primitive))




;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; environment
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; env 就是一系列框架的list. 而每个框架是这样的结构:
;; ( (var1 var2 var3) (val1 val2 val3))
;; 变量名var和对于的值val分别在框架的car和cadr中.

;; 定义个空环境
(define the-empty-environment '())

;; first-frame指的就是环境中的第一个frame, 而所谓的"外围环境"就是env的cdr.
(define (first-frame env) (car env))
(define (enclosing-environment env)(cdr env))

;;;;;;;;;;;;;;;;;;;;;;
;; 关于env的操作

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

;; 解释:
;; 不妨看成这样:
;; 
;;(define (lookup-variables-value var env)
;;    ...
;;    (env-loop env))
;;
;; 函数的body其实就只有一句(env-loop env).
;; 
;; 那下一步再看env-loop的定义是啥.
;;  (define (env-loop env)
;;       ...
;;      (if (eq? env the-empty-environment)
;;          (error "Unbound variable" var)
;;          (let ((frame (first-frame env)))
;;            (scan (frame-variables frame)
;;                  (frame-values frame)))))

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
;;@note: 检查set-car!的定义!
