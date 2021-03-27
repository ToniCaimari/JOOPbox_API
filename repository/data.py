from jsonschema import validate
import json
from service.date_validator import date_validator
from service.email_validator import email_validator
from service.nif_validator import nif_validator


class Data():

    # esquema Json para la validación
    schema = {
        "type": "object",
        "properties": {
            "name":     {"type": "string"},
            "id":       {"type": "string"},
            "phone_number": {"type": "number"},
            "street_name":  {"type": "string"},
            "street_type":  {
                "type": "string",
                "enum": ["Street", "Avenue", "Boulevard", "Square", "Other"]
            },
            "birth_date":  {"type": "string"},
            "email":  {"type": "string"},
            "interests": {
                "type": "array",
                "items": {"type": "string"}
            }
        },
        "required": ["name", "id", "phone_number"],
        "additionalProperties": False
    }

    # datos a validar
    datos = {"data": [
        {
            "name": "Jhon Snow",
            "id": "12345678-Z",
            "phone_number": 600000000,
            "street_name": "JSON square 12",
            "street_type": "Square"
        },
        {
            "name": "Jean Doe",
            "id": "X7654321-J",
            "phone_number": 616000000,
            "street_name": "python's exception 23, 1",
            "street_type": "Street",
            "birth_date": "1995-12-12"
        },
        {
            "name": "Alex Dotcom",
            "id": "17283946-K",
            "phone_number": 34619000000,
            "street_name": "Java Class 7, 8",
            "street_type": "Avenue",
            "birth_date": "1998-04-03",
            "interests": ["work", "jobs", "production"]
        },
        {
            "name": "Dr. X",
            "id": "00000000-X",
            "phone_number": 609000000,
            "street_name": "PHP spaguetti code 169, 5",
            "street_type": "Boulevard",
            "birth_date": "12-12-1995",
            "interests": "Rule the world",

        },
        {
            "name": "Toni Caimari",
            "id": "49483962-Z",
            "phone_number": 616000540,
            "street_name": "python's exception 22, 1",
            "street_type": "Street",
            "birth_date": "12-12-1995"
        },
        {
            "name": "Coni Taimari",
            "id": "49483962-Z",
            "phone_number": 616036540,
            "email": "estonoesunemail",
            "street_name": "python's exception 50, 1",
            "street_type": "Street",
            "birth_date": "1995-12-12"
        },
        {
            "name": "Cino Maitari",
            "id": "49483962-Z",
            "phone_number": 619636540,
            "email": "tonicaimbril@gmail.com",
            "street_name": "python's exception 44, 5",
            "street_type": "Street",
            "birth_date": "1995-06-09"
        }
    ]}

    @classmethod
    def get_list(cls):  # se crea una lista
        success = []
        fail = []
        datos = cls.datos
        schema = cls.schema
        for i in datos["data"]:
            try:
                # los datos pasan por el filtro validate y verifican el nif directamente ya que es un campo necesario
                validate(instance=i, schema=schema)
                if nif_validator(i) == True:
                    success.append(i)
                else:
                    fail.append(i)
            except:
                fail.append(i)

            try:
                date_validator(i) == True
                if email_validator(i) == True:
                    if i not in fail:
                        if i not in success:
                            success.append(i)
                else:
                    if i not in fail:
                        fail.append(i)
            except:
                if i not in fail:
                    fail.append(i)

                # se añaden a la lista los que pasen la validación
        return success

    @classmethod
    def get_fail(cls):  # se crea una lista
        success = []
        fail = []
        datos = cls.datos
        schema = cls.schema
        for i in datos["data"]:

            try:
                # los datos pasan por el filtro validate y verifican el nif directamente ya que es un campo necesario
                validate(instance=i, schema=schema)
                if nif_validator(i) == True:
                    success.append(i)
                else:
                    fail.append(i)
            except:
                fail.append(i)

            try:
                date_validator(i) == True
                if email_validator(i) == True:
                    if i not in fail:  # debido al primer filtro validate podría ya encontrarse en fail
                        success.append(i)
                else:
                    if i not in fail:  # debido al primer filtro validate podría ya encontrarse en fail
                        fail.append(i)
            except:
                if i not in fail:  # debido al primer filtro validate podría ya encontrarse en fail
                    fail.append(i)
        return fail
