import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('survey')


def survey_structure():
    """
    survey overall structure
    prints instructions of the survey 
    """
    print("please fill out all questons in survey")
    print("provide answers in a scale of 1-10, where 5 is the average")
    print("example: 7 \n")


def get_questions():
    """
    gets questions from each colum
    iterates over each colum and produces answer box
    adds input and returns  
    """
    question = SHEET.worksheet("questions").get_all_values()
    
    question_number = 0
    
    responses = []
    
    for col in question:
        question_number += 1
        print(f"\n Question {question_number}:{col}?")
        answer = int(input("Enter Answer Here:"))
        responses.append(answer)
        # validate_answer(answer)
    return responses
     

# def validate_answer(value):
#     """
#     checks that answer is an integer and returns custom error message 
#     checks that number is between 1 and 10 and returns custom error message   
#     """
#     try:
#         if 1 <= value >= 11:
#             raise ValueError(
#                 f"response should be in range 1-10. you replied {value}"
#             )
#     except ValueError as e:
#         print(f"incorrect data. you entered: {e} ")


def store_response():
    """
    takes submitted answers from responses variable
    adds responses to spreadseet
    aligns responses with corresponding question 
    """

def average_responses():
    """
    takes all responses submitted by each user and finds average for each question
    """        
           

def main():
    """
    calls all functions in one main function
    """
    survey_structure()
    get_questions()


main()