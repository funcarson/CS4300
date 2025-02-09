#Task 6 test file
import os
import task6
import pytest

#get the expected output 
def expected_count(filename):
    with open(filename, "r") as file:
        return len(file.read().split())

#List of text files to test
text_files = ["task6_readme.txt"]

#Dynamically generate test functions for each text file
for filename in text_files:
    def make_test(filename):
        def test_file():
            expected = expected_count(filename)
            result = task6.count_words(filename)
            assert result == expected, f"Expected {expected} words in {filename}, but got {result}"
        return test_file
    #Generate a test function name based on the filename, e.g. "test_task6_read_me_txt"
    test_name = f"test_{filename.replace('.', '_')}"
    globals()[test_name] = make_test(filename)
