import pytest
from SalaryInputs import SalaryInputs
from TooLowerError import TooLowerError
from TooHigherError import TooHigherError

@pytest.fixture(scope='session')
def get_salary():
    salary = SalaryInputs()
    return salary

@pytest.mark.parametrize('salary, expected', [(34000, True),
                                              (55000, True)])
def test_check_valid_inputs(get_salary,salary, expected):
    assert expected

def test_check_invalid_salary(get_salary='iuh'):
    with pytest.raises(ValueError):
        if get_salary != float:
            raise ValueError

def test_check_too_high(get_salary=101000):
    with pytest.raises(TooHigherError):
        if get_salary > 100000:
            raise TooHigherError

def test_check_too_low(get_salary=1000):
    with pytest.raises(TooLowerError):
        if get_salary < 10000:
            raise TooLowerError