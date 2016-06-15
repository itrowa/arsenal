#lang planet neil/sicp

;; plot:
;; 1. env operation
;; 2. eval function
;; 3. test and eval for each special form and combination eval
;; 4. REPL
;; 5: test

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; environment
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(define the-empty-environment '())


(define (first-frame env) (car env))
(define (enclosing-environment env)(cdr env))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; env operation
;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (extend-environment vars vals base-env)
  (if (= (length vars) (length vals))
      (cons (make-frame vars vals) base-env)
      (if (< (length vars) (length vals))
          (error "Too many args supplied" vars vals)
          (error "Too few args supplied" vars vals))))


(define (lookup-variable-value var env)
  (define(env-loop env)
    (define (scan vars vals)
      (cond ((null? vars)         (env-loop (enclosing-environment env)))
            ((eq? var (car vars)) (car vals))
            (else                 (scan (cdr vars) (cdr vals)))))
    (if (eq? env the-empty-environment)
        (error "Unbound variable" var)
        (let ((frame (first-frame env)))
          (scan (frame-variables frame)
                (frame-values frame)))))
  (env-loop env))


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


(define (define-variable! var val env)
  (let ((frame (first-frame env)))
    (define (scan vars vals)
      (cond ((null? vars)         (add-binding-to-frame! var val frame))
            ((eq? var (car vars)) (set-car! vals val))
            (else                 (scan (cdr vars) (cdr vals)))))
    (scan (frame-variables frame)
          (frame-values frame))))
    

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; frame operation
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (make-frame variables values)
  (cons variables values))

(define (frame-variables frame) (car frame))

(define (frame-values frame) (cdr frame))

(define (add-binding-to-frame! var val frame)
  (set-car! frame (cons var (car frame)))
  (set-cdr! frame (cons val (cdr frame))))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; eval
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
        ((begin? exp)                (eval-sequence (begin-actions exp) env))
        ((cond? exp)                 (ewal (cond->if exp) env))
        ((application? exp)          (epply (ewal (operator exp) env)
                                            (list-of-values (operands exp) env)))
        (else                        (error "Unknown type -- EWAL" exp))))



;;;;;;;;;;;;;;;;;;;;;;;;;;
;; self-eval test and eval
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (self-evaluating? exp)
  (cond ((number? exp) #t)
        ((string? exp) #t)
        (else #f)))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; variable test an eval
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (variable? exp) (symbol? exp))
;; (lookup-variable-value exp env) see below

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; quote test and eval
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (quoted? exp)
  (tagged-list? exp 'quote))

(define (text-of-quotation exp) (cadr exp))

(define (tagged-list? exp tag)
  (if (pair? exp)
      (eq? (car exp) tag)
      #f))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; assignment test and eval
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (assignment? exp)
  (tagged-list? exp 'set!))

(define (assignment-variable exp) (cadr exp))
(define (assignment-value exp) (caddr exp))

(define (eval-assignment exp env)
  (set-variable-value! (assignment-variable exp)
                       (ewal (assignment-value exp) env)
                       env)
  'ok) 

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; definition test and eval
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (definition? exp)
  (tagged-list? exp 'define))

(define (definition-variable exp)
  (if (symbol? (cadr exp))    
      (cadr exp)            
      (caadr exp)))         

(define (definition-value exp)
  (if (symbol? (cadr exp))
      (caddr exp)
      (make-lambda (cdadr exp)    ;;formal parameters
                   (cddr exp))))  ;;body

(define (make-lambda parameters body)
  (cons 'lambda (cons parameters body)))

(define (eval-definition exp env)
  (define-variable! (definition-variable exp)
                    (ewal (definition-value exp) env)
                    env)
  'ok)

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; lambda test and eval
;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (lambda? exp) (tagged-list? exp 'lambda))

(define (lambda-parameters exp) (cadr exp))

(define (lambda-body exp) (caddr exp))

(define (make-procedure parameters body env)
  (list 'procedure parameters body env))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; if test and eval
;;;;;;;;;;;;;;;;;;;;;;;;;;

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
;; begin test and eval
;;;;;;;;;;;;;;;;;;;;;;;;;;

(define (begin? exp) (tagged-list? exp 'begin))
(define (begin-actions exp) (cdr exp))
(define (last-exp? seq) (null? (cdr seq)))
(define (first-exp seq) (car seq))
(define (rest-exps seq) (cdr seq))


(define (eval-sequence exps env)
  (cond ((last-exp? exps) (ewal (first-exp exps) env))
        (else (ewal (first-exp exps) env)
              (eval-sequence (rest-exps exps) env))))

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; application test and eval
;;;;;;;;;;;;;;;;;;;;;;;;;;


(define (application? exp) (pair? exp)) 


(define (operator exp) (car exp))
(define (operands exp) (cdr exp))


(define (no-operands? ops) (null? ops))
(define (first-operand ops) (car ops))
(define (rest-operands ops) (cdr ops))


(define (list-of-values exps env)
  (if (no-operands? exps)
      '()
      (cons (ewal (first-operand exps) env)
            (list-of-values (rest-operands exps) env))))

(define (epply procedure arguments)
  (cond ((primitive-procedure? procedure) (apply-primitive-procedure procedure arguments))
        ((compound-procedure? procedure)  (ewal (procedure-body procedure)        ;; (*)
                                                         (extend-environment (procedure-parameters procedure)
                                                                             arguments
                                                                             (procedure-environment procedure))))
        (else                             (error "Unkown procedure type -- EPPLY" procedure))))


(define (primitive-procedure? proc)
  (tagged-list? proc 'primitive))

(define (primitive-implementation proc) (cadr proc))


(define (compound-procedure? p) (tagged-list? p 'procedure))


(define (procedure-parameters p) (cadr p))
(define (procedure-body p) (caddr p))
(define (procedure-environment p) (cadddr p))

(define (apply-primitive-procedure proc args)
  (apply-in-underlying-scheme (primitive-implementation proc) args))

(define apply-in-underlying-scheme apply)

;;;;;;;;;;;;;;;;;;;;;;;;;;
;; cond test and eval
;;;;;;;;;;;;;;;;;;;;;;;;;;

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

(define (make-if predicate consequent alternative)
  (list 'if predicate consequent alternative))

(define (sequence->exp seq)
  (cond ((null? seq) seq)
        ((last-exp? seq) (first-exp seq))
        (else (make-begin seq))))

(define (make-begin seq) (cons 'begin seq))

;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; env setup
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
(define (setup-environment)
  (let ((initial-env
         (extend-environment (primitive-procedure-names)
                             (primitive-procedure-objects)
                             the-empty-environment)))
    (define-variable! '#t #t initial-env)
    (define-variable! '#f #f initial-env)
    initial-env))

(define primitive-procedures
  (list(list 'car car)
       (list 'cdr cdr)
       (list 'null? null?)
       (list 'cons cons)
       (list '+ +)
       (list '- -)
       (list '* *)
       (list '/ /)
       (list '= =)))

(define (true? x)
  (not (eq? x false)))

(define (false? x)
  (eq? x false))

(define (primitive-procedure-names)
  (map car primitive-procedures))

(define (primitive-procedure-objects)
  (map (lambda (proc) (list 'primitive (cadr proc)))
       primitive-procedures))


(define the-global-environment (setup-environment))

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

(define (user-print object)
  (if (compound-procedure? object)
    (display (list 'compound-procedure
                   (procedure-parameters object)
                   (procedure-body object)
                   '<procedure-env>))))



;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;;; test
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(define env0 the-global-environment)

(ewal '(define (p1 x) (+ x 1)) env0 )

(ewal '(p1 4) env0)

(ewal '(define (append x y)
         (if (null? x)
             y
             (cons (car x)
                   (append (cdr x) y)))) env0)

(ewal '(define (factorial n)
         (if (= 1 n)
             1
             (* n (factorial (- n 1))))) env0)

(ewal '(factorial 5) env0)
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; init main loop
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;;(driver-loop)
;; this is commented since I found it run incorrectly
