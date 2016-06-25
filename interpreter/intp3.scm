;; #lang planet neil/sicp

;; 这是SICP 4.1~4.2所实现的解释器. 可以在DrRacket中以R5RS模式运行.

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

;; 定义一个变量
(define (define-variable! var val env)
  (let ((frame (first-frame env)))
    (define (scan vars vals)
      (cond ((null? vars)         (add-binding-to-frame! var val frame))
            ((eq? var (car vars)) (set-car! vals val))
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
        ((definition? exp)           (eval-definition exp env))
        ((if? exp)                   (eval-if exp env))
        ((lambda? exp)               (make-procedure (lambda-parameters exp)
                                                     (lambda-body exp)
                                                     env))
        ((begin? exp)                (eval-sequence (exp-seq-of exp) env))
        ((cond? exp)                 (ewal (cond->if exp) env))
        ((application? exp)          (epply (ewal (operator exp) env)
                                            (list-of-values (operands exp) env)))
        (else                        (error "Unknown type -- EWAL" exp))))



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
      #f))

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

;; 处理
(define (eval-definition exp env)
  (define-variable! (definition-variable exp)
                    (ewal (definition-value exp) env)
                    env)
  'ok)
;; 往环境中添加一个新绑定, 然后返回'ok

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; lambda式子的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 判断是不是lambda式
(define (lambda? exp) (tagged-list? exp 'lambda))

(define (lambda-parameters exp) (cadr exp))

(define (lambda-body exp) (cddr exp))

(define (make-procedure parameters body env)
  (list 'procedure parameters body env))    ;; 做成闭包

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; if式子的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 判断是不是if式
(define (if? exp) (tagged-list? exp 'if))

(define (if-predicate exp) (cadr exp))
(define (if-consequent exp) (caddr exp))
(define (if-alternative exp)
  (if (not (null? (cadddr exp)))
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
(define (exp-seq-of exp) (cdr exp))
(define (only-one-exp? seq) (null? (cdr seq)))
(define (first-exp seq) (car seq))
(define (rest-exps seq) (cdr seq))

;; begin式子的处理
(define (eval-sequence exps env)
  (cond ((only-one-exp? exps) (ewal (first-exp exps) env))
        (else (ewal (first-exp exps) env)
              (eval-sequence (rest-exps exps) env))))
; exps: 一系列表达式的list.


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

;; 表达式中的cond-clause和else clause.

(define (cond-clauses exp) (cdr exp))

(define (cond-else-clause? clause)
  (eq? (cond-predicate clause) 'else))

;; clause的predicate部分和actions部分.

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

(define (make-if predicate consequent alternative)
  (list 'if predicate consequent alternative))

;; 把一个序列变换为一个表达式
(define (sequence->exp seq)
  (cond ((null? seq) seq)
        ((only-one-exp? seq) (first-exp seq))
        (else (make-begin seq))))

(define (make-begin seq) (cons 'begin seq))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; application式(组合式, 或call-expression)的判断和处理
;;;;;;;;;;;;;;;;;;;;;;;;;;

;; 判断一个表达式是不是application(组合式)
(define (application? exp) (pair? exp)) 

;; operator和operand的selector
(define (operator exp) (car exp))
(define (operands exp) (cdr exp))

;; 关于operands的辅助过程
(define (no-operands? ops) (null? ops))
(define (first-operand ops) (car ops))
(define (rest-operands ops) (cdr ops))
; ops: 待求值的形式参数的list.

;; 求值所有的参数生成实参(arguments)表.
(define (list-of-values exps env)
  (if (no-operands? exps)
      '()
      (cons (ewal (first-operand exps) env)
            (list-of-values (rest-operands exps) env))))
; exps是一系列表达式的表, 它们会被分别求值.最后返回求值结果, 也是一张表.

;; 对procedure式子的处理.
;; procedure是一个形如(procedure|primitive (paras..) (body..) #环境指针)这样的list(闭包).
;; @?@ sicp这里, compound-procedure分支下 用的是eval-sequence. 但那样我就无法正确求值复合过程了.例如(factorial 5).
(define (epply procedure arguments)
  (cond ((primitive-procedure? procedure) (apply-primitive-procedure procedure arguments))
        ((compound-procedure? procedure)  (eval-sequence (procedure-body procedure)
                                                         (extend-environment (procedure-parameters procedure)
                                                                             arguments
                                                                             (procedure-environment procedure))))
        (else                             (error "Unkown procedure type -- EPPLY" procedure))))

;; 判断是不是基本过程
(define (primitive-procedure? proc)
  (tagged-list? proc 'primitive))

(define (primitive-implementation proc) (cadr proc))

;; 判断是否是复合过程
(define (compound-procedure? p) (tagged-list? p 'procedure))

;; 取出过程的参数和body以及env
(define (procedure-parameters p) (cadr p))
(define (procedure-body p) (caddr p))
(define (procedure-environment p) (cadddr p))

(define (apply-primitive-procedure proc args)
  (apply-in-underlying-scheme (primitive-implementation proc) args))

(define apply-in-underlying-scheme apply)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; env setup
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 返回一个初始的环境. 包含了基本过程的定义, 初始的基本变量.
(define (setup-environment)
  (let ((initial-env
         (extend-environment (primitive-procedure-names)
                             (primitive-procedure-objects)
                             the-empty-environment)))
    (define-variable! 'true #t initial-env)
    (define-variable! 'false #f initial-env)
    (define-variable! 'testobj 1 initial-env)
    initial-env))
  ;; 被实现的语言中true的值是#t, false的值是#f.

;; help:定义一个基本过程的name-object查找表.
(define primitive-procedures
  (list(list 'car car)
       (list 'cdr cdr)
       (list 'null? null?)
       (list 'cons cons)
       (list '+ +)
       (list '- -)
       (list '* *)
       (list '/ /)
       (list '= =)
       (list '> >)
       (list '< <)))

;; 谓词检测
(define (true? x)
  (not (eq? x #f)))
;; 它应该返回#t 或者#f, 这是underling lang中的真假值.

(define (false? x)
  (eq? x false))

;; help:从primitive-procedures取出names做成列表.
(define (primitive-procedure-names)
  (map car primitive-procedures))
;; help:从primitive-procedures取出objects做成列表.
(define (primitive-procedure-objects)
  (map (lambda (proc) (list 'primitive (cadr proc)))
       primitive-procedures))

;; 最后运行setup-environment, 得到解释器所用的环境.
(define the-global-environment (setup-environment))
;; @note: 这个只能放在最后. 因为(setup-environment)是一句函数调用.

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; REPL
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define input-prompt "M-Eval input:")
(define output-prompt "M-Eval value:")

(define (driver-loop)
  (prompt-for-input input-prompt)
  (let ((input (read)))
    (let ((output (ewal input the-global-environment)))
      (announce-output output-prompt)
      (user-print output)))
  (driver-loop))

(define (prompt-for-input string)
  (newline)
  (newline)
  (display string)
  (newline))

(define (announce-output string)
  (newline)
  (display string)
  (newline))

;; user-print 过程并没有实现.因此driver-loop不会有正确输出.
(define (user-print object)
  (if (compound-procedure? object)
    (display (list 'compound-procedure
                   (procedure-parameters object)
                   (procedure-body object)
                   '<procedure-env>))
    (display object)))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; test and eval for each predicate.
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(define env0 the-global-environment)

;; quote?
;;;;;;;;;;;;;;
(display "is this a quoted? ")(newline)
(quoted? '(quote (1 2 3)))
; #t
(text-of-quotation  '(quote (1 2 3)))
; (1 2 3)

;; assignment?
;;;;;;;;;;;;;;
(display "is this a assignment? ")(newline)
(assignment? '(set! testobj "false"))
; #t
(eval-assignment '(set! testobj "false") the-global-environment)
; ok (环境中的testobj变量的值已变成了"false")

;; definition?
;;;;;;;;;;;;;;
(display "is this a definition? ")(newline)
(definition? '(define newobj 2))
; #t
(eval-definition '(define newobj 2) the-global-environment)
; 无返回(往环境中新增了一个变量)


;; lambda?
;;;;;;;;;;;;;;
(display "is this a lambda? ")(newline)
(lambda? '(lambda (x y) (+ y x)))

(make-procedure '(x y) '(+ y x) the-global-environment)
(ewal '(define (plus x y)(lambda (x y) (+ y x))) the-global-environment)

;; if ?
;;;;;;;;;;;;;;
(display "is this a if? ")(newline)
(if? '(if (> 5 2) true false))
; #t
(eval-if '(if (> 5 2) true false) the-global-environment)
#t

;; begin
;;;;;;;;;;;;;;
(display "is this a begin? ")
(newline)
(begin? '(begin (+ 1 1) (+ 2 2) 3))
; #t

(eval-sequence '((define bg-var-1 100) (define bg-var-2 101) 1) the-global-environment)
; 在环境中添加bg-var-1: 100 和 bg-var-2: 101的绑定, 并返回1.

;; cond  
;;;;;;;;;;;;;;
(display "is this a cond? ")(newline)
(cond? '(cond ((> 5 3) (define cond-1-var 88))
                       ((= 5 3) (define cond-2-var 89))
                       (else    (define cond-else-var 90))))
; #t
(ewal (cond->if '(cond ((> 5 3) (define cond-1-var 88))
                       ((= 5 3) (define cond-2-var 89))
                       (else    (define cond-else-var 90))))
      the-global-environment)
; 相当于(ewal (define cond-1-var 88) the-global-environment)

;; application
;;;;;;;;;;;;;;
(display "is this a app(combination, or call expression)? ")(newline)
(application? '(+ 3 5))
; #t
; 这个call exp的operator是 +, 求值结果是:(primitive #<procedure:+>)
; 这个call exp的operand是 (3 5), 求值结果就是(3 5).

(application? '((lambda (x y) (+ x y)) 1 2))
; operator部分是 (lambda (x y) (+ x y)), 求值后得到一个闭包:
; (procedure (x y)(+ x y) (当前环境的指针))
; operand部分是(1 2). 经由 list-of-value 求值后得到(1 2)

; operator求值后, 这是一个compound procerdure.
(ewal '((lambda (x y) (+ x y)) 1 2) the-global-environment)

;; 验证对参数进行求值的正确性:
(list-of-values '((+ 3 2) (- 4 1)) env0)
;; (5 3)

; 对一个compound procedure进行求值:

(ewal '((lambda (n)
          (if (= 1 n)
              1
              0))
        5)
      the-global-environment)

(ewal '(define (append x y)
         (if (null? x)
             y
             (cons (car x)
                   (append (cdr x) y)))) env0)
(ewal '(append '(a b c) '(d e f)) env0)

; 求值body部分是多个表达式的组合式.
(ewal '((lambda (x)
         (+ x 1)
         (+ x 2)) 2) env0)

(ewal '(define (factorial n)
         (if (= 1 n)
             1
             (* n (factorial (- n 1)))))
      env0)

(ewal '(factorial 5) env0)

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; init main loop
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

(driver-loop)
