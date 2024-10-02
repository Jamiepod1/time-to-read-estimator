import math


def time_to_read_estimate(text, words_per_minute=200):
    if type(text) != str:
        raise Exception("Invalid input type, must be str")
    
    
    words = text.split()
    number_of_words = len(words)
    if number_of_words == 0:
        return "Nothing to read!"
    
    
    words_per_second = words_per_minute / 60
    seconds_to_read = number_of_words / words_per_second

    rounded_seconds_to_read = math.ceil(seconds_to_read)
        
    minutes_to_read = rounded_seconds_to_read / 60
    hours_to_read = minutes_to_read / 60

    if hours_to_read >= 1:
        hours_to_read = int(hours_to_read)
        output_string = f"{hours_to_read} Hour"
        remaining_minutes_to_read = int(minutes_to_read) % 60
        if remaining_minutes_to_read > 0:
            output_string += f", {remaining_minutes_to_read} Minute"
            

        remaining_seconds_to_read = rounded_seconds_to_read % 60
        if remaining_seconds_to_read > 0:
            output_string += f", {remaining_seconds_to_read} Second"
        if remaining_seconds_to_read > 1:
            output_string += "s"
        

    elif minutes_to_read >= 1:
        minutes_to_read = int(minutes_to_read)
        remaining_seconds_to_read = rounded_seconds_to_read % 60
        output_string = f"{minutes_to_read} Minute"
        if minutes_to_read > 1:
            output_string += "s"
        if remaining_seconds_to_read > 0:
            output_string += f", {remaining_seconds_to_read} Second"
        if remaining_seconds_to_read > 1:
            output_string += "s"
    
    elif rounded_seconds_to_read > 1:
        output_string = f"{rounded_seconds_to_read} Seconds"
    else:
        output_string = f"{rounded_seconds_to_read} Second"
        
    return output_string