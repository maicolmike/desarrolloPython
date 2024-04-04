def date_format(value):
    months = ("Enero", "Februar", "Marzo", "Abril")
    month = months[value.month -1]
    return "{} de {} del {}".format(value.day, month, value.year)