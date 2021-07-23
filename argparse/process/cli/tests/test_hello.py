import pytest
from ..main import main


def test_hello(capsys):
    with pytest.raises(SystemExit) as exc:
        main(['how-to', '--help'])
    out, err = capsys.readouterr()
    assert exc.value.args[0] == 0
    assert 'usage: process how-to [-h]' in out
    assert err == ''
