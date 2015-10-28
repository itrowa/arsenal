(define (sumsq-of-bigger x y z)
  if (< x y)
    ;if成立的分支，现在再比较x和z即可
    (if (< x z) 
              (+ (* z z )(* y y ));zy
              (+ (* x x )(* y y ));xy
              )
    ;if不成立的分支，现在再比较y和z即可
    (if (< y z)
              (+ (* x x )(* z z ));xz
              (+ (* x x )(* y y ));xy
              )
    )
