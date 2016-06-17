;(load "intp2.scm")

;基本的test
;(eval-1 '+ env1)
;(eval-1 '4 env1)
;(eval-1 '(+ 1 2) env1)

;(eval-1 '(+ a 1) env1)

(define x '(CLOSURE ((x) (+ x y)) env0) )
(cdadr x)
(cadadr x)
(caadr x)
(caddr x)


;;;;;;;;;;;;;;;;;
; env

; 把形参和实参作为一条记录追加到环境里去.
(define (bind vars vals env)
  (cons (pair-up vars vals)
        env))

; help
(define (pair-up vars vals)
  (cond
    ((eq? vars '())
      (cond ((eq? vals '()) '())
            (else "Too much args")))
    ((eq? vals '()) ("Too few args"))
    (else
      (cons (cons (car vars)
                  (car vals))
            (pair-up (cdr vars)
                     (cdr vals))))))

(define env1 '((a . 1) (b . 2) (c . 3)))
(define env0 '())

(bind '(d e f) '(4 5 6) env0)
(bind '(z) '(9) env0)


;;;;;;;;;;;;;;;;;;;;;;;;

(define (primitive-proc? proc)
  (primitive-proc?-core proc 
                        primitive-proc-list))

(define (primitive-proc?-core proc plist)
  (cond ((null? plist) #f)
        ((eq? (car plist) proc) #t)
        (else (primitive-proc?-core proc (cdr plist)))))

(define (compound-proc? proc)
  (if (eq? (car proc) 'CLOSURE)
      #t
      #f))

(define primitive-proc-list
  '(+ - * / car cdr cons list))

(primitive-proc? 'car)

;;;;;;;;;;;;;;;;;;;;;;;

(define n1 'name)
(define n2 (quote name))

(define n3 '(name))
n3  ; (name)

; 对于人类阅读的(name)而言, 对机器而言是一个列表.
(car n3)
; name
(cdr n3)
; ()
