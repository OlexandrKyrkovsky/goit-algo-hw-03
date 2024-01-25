from datetime import datetime
while True:
    try:
        date_string = input('Enter date YYYY-MM-DD ')
        date = datetime.strptime(date_string, "%Y-%m-%d")
        break
    except Exception:
        print('Invalid format, enter YYYY-MM-DD')

def get_days_from_today(date):
    today = datetime.today()
    days = today.toordinal() - date.toordinal()
    print(f'Date entered:  {date}')
    print(f'Today  {today}')
    print(f'Difference   {days}')
    return days
    

delta = get_days_from_today(date)


