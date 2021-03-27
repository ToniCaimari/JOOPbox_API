import pytest
from service.nif_validator import nif_validator


@pytest.mark.nif_format
def test_nif_validatorTrue():

    assert True == nif_validator({"id": "49483962-Z"})


@pytest.mark.nif_format
def test_nif_validatorFalse():

    assert False == nif_validator({"id": "00050690-Z"})
