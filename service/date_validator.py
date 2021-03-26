import datetime


def date_validator(date_text):
    if "birth_date" in date_text.keys():
        return datetime.datetime.strptime(date_text["birth_date"], '%Y-%m-%d')
    else:
        return True
