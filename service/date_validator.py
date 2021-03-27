import datetime


def date_validator(date_text):
    if "birth_date" in date_text.keys():  # birth_date no es un campo obligado en el json
        # check del formato del valor en la llave "birth_date"
        return datetime.datetime.strptime(date_text["birth_date"], '%Y-%m-%d')
    else:
        return True
