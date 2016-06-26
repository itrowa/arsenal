;; 本代码无法正常运行. 应该把测试代码复制到解释器程序的底部运行它.

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



;; 环境模型测试. 环境模式是一系列框架. 那么这些嵌套的框架是如何指定前一个框架的指针的呢?
(ewal '(define (make-withdraw balance)
  (lambda (amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))) env0)

;(ewal '(define W1 (make-withdraw 100)) env0)
;(ewal '(define W2 (make-withdraw 200)) env0)

;(make-withdraw 100)

;(ewal '(make-withdraw 100) env0)


;(ewal '(W1 50) env0)
;(ewal '(W2 50) env0)



;; 环境模型测试
(define env0 the-global-environment)

(define (proc1 balance)
  (lambda (x) (+ balance x)))

((proc1 1) 2)
;; 先创建E1框架 balance被绑定到2,  再创建E2, x被绑定到1. 框架: E2 -> E1 -> global-env
;; 可以正确求值, 但是通过引用the-global-env却还是那个没有扩展过的环境. 因为那个扩展过后的环境知只是被返回, 并没有赋值给the-global-env.