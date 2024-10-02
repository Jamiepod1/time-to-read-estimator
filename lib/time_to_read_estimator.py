import math


def time_to_read_estimate(text, words_per_minute=200):
    if type(text) != str:
        raise Exception("Invalid input type, must be str")
    
    words = text.split()
    number_of_words = len(words)
    if number_of_words == 0:
        return "Nothing to read!"
    
    words_per_second = words_per_minute / 60
    
    seconds = number_of_words / words_per_second
    rounded_seconds = math.ceil(seconds)
    minutes = rounded_seconds / 60
    hours = minutes / 60
    
    output_list = []
    if hours >= 1:
        hours = int(hours)
        minutes = int(minutes) % 60
        rounded_seconds = rounded_seconds % 3600
        hour_string = f"{hours} Hour"
        if hours > 1:
            hour_string += "s"
            
        output_list.append(hour_string)

    if minutes >= 1:
        minutes = int(minutes)
        minute_string = f"{minutes} Minute"
        rounded_seconds %= 60
        if minutes > 1:
            minute_string += "s"
        output_list.append(minute_string)
        
    if rounded_seconds > 0:
        second_string = f"{rounded_seconds} Second"
        if rounded_seconds > 1:
            second_string += "s"
        output_list.append(second_string)
        
    return ", ".join(output_list)


# print(time_to_read_estimate(" ".join(["word" for num in range(0, 12000)])))