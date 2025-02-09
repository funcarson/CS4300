#Test file for task3

import importlib
import pytest
import task3 

def test_is_prime():
    #Test cases for the is_prime function.
    #Primes
    assert task3.is_prime(2) is True
    assert task3.is_prime(3) is True
    assert task3.is_prime(5) is True
    assert task3.is_prime(7) is True
    #Non-prime or edge cases
    assert task3.is_prime(1) is False  
    assert task3.is_prime(4) is False  
    assert task3.is_prime(6) is False   
    assert task3.is_prime(-3) is False  

#Tests to make sure the prime list is correct
def test_primes_list():
    expected_primes = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]
    assert task3.primes == expected_primes

#Tests if total is = to 5050 in task3
def test_sum():
    assert task3.total == 5050

#Tests all the printed outputs
def test_printed_output(capsys):
    importlib.reload(task3)
    captured = capsys.readouterr().out.splitlines()
    assert captured[0] == "This num is even!"
    assert captured[1] == "[2, 3, 5, 7, 11, 13, 17, 19, 23, 29]"
    assert "5050" in captured[2]
