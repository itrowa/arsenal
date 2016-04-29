;; plot:
;; 1. 环境的表达和操作
;; 2. 求值器(eval)函数
;; 3. 对每个类型的判断, 和对每个类型的处理.
;; 4. REPL
;; 5: 测试代码

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; environment
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; env 就是一系列框架的list. 而每个框架是这样的结构:
;; ( (var1 var2 var3) (val1 val2 val3))
;; 变量名var和对于的值val分别在框架的car和cadr中.

;; 定义个空环境
(define the-empty-environment '())

;; first-frame指的就是环境中的第一个frame, 而所谓的"外围环境"就是env的cdr.
(define (first-frame env) (car env))
(define (enclosing-environment env)(cdr env))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 关于env的操作
;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 给环境添加一个新框架, 以扩充这个环境.
(define (extend-environment vars vals base-env)
  (if (= (length vars) (length vals))
      (cons (make-frame vars vals) base-env)
      (if (< (length vars) (length vals))
          (error "Too many args supplied" vars vals)
          (error "Too few args supplied" vars vals))))

;; 在环境中查找一个变量:
(define (lookup-variable-value var env)
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
;;(define (lookup-variable-value var env)
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

;; 定义一个变量 @? 这个在哪用上了?
(define (define-variable! var val env)
  (let ((frame (first-frame env)))
    (define (scan vars vals)
      (cond ((null? vars)         (add-binding-to-frame! var val frame))
            ((eq? var (car vars)) (setcar! vals val))
            (else                 (scan (cdr vars) (cdr vals)))))
    (scan (frame-variables frame)
          (frame-values frame))))
    

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 关于frame的操作
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (make-frame variables values)
  (cons variables values))

(define (frame-variables frame) (car frame))

(define (frame-values frame) (cdr frame))

(define (add-binding-to-frame! var val frame)
  (set-car! frame (cons var (car frame)))
  (set-cdr! frame (cons val (cdr frame))))
;;@note: 检查set-car!的定义!


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; 求值器
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (ewal exp env)
  (cond ((self-evaluating? exp)      exp)
        ((variable? exp)             (lookup-variable-value exp env))
        ((quoted? exp)               (text-of-quotation exp))
        ((assignment? exp)           (eval-assignment exp env))
        ((if? exp)                   (eval-if exp env))
        ((lambda? exp)               (make-procedure (lambda-parameters exp)
                                                     (lambda-body exp)
                                                     env))
        ((begin? exp)                (eval-sequence (begin-actions exp) env))
        ((cond? exp)                 (ewal (cond->if exp) env))
        ((application? exp)          (apply (eval (operator exp) env)
                                            (list-of-values (operands exp) env)))
        (else                        (error "Unknown type -- EVAL" exp))))



;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 自求值式子的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (self-evaluating? exp)
  (cond ((number? exp) #t)
        ((string? exp) #t)
        (else #f)))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 变量(name)的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (variable? exp) (symbol? exp))
;; (lookup-variable-value exp env) 见后面

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; quote式子的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (quoted? exp)
  (tagged-list? exp 'quote))

(define (text-of-quotation exp) (cadr exp))

(define (tagged-list? exp tag)
  (if (pair? exp)
      (eq? (car exp) tag)
      (#f)))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 赋值式子的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (assignment? exp)
  (tagged-list? exp 'set!))

(define (assignment-variable exp) (cadr exp))
(define (assignment-value exp) (caddr exp))

;; 对赋值式子的求值方式如下.
(define (eval-assignment exp env)
  (set-variable-value! (assignment-variable exp)
                       (ewal (assignment-value exp) env)
                       env)
  'ok) ; 求值完成后返回ok.

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 定义式子的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (definition? exp)
  (tagged-list? exp 'define))

(define (definition-variable exp)
  (if (symbol? (cadr exp))    
      (cadr exp)            ; 表达式是(define <name> <value>)的形式, 因此取出cadr即可
      (caadr exp)))         ; 表达式是(define (<var><parameter1>...<parametern>) <body>)的形式. 因此取出caadr

(define (definition-value exp)
  (if (symbol? (cadr exp))
      (caddr exp)
      (make-lambda (cdadr exp)    ;;formal parameters
                   (cddr exp))))  ;;body

(define (make-lambda parameters body)
  (cons 'lambda (cons parameters body)))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; lambda式子的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 判断是不是lambda式
(define (lambda? exp)
  (tagged-list? exp 'lambda))

(define (lambda-parameters exp)
  (cadr exp))

(define (lambda-body exp)
  (caddr exp))

(define (make-procedure parameters body env)
  (list 'procedure parameters body env))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; if式子的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 判断是不是if式
(define (if? exp) (tagged-list? exp 'if))

(define (if-predicate exp) (cadr exp))

(define (if-consequent exp) (caddr exp))

(define (if-alternative exp)
  (if (not (null? (cdddr exp)))
      (cadddr exp)
      'false))

(define (eval-if exp env)
  (if (true? (ewal (if-predicate exp) env))
      (ewal (if-consequent exp) env)
      (ewal (if-alternative exp) env)))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; begin式的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
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

;; begin式子的处理
(define (eval-sequence exps env)
  (cond ((last-exp? exps) (ewal (first-exp exps) env))
        (else (ewal (first-exp exps) env)
              (eval-sequence (rest-exps exps) env))))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; application式的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 判断一个表达式是不是application(组合式)
(define (application? exp) (pair? exp))

(define (operator exp) (car exp))
(define (operands exp) (cdr exp))
(define (no-operands? ops) (null? ops))
(define (first-operand ops) (car ops))
(define (rest-operands ops) (car ops))

;; 对procedure式子的处理.
(define (epply procedure arguments)
  (cond ((primitive-procedure? procedure) (apply-primitive-procedure procedure arguments))
        ((compound-procedure? procedure)  (eval-sequence (procedure-body procedure)
                                                         (extend-environment (procedure-parameters procedure)
                                                                             arguments
                                                                             (procedure-environment procedure))))
        (else                             (error "Unkown procedure type -- APPLY" procedure))))

;; 判断是不是基本过程
(define (primitive-procedure? proc)
  (tagged-list? proc 'primitive))

(define (primitive-implementation proc) (cadr proc))

;; 判断是否是复合过程
(define (compound-procedure? p) (tagged-list? p 'procedure))

(define (procedure-parameters p) (cadr p))

(define (procedure-body p) (caddr p))

(define (procedure-environment p) (cadddr p))

(define (apply-primitive-procedure proc args)
  (apply-in-underlying-scheme (primitive-implementation proc) args))



;;;;;;;;;;;;;;;;;;;;;;;;;;
;; cond式子的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
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



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; env setup
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
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

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; test
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(quoted? '(quote (1 2 3)))
; #t
(text-of-quotation  '(quote (1 2 3)))
; (1 2 3)