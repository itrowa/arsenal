# input func: 用户的键盘输入将全部被捕获并被user_name引用. 而且是string类型的
user_name = input('Please enter your name:')

# processing..
print("Your name in all capital is", user_name.upper(),
      "and has length",              len(user_name))