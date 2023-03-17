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
    print("provide answers in a scale of 1-7")
    print("example: 7 \n")


def get_questions():
    """
    gets questions from each colum
    allows uder to enter name
    iterates over each colum and produces answer box
    adds input and returns  
    """
    question = SHEET.worksheet("questions").get_all_values()
    
    question_number = 0
    
    responses_str = []
    name = input(" To begin, enter name here:")
    responses_str.append(name)
    for col in question:
        question_number += 1
        print(f"\n Question {question_number}:{col}?")
        answer = input("Enter Answer Here:")
        while (not answer_is_valid(answer)):
            answer = input("Enter Answer Here:")
        # must be int so convert
        responses_str.append(int(answer))
    print(responses_str)    
    return responses_str

    
def answer_is_valid(value):
    """
    checks that answer is an integer and returns custom error message 
    checks that number is between 1 and 10 and returns custom error message   
    """
    try:
        if not value.isdigit() or 1 <= int(value) >= 8:
            raise ValueError
    except ValueError:
        print(f"Response should be in range 1-7. you replied {value}")
        return False
    return True


def store_response(data):
    """ 
    takes submitted answers from responses variable
    adds responses to spreadseet
    aligns responses with corresponding question 
    """
    print("Processing results...")
    add_to_worksheet = SHEET.worksheet("users")
    add_to_worksheet.append_row(data) 


def average_responses(data):
    """
    takes responses submitted by each user and finds average for each question
    """   
    all_answers = data[1:-1]
    all_answers.append(data[-1])
    avg = sum(all_answers) // len(all_answers)
    data.append(avg)
    return data
    

def main():
    """
    calls all functions in one main function
    """
    survey_structure()
    user_results = get_questions()
    all_data = average_responses(user_results)
    store_response(all_data)


print(" \nwelcome to our health and fitness survey \n")
main()
