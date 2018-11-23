#Задание 1
def my_round(a, b):
    a = a*(10**b)
    a = a//1
    return a/(10**b)
print(my_round(2.1234567, 5))
print(my_round(2.1999967, 5))
print(my_round(2.9999967, 5))

#Задание 2
def lucky_ticket(ticket_number):
    return (ticket_number[:3]) == sum(ticket_number[-3:])



print(lucky_ticket([123006]))
print(lucky_ticket([12321]))
print(lucky_ticket([436751]))

#почему-то не работает?