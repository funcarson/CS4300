#test file for task1
import pytest
def test_hello_world(capsys):
    import task1  
    captured = capsys.readouterr()
    assert "Hello World!" in captured.out