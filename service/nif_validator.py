def nif_validator(nif):

    letter_list = "TRWAGMYFPDXBNJZSQVHLCKE"
    num_list = "1234567890"

    if (len(nif["id"]) == 10):
        dni = nif["id"][:8]
        if (len(dni) == len([n for n in dni if n in num_list])):
            if letter_list[int(dni) % 23] == nif["id"][9].upper():
                return True
            else:
                return False
        else:
            return False
    else:
        return False
