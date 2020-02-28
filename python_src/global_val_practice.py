def f1():
    global count
    count = 200
    print('f1: ', count)

count = 100
print('before f1 main: ', count)
f1()
print('after f1 main: ', count)
