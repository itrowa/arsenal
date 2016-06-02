;; 功能: 构造一个串行化组.
;; 给定一个过程p, 串行化组将返回一个过程, 这个过程会把互斥元
;; 拾取走(设置互斥元的值为#t, 表示已被拾取); 然后运行p, 最后释
;; 放这个互斥元(设置互斥元的值为#f, 表示没被拾取).
;; 而后运行p, 最后又释放互斥元.(保证了p在运行全程中都不被抢断)

;; eg: (make-serializer (lambda()(+ 2 2)) )
(define (make-serializer)
  (let ((mutex (make-mutex)))
    (lambda (p)
      (define (serialized-p . args)
        (mutex 'acquire)
        (let ((val (apply p args)))
          (mutex 'release)
          val))
      serialized-p)))

;; 互斥元的构造函数
;; cell是只有一个元素的list. 若cell为#f, 表示这个互斥元没被获取.
;;
(define (make-mutex)  
  (let ((cell (list #f)))    
    (define (the-mutex m)
      (cond ((eq? m 'acquire)
             (if (test-and-set! cell)
                 (the-mutex 'acquire)))      ; 若cell为#t, 则反复尝试直到cell为#f
            ((eq? m 'release) (clear! cell))))
    the-mutex))

;; help func
(define (clear! cell)
  (set-car! cell #f))

;; help func
;; 检查并设置cell的值。如果cell是假，在返回假之前还要把cell设置为真。
;; 当cell为真, 返回#t, 意味着不能被获取.
;; 和cell为假, 返回#f, 在此之前还要把cell设置为#t
(define (test-and-set! cell)
  (if (car cell)
      #t
      (begin (set-car! cell #t)
             #f)))
;; cavet! 可能需要设置no-interrupts! (P218)


;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; 改进make-account的例子
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;


(define (make-account balance)
  
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))
  
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  
  (let ((protected (make-serializer)))
    
    (define (dispatch m)
      (cond ((eq? m 'withdraw) (protected withdraw))
            ((eq? m 'deposit) (protected deposit))
            ((eq? m 'balance) balance)
            (else (error "Unknown request -- MAKE-ACCOUNT" m))))
    dispatch))