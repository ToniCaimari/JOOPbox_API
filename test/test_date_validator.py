import pytest
from service.date_validator import date_validator
import datetime


def if_validate(sample):
    try:
        date_validator(sample)
        return True
    except:
        return False


@pytest.mark.date_format
def test_date_validator():
    assert datetime.datetime(1999, 12, 5, 0, 0) == date_validator(
        {"birth_date": "1999-12-05"})

    assert False == if_validate({"birth_date": "15-12-2005"})
    assert True == if_validate({"birth_date": "2005-12-15"})
