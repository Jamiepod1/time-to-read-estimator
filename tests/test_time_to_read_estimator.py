from lib.time_to_read_estimator import *
import pytest


def test_empty_string_returns_alert_message():
    result = time_to_read_estimate("")
    assert result == "Nothing to read!"
    
    
def test_string_suite_returns_1_Second():
    assert time_to_read_estimate("Hello") == "1 Second"
    assert time_to_read_estimate("Hello world") == "1 Second"
    assert time_to_read_estimate("Hello wide world") == "1 Second"
    

def test_string_suite_returns_n_Seconds():
    assert time_to_read_estimate("Four word long sentance") == "2 Seconds"
    assert time_to_read_estimate("This sentance is seven whole words long") == "3 Seconds"
    input_196_words = " ".join(["word" for num in range(0, 196)])
    assert time_to_read_estimate(input_196_words) == "59 Seconds"

    
def test_string_suite_returns_1_minute():
    input_197_words = " ".join(["word" for num in range(0, 197)])
    assert time_to_read_estimate(input_197_words) == "1 Minute"
    input_200_words = " ".join(["word" for num in range(0, 200)])
    assert time_to_read_estimate(input_200_words) == "1 Minute"


def test_string_suite_returns_1_minutes_1_second():
    input_201_words = " ".join(["word" for num in range(0, 201)])
    assert time_to_read_estimate(input_201_words) == "1 Minute, 1 Second"
    input_203_words = " ".join(["word" for num in range(0, 203)])
    assert time_to_read_estimate(input_203_words) == "1 Minute, 1 Second"


def test_string_suite_returns_1_minutes_n_seconds():
    input_204_words = " ".join(["word" for num in range(0, 204)])
    assert time_to_read_estimate(input_204_words) == "1 Minute, 2 Seconds"
    input_396_words = " ".join(["word" for num in range(0, 396)])
    assert time_to_read_estimate(input_396_words) == "1 Minute, 59 Seconds"
    
    
def test_string_suite_returns_n_minutes_1_second():
    input_401_words = " ".join(["word" for num in range(0, 401)])
    assert time_to_read_estimate(input_401_words) == "2 Minutes, 1 Second"
    input_11801_words = " ".join(["word" for num in range(0, 11801)])
    assert time_to_read_estimate(input_11801_words) == "59 Minutes, 1 Second"
    
    
def test_string_suite_returns_n_minutes():
    input_400_words = " ".join(["word" for num in range(0, 400)])
    assert time_to_read_estimate(input_400_words) == "2 Minutes"
    input_11800_words = " ".join(["word" for num in range(0, 11800)])
    assert time_to_read_estimate(input_11800_words) == "59 Minutes"
    
    
def test_500_word_string_returns_n_minutes_n_seconds():
    input_404_words = " ".join(["word" for num in range(0, 404)])
    assert time_to_read_estimate(input_404_words) == "2 Minutes, 2 Seconds"
    input_11996_words = " ".join(["word" for num in range(0, 11996)])
    assert time_to_read_estimate(input_11996_words) == "59 Minutes, 59 Seconds"
    
    
def test_12000_word_string_returns_1_hour():
    input_12000_words = ["word" for num in range(0, 12000)]
    input_12000_words = " ".join(input_12000_words)
    result = time_to_read_estimate(input_12000_words)
    assert result == "1 Hour"
    
    
def test_12200_word_string_returns_1_hour_1_minute():
    input_12200_words = ["word" for num in range(0, 12200)]
    input_12200_words = " ".join(input_12200_words)
    result = time_to_read_estimate(input_12200_words)
    assert result == "1 Hour, 1 Minute"
    
    
def test_12300_word_string_returns_1_hour_1_minute():
    input_12300_words = ["word" for num in range(0, 12300)]
    input_12300_words = " ".join(input_12300_words)
    result = time_to_read_estimate(input_12300_words)
    assert result == "1 Hour, 1 Minute, 30 Seconds"
    
    
def test_None_throws_an_error():
    with pytest.raises(Exception) as e:
        time_to_read_estimate(None)
    error = str(e.value)
    assert error == "Invalid input type, must be str"