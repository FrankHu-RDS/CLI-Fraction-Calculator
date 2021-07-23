import pytest
from ..main import main


def test_main_help(capsys):
    with pytest.raises(SystemExit) as exc:
        main(['--help'])
    out, err = capsys.readouterr()
    assert exc.value.args[0] == 0
    assert 'usage: process [-h] [--loglevel {debug,info,warning,error,critical}]' in out
    assert err == ''


def test_main_argparse_error(capsys):
    with pytest.raises(SystemExit) as exc:
        main(['--loglevel', 'spam'])
    out, err = capsys.readouterr()
    assert exc.value.args[0] == 2
    assert out == ''
    assert "error: argument --loglevel: invalid choice: 'spam'" in err

def test_main_success(capsys):
    ret = main(['--loglevel', 'info', 'calc', '1/2 + 7/8'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '1_3/8' in out
    assert err == ''

def test_main_calculation_test_1(capsys):
    ret = main(['calc', '2_3/8 + 9/8'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '3_4/8' in out
    assert err == ''

def test_main_calculation_test_2(capsys):
    ret = main(['calc', '2/4 + 3/4'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '1_1/4' in out
    assert err == ''

def test_main_calculation_test_3(capsys):
    ret = main(['calc', '3_1/2 + 10/20'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '4' in out
    assert err == ''


def test_main_calculation_test_1(capsys):
    ret = main(['calc', '2 + 3'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '5' in out
    assert err == ''


def test_main_calculation_test_4(capsys):
    ret = main(['calc', '1_1/2 + 1_7/8'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '3_3/8' in out
    assert err == ''


def test_main_calculation_test_5(capsys):
    ret = main(['calc', '1/2 / 7/8'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '8/14' in out
    assert err == ''


def test_main_calculation_test_6(capsys):
    ret = main(['calc', '2_100/200 / 3/8'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '6_400/600' in out
    assert err == ''



def test_main_calculation_divide_wholes(capsys):
    ret = main(['calc', '2 / 4'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '2/4' in out
    assert err == ''



def test_main_calculation_divide_mixeds_2(capsys):
    ret = main(['calc', '1_2/3 / 4_1/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '50/123' in out
    assert err == ''



def test_main_calculation_divide_whole_mixed(capsys):
    ret = main(['calc', '2 / 1_4/3'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '6/7' in out
    assert err == ''



def test_main_calculation_divide_mixeds(capsys):
    ret = main(['calc', '2_2/3 / 2_4/3'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '24/30' in out
    assert err == ''

def test_main_calculation_divide_fractions(capsys):
    ret = main(['calc', '2/3 / 4/9'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '1_6/12' in out
    assert err == ''

def test_main_calculation_addition_wholes(capsys):
    ret = main(['calc', '2 + 4'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '6' in out
    assert err == ''


def test_main_calculation_addition_fractions(capsys):
    ret = main(['calc', '2/5 + 4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '8/10' in out
    assert err == ''


def test_main_calculation_addition_mixeds(capsys):
    ret = main(['calc', '2_2/5 + 1_4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '3_8/10' in out
    assert err == ''

def test_main_calculation_addition_whole_mixed_1(capsys):
    ret = main(['calc', '2 + 1_4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '3_4/10' in out
    assert err == ''


def test_main_calculation_addition_whole_mixed_2(capsys):
    ret = main(['calc', '0 + 1_4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '1_4/10' in out
    assert err == ''



def test_main_calculation_multiplication_wholes(capsys):
    ret = main(['calc', '2 * 4'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '8' in out
    assert err == ''


def test_main_calculation_multiplication_fractions(capsys):
    ret = main(['calc', '2/5 * 4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '8/50' in out
    assert err == ''


def test_main_calculation_multiplication_mixeds(capsys):
    ret = main(['calc', '2_2/5 * 1_4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '3_18/50' in out
    assert err == ''

def test_main_calculation_multiplication_whole_mixed_1(capsys):
    ret = main(['calc', '2 * 1_4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '2_8/10' in out
    assert err == ''


def test_main_calculation_multiplication_whole_mixed_2(capsys):
    ret = main(['calc', '0 * 1_4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '0' in out
    assert err == ''


def test_main_calculation_subtraction_wholes(capsys):
    ret = main(['calc', '2 - 4'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '-2' in out
    assert err == ''


def test_main_calculation_subtraction_fractions(capsys):
    ret = main(['calc', '2/5 - 4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '0' in out
    assert err == ''


def test_main_calculation_subtraction_mixeds(capsys):
    ret = main(['calc', '2_2/5 - 1_4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '1' in out
    assert err == ''

def test_main_calculation_subtraction_whole_mixed_1(capsys):
    ret = main(['calc', '2 - 1_4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '6/10' in out
    assert err == ''


def test_main_calculation_subtraction_whole_mixed_2(capsys):
    ret = main(['calc', '0 - 1_4/10'])
    out, err = capsys.readouterr()
    assert ret == 0
    assert '-1_4/10' in out
    assert err == ''