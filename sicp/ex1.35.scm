;; 通过计算f(x)=1+1/x的不动点求得黄金分割率φ.(黄金分割率φ正好是f(x)=1+1/x，证明见onenote笔记)
(load "ch1_fixed-point.scm")

(fixed-point (lambda(x) (+ 1 (/ 1 x))) 1)
