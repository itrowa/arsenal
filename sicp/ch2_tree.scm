;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; binary tree
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

;; constructor
(define (make-tree entry left right)
  (list entry left right))

;; selector
(define (entry tree) (car tree))

(define (left-branch tree) (cadr tree))

(define (right-branch tree) (caddr tree))

;; other behaviors

;; is x a member of set?
(define (element-of-set? x set)
  (cond ((null? set) false)
        ((= x (entry set)) #t)
        ((< x (entry set)) (element-of-set? x (left-branch set)))
        ((> x (entry set)) (element-of-set? x (right-branch set)))))

;; return a tree with x joined in that tree.
(define (adjoin-set x set)
  (cond ((null? set) (make-tree x '() '()))
        ((= x (entry set)) set)
        ((< x (entry set)) (make-tree (entry set)
                                      (adjoin x (left-branch set))
                                      (right-branch set)))
        ((> x (entry set)) (make-tree (entry set)
                                      (left-branch set)
                                      (right-branch set)))))
                           
; 这个不符合规定! leaf也是tree,left branch 和right branch必须是'()
;(define t1 (make-tree 7
;                      (make-tree 3
;                                 1
;                                 5)
;                      (make-tree 9
;                                 '()
;                                 11)))

;; test
(define t (make-tree 7
                      (make-tree 3
                                 (make-tree 1 '() '())
                                 (make-tree 5 '() '()))
                      (make-tree 9
                                 '()
                                 (make-tree 11 '() '()))))

;(entry t)
;(left-branch t)
;(right-branch t)
                      