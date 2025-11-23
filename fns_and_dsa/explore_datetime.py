from datetime import date, time, datetime, timedelta


def display_current_datetime ():
    now = datetime.now()
    return now




def calculate_future_date ():
    current = display_current_datetime()
    days = int(input ('Enter the number of days to add to the current date: '))
    future_date = current + timedelta(days= days)
    print("Future date: ", future_date.strftime("%Y-%m-%d"))
    return future_date


current_date = display_current_datetime().strftime("%Y-%m-%d %H:%M:%S")
print("Current date and time: ", current_date)
calculate_future_date()
