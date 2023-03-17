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
    name = input("To begin, enter name here:")
    responses_str.append(name)
    for col in question:
        question_number += 1
        print(f"\nQuestion {question_number}:{col}")
        answer = input("Enter Answer Here:")
        while (not answer_is_valid(answer)):
            answer = input(" Enter Answer Here: ")
        # must be int so convert
        responses_str.append(int(answer))    
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
    print("\nProcessing results...")
    add_to_worksheet = SHEET.worksheet("users")
    add_to_worksheet.append_row(data) 


def add_average_of_user_respones(data):
    """
    takes responses submitted by each user and finds the average score
    adds average store to end of string with name and submitted responses 
    """  
    print("\ncalculating averages...")

    all_answers = data[1:-1]
    all_answers.append(data[-1])
    avg = sum(all_answers) // len(all_answers)
    data.append(avg)
    return data


def display_user_responses(data):
    """
    shows user their submitted scores
    takes the average score  
    if average score is in certain range, custom message is printed 
    """   

    name = data[0]
    responses = data[1:-1]
    average = data[-1]
    
    print(f"\n{name}, you submitted:\n{responses} as your responses")
    print(f"\nAverage response you submitted was:\n{average}")
    
    if average == 1 or average == 2:
        print("\nyou recorded your health and fitness as below average ")
    elif average == 3 or average == 4:
        print("\nyou recorded your health and  fitness as average ")
    else:
        print("\nyou recorded your health and fitness as above average.")


def main():
    """
    calls all functions in one main function
    """
    survey_structure()
    user_results = get_questions()
    all_data = add_average_of_user_respones(user_results)
    store_response(all_data)
    display_user_responses(all_data)


print(" \nwelcome to our health and fitness survey \n")
main()
