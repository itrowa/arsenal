;; P214

;; 交换两个银行账户的程序.
(define (exchange account1 account2)
  (let ((difference (- (account1 'balance)
                       (account2 'balance))))
    ((account1 'withdraw) difference)
    ((account2 'deposit) difference)))


;; 改进版的函数, 用于创建银行账户, 改进之处在于每个创建的银行账户都支持在其内部创建一个串行化组.
(define (make-account-and-serializer balance)
  (define (withdraw amount)
    (if (>= balance amount)
        (begin (set! balance (- balance amount))
               balance)
        "Insufficient funds"))
  (define (deposit amount)
    (set! balance (+ balance amount))
    balance)
  (let ((balance-serializer (make-serializer)))
    (define (dispatch m)
      (cond ((eq? m 'withdraw) withdraw)
            ((eq? m 'deposit) deposit)
            ((eq? m 'balance) balance)
            ((eq? m 'serializer) balance-serializer)
            (else (error "Unknown request -- MAKE-ACCOUNT" m))))
    dispatch))

;; 作为一个例子, 说明如何从这样的账户中取款. 取款的请求所代表的过程, 必须加入到目标账户串行化组中, 以保证并发的正确.
(define (deposit account amount)
  (let ((s (account 'serializer))
        (d (account 'deposit)))
    ((s d) amount)))

(define (serialized-exchange account1 account2)
  (let ((serialized1 (account1 'serializer))
        (serialized2 (account2 'serializer)))
    ((serializer1 (serializer2 exchange)) account1 account2))