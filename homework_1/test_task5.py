#Task 5 test file
import importlib
import pytest
import task5 

#Tests the printed statements for correctness
def test_printed_output(capsys):
    #Reload the module to re-run the print statements so that output is captured.
    importlib.reload(task5)
    captured = capsys.readouterr().out.splitlines()

    #Expected output:
    expected_output = [
        "Lord of the Flies by William Golding",
        "Farenheight 451 By Ray Bradbury",
        "1984 by George Orwell",
        "Student Name: Alice Johnson, Student ID: S001",
        "Student Name: Bob Smith, Student ID: S002",
        "Student Name: Charlie Brown, Student ID: S003",
        "Student Name: Diana Prince, Student ID: S004"
    ]
    assert captured == expected_output
