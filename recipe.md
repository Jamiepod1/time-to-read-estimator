# {{PROBLEM}} Function Design Recipe

Copy this into a `recipe.md` in your project and fill it out.

## 1. Describe the Problem


> As a user
> So that I can manage my time
> I want to see an estimate of reading time for a text, assuming that I can read 200 words a minute.


## 2. Design the Function Signature

_Include the name of the function, its parameters, return value, and side effects._

```python
# EXAMPLE

def calculate_time_to_read_text(text, words_per_minute):
    """Extracts uppercase words from a string

    Parameters:
        text: a string containing words
        words_per_minute: an integer with a default value of 200

    Returns:
        an string representing time to read the text (e.g. "1 Hour, 53 Minutes", "30 Seconds")

    Side effects:
        This function doesn't print anything or have any other side-effects
    """
    pass # Test-driving means _not_ writing any code here yet.
```

## 3. Create Examples as Tests

_Make a list of examples of what the function will take and return._

```python
# EXAMPLE

"""
Given an empty string
It returns a string with a warning
"""
calculate_time_to_read_text("") => ["Nothing to read!"]

"""
Given a string with one word
It returns a string, time rounded up to nearest second
"""
calculate_time_to_read_text("Hello") => ["1 Second"]

"""
Given a string with two words
It returns a string, time rounded up to nearest second
"""
calculate_time_to_read_text("Hello world") => ["1 Second"]

"""
Given a string with 9 words
It returns a string, time rounded up to nearest second
"""
calculate_time_to_read_text("Hello world this will take three seconds rounded up") => ["3 Seconds"]

"""
Given a string with 2 words, punctuation and upper case characters
It returns a string, time rounded up to nearest second
"""
calculate_time_to_read_text("hello, WORLD!") => ["1 Second"]

"""
Given a string with 200 words
It returns a string, now displaying minutes
"""
calculate_time_to_read_text("(A string of length 400 words)") => ["1 Minute"]

"""
Given a string with 400 words
It returns a string, now displaying minutes
"""
calculate_time_to_read_text("(A string of length 400 words)") => ["2 Minutes"]

"""
Given a string with 500 words
It returns a string, now displaying minutes and seconds
"""
calculate_time_to_read_text("(A string of length 400 words)") => ["2 Minutes, 30 Seconds"]

"""
Given a string with 12000 words
It returns a string, now displaying hours
"""
calculate_time_to_read_text("(A string of length 400 words)") => ["1 Hour"]

"""
Given a string with 12200 words
It returns a string, now displaying hours
"""
calculate_time_to_read_text("(A string of length 400 words)") => ["1 Hour, 1 Minute"]

"""
Given a string with 12300 words
It returns a string, now displaying hours
"""
calculate_time_to_read_text("(A string of length 400 words)") => ["1 Hour, 1 Minute, 30 seconds"]

"""
Given a None value
It throws an error
"""
calculate_time_to_read_text(None) throws an error
```

_Encode each example as a test. You can add to the above list as you go._

## 4. Implement the Behaviour

_After each test you write, follow the test-driving process of red, green, refactor to implement the behaviour._

Here's an example for you to start with:

```python
# EXAMPLE

from lib.extract_uppercase import *

"""
Given a lower and an uppercase word
It returns a list with the uppercase word
"""
def test_extract_uppercase_with_upper_then_lower():
    result = extract_uppercase("hello WORLD")
    assert result == ["WORLD"]
```