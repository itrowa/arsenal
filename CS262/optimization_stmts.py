# Living statement: the value that holds my be needed in the future.
# formally we say a variable is live at some point P if it may be read
# before being overwritten after P. 


# live: 这个变量是不是live的, 是相对于某一行而言的.
# 在某一行处, 这个变量被overwrite前 它会被读取. 我们就说这个variable相对于这一行而言, 是live的.
# 