import requests
import json

cat_map = {
    'general_knowledge': '9',
    'entertainment_books': '10',
    'entertainment_film': '11',
    'entertainment_music': '12',
    'entertainment_misicals': '13',
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

def check_question_db():
    pass
    # TODO - CHeck if a question is already added to dynamodb

def get_question(category, difficulty="medium"):
    # Get a single question from the trivia API
    # Returns a dictionary with category, type, difficulty, question, correct_answer, incorrect_answer
    url = "https://opentdb.com/api.php"
    params = {
        'amount': '10',
        'category': cat_map[category],
        'type': 'multiple',
        'difficulty': difficulty
    }
    all_questions = json.loads(requests.get(url, params=params).text)['results']
    return_question = all_questions[0]
    return_question['category'] = category
    return return_question

