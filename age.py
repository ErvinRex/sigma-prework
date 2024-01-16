from datetime import date
# use date to take tuple of integers as dob
birthday = date(2000, 2, 20)


# define our function
def calculate_age(dob):
    # obtain today's date
    today = date.today()
    # find the difference in years
    years = today.year - dob.year
    # if function so that if the day and month is not larger than today's date
    # then deduct 1 year.
    if today.month <= dob.month and today.day < dob.year:
        years -= 1
    # return the years of age.
    print(years)


calculate_age(birthday)
