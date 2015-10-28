;; see this file
(load "ch2_sets-unorderd.scm")

;; test
(union-set s1 s2)
(union-set s1 s3)
(union-set '() s2)
(union-set  s2 '())
(union-set '() '())