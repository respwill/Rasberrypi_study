# input : age
# ticket : <=6 : free, 7<= age <=18: 6500, 19<= age <=64: 10000, 65 <= age : free

age = int(input('age of customer? :'))

if age <= 6:
    ticket = 'free'
elif 7 <= age <= 18:
    ticket = 6500
elif 19 <= age <= 64:
    ticket = 10000
else:
    ticket = 'free'

print('Price of a ticket is {}'.format(ticket))

