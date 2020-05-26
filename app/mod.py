import requests
import json

cat_map = {
    'general_knowledge': '9'

}

def check_question_db():
    # TODO - CHeck if a question is already added to dynamodb

def get_question(category, difficulty="medium"):
    # Get a single question from the trivia API
    # Returns a dictionary with category, type, difficulty, question, correct_answer, incorrect_answer
    url = "https://opentdb.com/api.php"
    params = {
        'amount': '10',
        'category': cat_map[category],
        'type': 'multiple',
        'difficulty': 'easy'
    }
    all_questions = json.loads(requests.get(url, params=params).text)['results']
    return_question = all_questions[0]
    return_question['category'] = category
    return return_question

