(define input-prompt ";;; M-Eval input:")
(define output-prompt ";;; M-Eval value:")

(define (driver-loop)
  (prompt-for-input input-prompt)
  (let ((input (read)))
    (let ((output input))
      (announce-output output-prompt)
      (user-print output)))
  (driver-loop))

(define (prompt-for-input string)
  (newline)(newline)(display string)(newline))

(define (announce-output string)
  (newline)(display string)(newline))

(define (user-print object)
  (display object))

;; read函数是做什么的..