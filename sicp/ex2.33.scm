(load "ch2_interface_after.scm")

(define (map-1 p sequence)
  (accumulate (lambda (x y) (cons (p x) y)) '() sequence))

(define (append-1 seq1 seq2)
  (accumulate cons  seq2 seq1))

(define (length-1 sequence)
  (accumulate
    (lambda(x y)
      (+ 1 y))
    0
    sequence))

;; test
(map-1 (lambda (x) (* x x)) (list 1 2 3))

(append-1 (list 1 2 3) (list 4 5 6))

(length-1 (list 1 2 3 4))