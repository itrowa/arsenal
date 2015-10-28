
; cs61A习题也有这个题
(define f
	(lambda n
	(
		(cond
			((< n 3) n)
			(else (+ f(n - 1)
					 (* 2 (f(n - 2)))
					 (* 3 (f(n - 3)))
				))))))

(f 3)

(define f_iter
	; python版本的其实更好理解些。因为不用递归调用函数。
	(lambda a, b, c, cnt, n
	(
		; 例如，现在cnt是 4， 那么a就是f3, b就是f2, c就是f1
		(cond
			((= n 3) n)
			((= n 2) n)
			((= n 1) n)
			((= cnt n) a)
			(else
				(f_iter a b c (+ 1 cnt) max)
				)))))