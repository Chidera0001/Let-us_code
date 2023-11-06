"""
Date-related calculations module.

This module provides functions to calculate days in a month, check date validity,
calculate days between two dates, and calculate a person's age in days.
"""

import datetime


def days_in_month(year, month):
    """
    Calculate the number of days in a given month and year.

    Args:
        year (int): The year.
        month (int): The month.

    Returns:
        int: The number of days in the month.
    """
    try:
        if 1 <= month <= 12 and datetime.MINYEAR <= year <= datetime.MAXYEAR:
            next_month = month % 12 + 1
            next_year = year + 1 if month == 12 else year
            first_day_of_next_month = datetime.date(next_year, next_month, 1)
            num_days = (first_day_of_next_month - datetime.date(year, month, 1)).days
            return max(num_days, 0)
        else:
            return 0
    except ValueError:
        return 0


def is_valid_date(year, month, day):
    """
    Check if a date is valid.

    Args:
        year (int): The year.
        month (int): The month.
        day (int): The day.

    Returns:
        bool: True if the date is valid, False otherwise.
    """
    try:
        return (
            0 < year <= datetime.MAXYEAR
            and 1 <= month <= 12
            and 1 <= day <= days_in_month(year, month)
        )
    except ValueError:
        return False


def days_between(year1, month1, day1, year2, month2, day2):
    """
    Calculate the number of days between two dates.

    Args:
        year1 (int): The year of the first date.
        month1 (int): The month of the first date.
        day1 (int): The day of the first date.
        year2 (int): The year of the second date.
        month2 (int): The month of the second date.
        day2 (int): The day of the second date.

    Returns:
        int: The number of days between the two dates.
    """
    try:
        date1 = datetime.date(year1, month1, day1)
        date2 = datetime.date(year2, month2, day2)
        return (date2 - date1).days if date1 <= date2 else 0
    except ValueError:
        return 0


def age_in_days(birth_year, birth_month, birth_day):
    """
    Calculate a person's age in days based on their birthdate.

    Args:
        birth_year (int): The year of birth.
        birth_month (int): The month of birth.
        birth_day (int): The day of birth.

    Returns:
        int: The person's age in days as of the current date.
    """
    try:
        birth_date = datetime.date(birth_year, birth_month, birth_day)
        current_date = datetime.date.today()
        if is_valid_date(birth_year, birth_month, birth_day) and birth_year > 0:
            age_days = (current_date - birth_date).days
            return max(age_days, 0)
        else:
            return 0
    except ValueError:
        return 0
