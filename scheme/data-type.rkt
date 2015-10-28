;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;
;; boolean
;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;

#t
#f

(boolean? #t)
(not #t)

;在一个需要boolean类型的上下文中,Scheme会将任何非 #f的值看成true:
(not "Hello, World!")

