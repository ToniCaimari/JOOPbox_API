import pytest
from repository.data import Data


@pytest.mark.filtro
def test_data_list():

    assert 4 == len(Data.get_list())


def test_data_fail():

    assert 3 == len(Data.get_fail())
