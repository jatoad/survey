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
    # print(f"\n your responses:\n{responses}")     


def validate_answer():
    """
    """


def main():
    """
    calls all functions in one main function
    """
    survey_structure()
    get_questions()


main()