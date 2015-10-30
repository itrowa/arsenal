(load "intp2.scm")

;基本的test
(eval-1 '+ env1)
(eval-1 '4 env1)
(eval-1 '(+ 1 2) env1)

(eval-1 '(+ a 1) env1)