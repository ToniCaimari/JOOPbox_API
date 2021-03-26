import pytest
from repository.data import Data


@pytest.mark.filtro
def test_data():

    assert 3 == len(Data.get_list())
    assert 2 == len(Data.get_fail())
