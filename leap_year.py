def is_leap_year(year):
    # Check if the year is divisible by 400
    if year % 400 == 0:
        return True
    # Check if the year is divisible by 100
    elif year % 100 == 0:
        return False
    # Check if the year is divisible by 4
    elif year % 4 == 0:
        return True
    # If none of the above conditions are met, it's not a leap year
    else:
        return False

# Example usage:
print(is_leap_year(2100)) 