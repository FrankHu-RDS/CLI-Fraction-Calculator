import pytest
from ..main import main
from unittest.mock import Mock

def test_main_calculation_divide_by_zero(capsys):
    ret = main(['calc', '2/3 / 0'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert 'error cannot divide by 0' in out
    assert err == ''

def test_main_calculation_divide_by_fraction_zero(capsys):
    ret = main(['calc', '2/3 / 1/0'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert 'error cannot divide by 0' in out
    # assert 'the following arguments are required: equation' in err


def test_main_calculation_incorrect_input_0(capsys):
    a = Mock()
    a.side_effect = SystemExit
    with pytest.raises(SystemExit, match='2') as cm:
        ret = main(['calc'])
    out, err = capsys.readouterr()

def test_main_calculation_incorrect_input(capsys):
    ret = main(['calc', 'asdf'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert 'Too few arguments' in out
    # assert 'process calc: error: the following arguments are required: equation' in err


def test_main_calculation_incorrect_input_2(capsys):
    ret = main(['calc', 'asdf asdf asdf'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert 'The equation was improperly formatted, please put in a correctly formatted equation' in out
    # assert 'process calc: error: the following arguments are required: equation' in err


def test_main_calculation_incorrect_input_mixed_number_formatting_error(capsys):
    a = Mock()
    a.side_effect = ValueError
    with pytest.raises(ValueError, match='Improperly formatted equation') as cm:
        ret = main(['calc', '2_10 / 2'])
    out, err = capsys.readouterr()
    # assert ret == 0
    # assert 'The equation was improperly formatted, please put in a correctly formatted equation' in out
    # assert 'process calc: error: the following arguments are required: equation' in err


def test_main_calculation_incorrect_input_3(capsys):
    ret = main(['calc', '10 asdf 10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert 'The equation was improperly formatted, please put in a correctly formatted equation' in out
    # assert 'process calc: error: the following arguments are required: equation' in err