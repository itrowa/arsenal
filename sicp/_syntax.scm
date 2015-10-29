; define
(define (square x) (* x x))
(define square (lambda x (* x x)))

; cond的表达
(cond
	(predicate1 exp1)
	(predicate2 exp2)
	;...
	(else exp_else)
	)

(define (abs x)
    (if (< x 0) (- x)     ;<precicate> <consequence>
        x)                ;<alt consequence>, 相当于else
