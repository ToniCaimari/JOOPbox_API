import pytest
from service.email_validator import email_validator


@pytest.mark.email_format
def test_date_validatorTrue():

    assert True == email_validator({"email": "toni.caimbril1@gmail.com"})
    assert True == email_validator({"id": "x485266"})


@pytest.mark.email_format
def test_date_validatorFalse():
    assert False == email_validator({"email": "estonoesunemail"})
