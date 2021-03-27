def nif_validator(nif):

    letter_list = "TRWAGMYFPDXBNJZSQVHLCKE"  # pull de letras y numeros
    num_list = "1234567890"

    if (len(nif["id"]) == 10):  # check sobre la longitud de id
        dni = nif["id"][:8]  # variable que conserva los numeros del id
        # comprobación de que toda la extensión de dni son numeros
        if (len(dni) == len([n for n in dni if n in num_list])):
            # validación de la letra del id comparando con la pull de letras
            if letter_list[int(dni) % 23] == nif["id"][9].upper():
                return True
            else:
                return False
        else:
            return False
    else:
        return False
