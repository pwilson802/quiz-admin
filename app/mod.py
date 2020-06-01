import os
import requests
import json
import boto3
from random import randint
from boto3.dynamodb.conditions import Key, Attr

DYNAMO_DB = os.environ.get("TRIVIA_DYNAMODB")

cat_map = {
    'general_knowledge': '9',
    'entertainment_books': '10',
    'entertainment_film': '11',
    'entertainment_music': '12',
    'entertainment_musicals': '13',
    'entertainment_telivision': '14',
    'entertainment_video_games': '15',
    'entertainment_board_games': '16',
    'science_nature': '17',
    'science_computers': '18',
    'science_mathematics': '19',
    'mythology': '20',
    'sports': '21',
    'geography': '22',
    'history': '23',
    'politics': '24',
    'art': '25',
    'celebrities': '26',
    'animals': '27',
    'vehicles': '28',
    'entertainment_comics': '29',
}

def check_question_db(question, check="all"):
    # Check if a question is already in the database
    # check = 'all': will check the entire quesiton string
    # check = 'part': will just check half the question string
    boto3.setup_default_session(region_name='ap-southeast-2')
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(DYNAMO_DB)
    if check == 'all':
        response = table.query(
            IndexName = 'question-index',
            KeyConditionExpression=Key('question').eq(question)
            )
        count = response['Count']
    else:
        half_question = ' '.join(question.split()[len(question.split()) // 2:])
        response = table.scan(
            FilterExpression=Attr('question').contains(half_question)
            )
        count = response['Count']
    return count


def get_question_api(category, difficulty):
    # Get a single question from the trivia API
    # Check the first half or the question to see if its alrady in the datbase before returning it.
    # Returns a dictionary with category, type, difficulty, question, correct_answer, incorrect_answer
    url = "https://opentdb.com/api.php"
    params = {
        'amount': '10',
        'category': cat_map[category],
        'type': 'multiple',
        'difficulty': difficulty
    }
    found_question = False
    while found_question == False:
        all_questions = json.loads(requests.get(url, params=params).text)['results']
        for q in all_questions:
            q_check = check_question_db(q['question'], check="part")
            if q_check == False:
                return_question = q
                found_question = True
            else:
                print(f'question already added - {q}')
    # The returned category text contains a space, so this is overwritter with values used in the database
    return_question['category'] = category
    return return_question

def add_question(question):
    # Adds a question to DynamoDB 
    # First check that the question is not already in the database
    q_check = check_question_db(question['question'], check="all")
    if q_check == True:
        print('question alreeady exists')
        return {'response': 'already_exists'}
    boto3.setup_default_session(region_name='ap-southeast-2')
    client = boto3.client('dynamodb')
    client.put_item(
        TableName=DYNAMO_DB,
        Item={
            'id': {
                'S': str(randint(100000000000,999999999999))
            },
            'question': {
                'S': question['question']
            },
            'correct_answer': {
                'S': question['correct_answer']
            },
            'incorrect_answer_1': {
                'S': question['incorrect_answer_1']
            },
            'incorrect_answer_2': {
                'S': question['incorrect_answer_2']
            },
            'incorrect_answer_3': {
                'S': question['incorrect_answer_3']
            },
            'difficulty': {
                'S': question['difficulty']
            },
            'category': {
                'S': question['category']
            },
            'date': {
                'S': question['date']
            },
        }
    )
    return 'question_added'