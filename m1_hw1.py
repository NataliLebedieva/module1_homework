from datetime import datetime



def get_days_from_today(date):
    input_date_str = input("Введіть дату в форматі РРРР-ММ-ДД: ") 
    input_date = datetime.strptime(input_date_str, '%Y.%m.%d')
    date_today = datetime.today()
    print(input_date_str, type(input_date_str))
    print(input_date, type(input_date))
    print((date_today).date())
get_days_from_today()
    