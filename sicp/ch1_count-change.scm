(define (count-change amount)
    (cc amount 5))

(define (cc amount kinds-of-coins)
    (cond 
      ;; 1
      ((= amount 0) 1)
      ;; 2
      ((or (< amount 0) (= kinds-of-coins 0)) 0)
      ;; else
      (else
        (+ (cc amount 
               (- kinds-of-coins 1))
           (cc (- amount (first-denomination kinds-of-coins))
               kinds-of-coins)))))

(define (first-denomination kinds-of-coins)
;; 这个函数根据你输入的硬币种数返回第一种硬币的币值。
;; 例如， 有三种硬币， 那么函数返回面额10.
  (cond ((= kinds-of-coins 1) 1)
        ((= kinds-of-coins 2) 5)
        ((= kinds-of-coins 3) 10)
        ((= kinds-of-coins 4) 25)
        ((= kinds-of-coins 5) 50)))

;;test:
;;(count-change 100) gets 292
;;or just
;;(cc 100 5)
;;即换100元，5中面值都用上。
