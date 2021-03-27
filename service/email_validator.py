import re

regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'


def email_validator(element):

    if "email" in element.keys():
        if(re.search(regex, element["email"])):
            return True

        else:
            try:
                return False
            except:
                return False
    else:
        return True
