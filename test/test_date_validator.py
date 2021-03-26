import pytest
from service.date_validator import date_validator
import datetime


@pytest.mark.date_format
def test_date_validator():
    assert datetime.datetime(1999, 12, 5, 0, 0) == date_validator(
        {"birth_date": "1999-12-05"})
    # assert datetime.datetime(2005, 12, 19, 0, 0) != date_validator(
    #     {"birth_date": "19-12-2005"})
