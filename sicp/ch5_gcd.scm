;; SICP 5.1

;; 对GCD机器的描述
(controller
  test-b
    (test (op = ) (reg b) (const 0))
    (branch (label gcd-done))
    (assign t (op rem) (reg a) (reg b))
    (assign a (reg b))
    (assign b (reg t))
    (goto (label test-b))
  gcd-done)