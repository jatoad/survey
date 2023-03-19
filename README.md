# Health and Fitness Survey
- This command-line interface programme aims to take user health and fitness data, calculates their average response and returns a custom response based on their average 

## How to use
- Enter name to begin, and enter scores on a scale from 1-7 for each question on how you feel best suits you. Press enter on each question to submit your answer. If you submit the wrong data type or a number outside the range of 1-7, the question will reappear and you will need to enter a valid answer to continue. Once all questions are answered, the prgramme will show you the responses that you ahevsubmitted, your average, and a message based off of that average score.

## Features

### - Instructions and start of survey
![screen shot of start of survey instructions when first loded up](/images/start_screen.png)
- prints instructions for the survey and gives example. 
- user puts in username here and begins survey 

### - Questions Asked to User 
![screen shot of start of some of the questions aked to the user](/images/questions.png)
- all questions in the quiz are printed one at a time from question 1-7 
- user must supply a valid respone t ocintinue onto the next question 

### - Error Messages
![screen shot of invalid data submitted by the user](/images/error_response.png)
- if the user submits invalid data(integers outside the range of 1-7 and non integer responses), an error message occurs.
this will loop the question until the correct data is submitted by the user, where they willthen be able to continue onto the next question.

### - Response after Questions are submitted
![screen shot of response after the user had submitted all questions](/images/response.png)
- once all questions are filled in and answered the terminal prints a response, using the username provided to at the beginng 
- a list of answers submitted
- the average score 
- message printed(determined bt the average score of the user)

### - spreadseet data
![screen shot of questions in spreadsheeet](/images/spreadsheet_questions.png)
- all questions in spreadsheet
![screen shot of questions in spreadsheeet](/images/user_data.png)
- responses, average and username submitted by user added to page on spreadsheet 

## Bug Fixes 
- error message qould only print correctly if it was correct data type and not in range. if, for example a letter was supplied fot the question answer, the programme would break its loop. this was fixed by changing the exception handler to treat all errors the amse and provide a univeral response for everything. in the future i would like to add seperate responses for the different errors, however at this moment i was unabke to get it working
- during the process of the project my computer crashed and uninstalled the google auth and gspread from the file, which caused the code to be unable to import them. I was able to identify this after trialing a range of probable causes for the error and re-install to get the project running again 

## - Testing the code 
- ran the code through the PEP8 linter and no major errors were flagged
- used print statements throughout the code to identify if functions and processes were working in the intended way
- went through different invalid inputs to see what each would do to the programme

## - Future Additions
- in the future i would like to add a feature that will alow the user to change answers if needed



LO1Implement a given algorithm as a computer program

1.1	Write Python code that passes through a linter (eg PEP8) with no significant issues.
1.2	Ensure all intended functionality works as per the critical project objectives
1.3	Write code that meets minimum standards for readability (comments, indentation, consistent and meaningful naming conventions).
LO2 Adapt and combine algorithms to solve a given problem

2.1	Write code that handles empty or invalid input data.
2.2	Clearly separate and identify code written for the application and code from external sources (e.g. libraries or tutorials)
2.3	Ensure a consistent flow of logic and data with well defined granular functions
LO3 Adequately use standard programming constructs: repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.)

3.1	Implement standard programming constructs such as flow control, iteration, selection, functions, object-oriented programming and data structures - as appropriate - to achieve the project goals.
3.2	Implement exception/error handling to optimise the user experience
LO4 Explain what a given program does

4.1	Use consistent and effective markdown formatting that is well-structured, easy to follow, and has few grammatical errors when writing a README file.
4.2	Write a README.md file in English for the Python application that explains its purpose and the value that it provides to its users.
LO5 Identify and repair coding errors in a program

5.1	Implement basic manual testing procedures for code validation
LO6 Use library software for building a graphical user interface, or command-line interface, or web application, or mathematical software

6.1	Implement the use of external Python libraries where appropriate to provide the functionality that the project requires.
LO7 Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.

7.1	Implement a working data model that supports the intended project functionality
7.2	Write code that queries and manipulates data to meet the identified vital project needs.
LO8 Demonstrate and document the development process through a version control system such as GitHub

8.1	Use Git & GitHub for version control of the web application up to deployment.
LO9 Deploy a command-line application

9.1	Deploy a final version of the Python Essentials application code to a cloud-based platform.
9.2	Ensure that the deployed application is free of commented out code.

O1	Implement a given algorithm as a computer program
LO2	Adapt and combine algorithms to solve a given problem
LO3	Adequately use standard programming constructs: repetition, selection, functions, composition, modules, aggregated data (arrays, lists, etc.)
LO4	Explain what a given program does
LO5	Identify and repair coding errors in a program
LO6	Use library software for building a graphical user interface, or command-line interface, or web application, or mathematical software
LO7	Implement a data model, application features and business logic to manage, query and manipulate data to meet given needs in a particular real-world domain.
LO8	Demonstrate and document the development process through a version control system such as GitHub
L09	Deploy a command-line application to a cloud-based platform