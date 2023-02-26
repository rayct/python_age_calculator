# This program will prompt the user for their date of birth, and then it will calculate current age, 
# the day of the week you were born on, and the number of days until your next birthday.
## To use the program, simply run it in a Python environment and follow the prompts.

## Version: 1.0.5
## In this further optimised version, we use an f-string to format the output strings with variables directly, which is more concise and easier to read.

## We also replace the ((now.month, now.day) < (birthdate.month, birthdate.day)) expression with int(now < next_birthday), which is more efficient and has the same result.

## Additionally, we use datetime.date instead of datetime.datetime throughout the code, which is more memory-efficient and requires fewer computations.

## Overall, these optimizations make the program more efficient, faster, and more readable.

## Ray C. Turner