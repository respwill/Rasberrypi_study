# define function
def addsub(num1=20, num2=10):
    hap = num1 + num2
    cha = num1 - num2
    return (hap, cha)

# call function -> execution

n1 = int(input('num1?: '))
n2 = int(input('num2?: '))

hap, cha = addsub(n1, n2)
print('{} + {} = {}'.format(n1, n2, hap))
print('{} - {} = {}'.format(n1, n2, cha))

hap, cha = addsub(n1)
print('{} + default = {}'.format(n1, hap))
print('{} - default = {}'.format(n1, cha))


hap, cha = addsub()
print('default + default = {}'.format(hap))
print('default - default = {}'.format(cha))
