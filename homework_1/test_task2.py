#Test file for task2
import runpy
import pytest

def test_task2_output(capsys):
    """
    Run task2.py and verify its printed output.
    """
    #Runs the script 
    runpy.run_path("task2.py")
    
    #Capture the output 
    captured = capsys.readouterr().out.strip().splitlines()
    
    #The expected output
    expected_output = [
        "12 + 16 = 28",
        "12.5 + 3.14 = 15.64",
        "Hello My name is Carson ",
        "True"
    ]
    
    assert captured == expected_output