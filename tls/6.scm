(define numbered?
  (lambda(aexp)
    (cond
      ;()
      ;()
      ;()
      ;()
      )))

;numbered?用来测试一个数学表达式里面是否除了+,*，和^以外都是数字
;数学表达式是指：一个数字；或者两个又+,*,^连接起来的数学表达式。
;  3
; (3 + 5)
; ( (3*2) + 5)
; (car (cdr (cdr aexp)))和(cdr (cdr aexp)) 到底有什么区别？？
(define numbered?
  (lambda(aexp)
    (cond
      ;Q1 测试aexp是数字的情况；如果exep是atom,我们就进一步问它是不是number.
      ((atom? aexp)(number? aexp))
      ; aexp看成3块，先测试中间一块是不是+ * ^，如果是的话就进一步问第一个和最后一个分别是不是数字
      ;Q2
      (eq?(car (cdr aexp))(quote +)
        (and(numbered?(car aexp))(numbered?(car (cdr (cdr aexp)))))) 
         ;后面一个为什么不是(cdr(cdr aexp))?
         ;如果是这样，那么拿(5 + 2)来说，它的(cdr(cdr aexp))是(2)，
         ;而我们需要的是数学表达式2，所以还要再套一个car
      ;Q3
      ((eq?(car (cdr aexp))(quote *))
         (and(numbered?(car aexp))(numbered?(car (cdr (cdr aexp))))))
      ;Q4
      ((eq?(car (cdr aexp))(quote ^))
       (and (numbered? (car aexp))(numbered?(car (cdr (cdr aexp)))))))))

;既然我们已经知道aexp是数学表达式了，就不要再测试它是不是数学表达式了，写得更简单一点：
(define numbered?
  (lambda (aexp)
    (cond
      ((atom? aexp)(number? aexp))
      (else
        (and(numbered?(car aexp))(numbered?(car(cdr(cdr aexp)))))))))

;(value nexp) 返回一个一个以自然书写方式表达的数学表达式的运算结果。
;如 (1+3^4) = 82
;试着写一下函数
;
; 第一
; nexp可能是:
; 一个number
; 一个由+连起来的两个数学表达式
; 第二
; 考虑用value函数自己
;
; ---------------------------------------------
; 7th commandment:
; 考虑到subpart和要处理的对象有相同的形式来递归这两种subpart:
; sublist of a list
; subexpressions of an arithmetic expression
; ---------------------------------------------

; (define value
;   (lambda (nexp)
;     (cond
;       ((atom? nexp)...)
;       ((eq?(car(cdr nexp))(quote +) ...)
;       ((eq?(car(cdr nexp))(quote +) ...)
;       ((eq?(car(cdr nexp))(quote +) ...)
;       (else ...))))
(define value
  (lambda (nexp)
    (cond
      ;如果nexp的是atom那么value函数的值就是nexp自己。
      ((atom? nexp) nexp)
      ;第二个原子是+的话
      ((eq?(car(cdr nexp)))(quote +) 
         (plus (value (car nexp)) 
         (value (car (cdr (cdr nexp))))))
      ;第二个原子是*的话
      ((eq?(car(cdr nexp)))(quote *) 
         (mtply (value (car nexp)) 
                (value (car (cdr (cdr nexp))))))
       )
      ;最后一种情况肯定就是幂了
      (else 
         (power (value (car nexp)) 
                (value (car (cdr (cdr nexp))))))))

;现在再构想新的value函数它返回以这种书写方式记录的数学表达式的运算结果：
; (+(* 3 6) (^ 8 2))
;
(define value
  (lambda (nexp)
    (cond
      ;如果nexp的是atom那么value函数的值就是nexp自己。
      ((atom? nexp) nexp)
      ;第一个原子，也就是运算符是+的话
      ((eq?(car nexp))(quote +) 
         (plus (value (car (cdr nexp)) 
               (value (car (cdr (cdr nexp))))))
      ;第一个原子是*的话
      ((eq?(car nexp)))(quote *) 
         (mtply (value (car (cdr nexp)) 
                (value (car (cdr (cdr nexp))))))
       )
      ;最后一种情况肯定就是幂了
      (else 
         (power (value (car (cdr nexp)) 
                (value (car (cdr (cdr nexp))))))))))
;这个程序有bug！不信代入(+ 1 3)进去试试
; 第一个问题 因为(+ 1 3)不是atom所以不执行，到第二个问题；
; 处理value()
;
;
; 
;通过以上几个函数，不难发现经常需要取算数表达式的
;第一个，第二个子算数表达式
;以及中间的算数操作符(+, *, ^)
;可以把这些取subexp的过程定义为函数嘛。
(define 1st-sub-exp
  (lambda (aexp)
    (car (cdr aexp))))

(define 2nd-sub-exp
  (lambda (aexp)
    (car (cdr (cdr aexp)))))

(define operator
  (lambda (aexp)
    (car aexp)))

;用以上三个函数重写value函数。
(define value
  (lambda nexp)
    (cond
      ((atom? aexp) aexp)
      ((eq? (operator nexp)(quote +))
        (plus (value (1st-sub-exp nexp)) 
              (value (2nd-sub-exp nexp))))
      ((eq? (operator nexp)(quote *))
        (mtply (value (1st-sub-exp nexp)) 
               (value (2nd-sub-exp nexp))))
      (else
        (power (value (1st-sub-exp nexp)) 
               (value ((2nd-sub-exp nexp)))))))

; ---------------------------------------------
;     9th Commandment
;     Use help function to abstract from representations.
; ---------------------------------------------
;

;用新的表达符号来表达one,two,three这些意思:
;0: ()
;1: (())
;2: (() ())
;3: (() () ())
;原来我们使用number? zero? add1 sub1这四个函数作为primitive fun.

;sero test for zero.
(define sero
  (lambda (n)
    (null? n)))

;a function like add1
(define edd1
  (lambda (n)
    (cons (quote()) n)))
 
;a function like sub1
(define zub1
  (lambda (n)
    (cdr n)))

;a function like plus
(define blus
  (lambda (n m)
    (cond 
      ((zero? m) n)
      (else(edd1(blus n (zub1 m)))))))

;recall lat?
(define latt?
  (lambda (l)
    (cond
      ((null? l) #t)
      ((atom?(car l))(latt?(cdr l)))
      (else #f))))
;写这个函数是为了说明，
;对于以前的数字表示法来说，(lat? ls) when ls is(1 2 3) is true
;但是对新的表示法来说，(latt? ls) when ls is ((()) (()()) (()()()))
;就完全不对！！！
; be ware of shadows !!!

