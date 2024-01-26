import random
def get_numbers_ticket(min, max, quantity):
    list=[]
    if min<max:
        while len(list)<max:
            b=random.randint(min, max)
            if b not in list:
                list.append(b)
        c=random.sample(list, quantity)
        d=sorted(c)
        return d
    else:
        print('не вірно вказані дані: min має бути менше max')

lottery_numbers = get_numbers_ticket(100,50,6)
print("Ваші лотерейні числа:", lottery_numbers)
