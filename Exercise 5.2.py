from datetime import datetime, timedelta

def print_working_days(date1, date2):
    start_date = datetime.strptime(date1, '%Y-%m-%d')
    end_date = datetime.strptime(date2, '%Y-%m-%d')

    while start_date < end_date:
        if start_date.weekday() < 5:
            print(start_date.strftime('%Y-%m-%d'))
        start_date += timedelta(days=1)

# Example:
print_working_days('2024-04-01', '2024-04-15')
