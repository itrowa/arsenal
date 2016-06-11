#lang racket
(define f1
  (lambda (callback)
    (callback)))

(define do-it
  (lambda () "just do it!"))

(f1 do-it)
;; "just do it!"