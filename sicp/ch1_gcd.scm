;; gcd是scheme的基本过程.
(define (gcd/demo a b)
  (if (= b 0)
      a
      (gcd b (remainder a b))))
