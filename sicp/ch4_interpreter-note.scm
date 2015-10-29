(define (tagged-list? exp tag)
  (if (pair? exp)
      (eq? (car exp) tag)
      #f))


; > (tagged-list? '(set! a 6) 'set!)
; #t

(cond 
  ((= x 1)    'a)
  ((= x 2)    'b)  
  ((= x 3)    'c)  
  ((= x 4)    'd)
  (else    'null))

  
(if (= x 1)
    'a
    (if (= x 2)
        'b
        (if (= x 3)
            'c
            (if (= x 4)
                'd
                'null'))))