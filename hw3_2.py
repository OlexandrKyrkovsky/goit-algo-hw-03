import random
def get_numbers_ticket(min, max, quantity):
    list=[]
    while len(list)<max:
        b=random.randint(min, max)
        if b not in list:
            list.append(b)
    c=random.sample(list, quantity)
    d=sorted(c)
    return d

lottery_numbers = get_numbers_ticket(1,100,6)
print("Ваші лотерейні числа:", lottery_numbers)
