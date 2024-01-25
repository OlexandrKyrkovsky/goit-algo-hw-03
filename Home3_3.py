import re
number_of_phone=["067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

def normalize_phone(phone_number):
    p=r"[\d\+]+"
    el_phone_number=re.findall(p,phone_number)
    phone_number=''.join(el_phone_number)
    if len(phone_number)==10:
        phone_number='+38'+phone_number
    elif len(phone_number)==12:
        phone_number='+'+phone_number
    return phone_number


for phone in number_of_phone:
    print("Нормалізовані номери телефонів для SMS-розсилки:", normalize_phone(phone))