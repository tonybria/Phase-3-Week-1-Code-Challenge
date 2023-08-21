# Phase-3-Week-1-Code-Challenge
  
## Clock System
The convert_to_24_hour function takes three arguments: hour, minute, and period. It checks whether the given time is in the "pm" period and not equal to 12, in which case it adds 12 to the hour to convert it to 24-hour format. If the period is "am" and the hour is 12, it sets the hour to 0. Finally, it returns a formatted string with the hour and minute in 24-hour format.

## Alphabet
The consonant_value function iterates through the characters in the input string. If the character is a consonant (present in the consonant_values dictionary), it accumulates the value. If the character is not a consonant, the current accumulated value is reset to 0. The function returns the maximum accumulated value of consonant substrings.

## Interger
The exactly_two_positive function counts the number of positive integers among a, b, and c. If the count is exactly 2, the function returns True, indicating that two of the three numbers are positive. Otherwise, it returns False.