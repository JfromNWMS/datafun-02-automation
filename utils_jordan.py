"""
File: utils_jordan.py

Purpose: Reusable Module for My Analytics Projects

Description: This module provides a byline for my analytics projects. 
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.

Advanced: This version requires a working .venv with loguru and pyttsx3 installed.
It includes a function to read the byline aloud using pyttsx3.

Author: JfromNWMS

"""

#####################################
# Import Modules
#####################################

# Import helpful modules from the Python Standard library
# Learn more: https://docs.python.org/3/library/

import statistics 

# Import packages from requirements.txt
# Learn more: https://pypi.org/project/loguru/ 
# Learn more:  https://pypi.org/project/pyttsx3/
#import loguru   # Easy logging
#import pyttsx3  # Text-to-speech engine

#####################################
# Configure Logger and Verify
#####################################

#logger = loguru.logger
#logger.add("project.log", level="INFO", rotation="100 KB") 
#logger.info("Logger loaded.")

#####################################
# Declare Global Variables
#####################################

# declare a boolean variable (has a value True or False)
is_math_student: bool = True

# declare an integer variable 
years_as_math_student: int = 20

# declare a floating point variable
# TODO: Add or replace this with your own floating point variable
favorite_irrational_number: float = 1.618

# declare a list of strings
last_three_math_courses: list = ["Abstract Algebra", "Calculus 7", "Euclidian Geometry"]

# declare a list of numbers so we can illustrate statistics skills 
last_three_course_scores: list = [74, 53, 98]

# Calculate basic statistics using built-in Python functions and the statistics module
min_score: float = min(last_three_course_scores)  
max_score: float = max(last_three_course_scores)  
mean_score: float = statistics.mean(last_three_course_scores)  
stdev_score: float = statistics.stdev(last_three_course_scores)

# Use a Python formatted string (f-string) to show information
byline: str = f"""
---------------------------------------------------------
Graduate Applicant Basic Analytics
---------------------------------------------------------
Current Student of Mathematics:       {is_math_student}
Years as a Mathematics Student:       {years_as_math_student}
Favorite Irrational Number:           {favorite_irrational_number:.3f}...
Last Three Math Courses:              {', '.join(last_three_math_courses)}
Final Scores of Courses:              {', '.join(map(str, last_three_course_scores))}
Minimum Course Score:                 {min_score}
Maximum Course Score:                 {max_score}
Mean Course Score:                    {mean_score:.1f}
Standard Deviation of Course Scores:  {stdev_score:.2f}
"""

#####################################
# Define global functions
#####################################

def get_byline() -> str:
    '''
    Get a byline for my analytics projects.
       
    Returns a string byline that illustrates my specific skills.

    A function is a block of code that performs a task.
    This function just returns our byline.
    We can call this (or other functions) in later modules 
    so we can write it once and reuse it. 
    We use a type hint to indicate this function returns a string
    (that is, it has a Python type of str).
    It doesn't need any additional information passed in, 
    so there's nothing needed inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''
    return byline


# Read the byline aloud (requires pyttsx3)
"""
def read_byline_aloud():
    engine = pyttsx3.init()
    engine.say(get_byline())
    engine.runAndWait()
"""

#####################################
# Define main function for this module.
#####################################

def main() -> None:
    '''
    Print results of get_byline() when main() is called.

    This function just prints the byline to the console when we run this as a script.
    The type hint indicates this function doesn't return anything when called 
    (that is, it has a Python type of None).
    It doesn't need any additional information passed in, 
    so there's nothing inside the parentheses.
    Everything after the colon must be indented consistently (usually 4 spaces)
    '''

    print("START main() in utils_jordan.py")
    #loguru.logger.info("START main() in utils_jordan.py")

    print(get_byline())
    #loguru.logger.info("Byline:\n" + get_byline())

    # Uncomment to hear it read aloud:
    #read_byline_aloud()

    print("END main() in utils_jordan.py")
    #loguru.logger.info("END main() in utils_jordan.py")

#####################################
# Conditional Execution
#####################################

# If we are running this file as a script then call main()
# and verify our code works as expected.

if __name__ == '__main__':
    main()