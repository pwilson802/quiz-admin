import requests
import json

cat_map = {
    'general_knowledge': '9'

}

def get_question(category, difficulty="medium"):
    url = "https://opentdb.com/api.php"
    params = {
        'amount': '10',
        'category': cat_map[category],
        'type': 'multiple',
        'difficulty': 'easy'
    }
    all_questions = json.loads(requests.get(url, params=params).text)['results']
    return_question = all_questions[0]
    return return_question