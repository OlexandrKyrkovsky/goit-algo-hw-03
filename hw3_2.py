import random


def get_numbers_ticket(min, max, quantity):
    list=[]
    if (min<max) and (1<min<1000) and (max<1000) and (min<quantity<max):
        while len(list)<(max-min):
            b=random.randint(min, max)
            if b not in list:
                list.append(b)
        c=random.sample(list, quantity)
        d=sorted(c)
        return d
    else:
        print('не вірно вказані дані')


lottery_numbers = get_numbers_ticket(5,80,90)
print("Ваші лотерейні числа:", lottery_numbers)
