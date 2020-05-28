const showButton = document.querySelector('.show-api')
const apiSection = document.querySelector('.get-api')

showButton.addEventListener('click', function(){
    apiSection.classList.remove("hide")
})

const categories = [
        'general_knowledge',
        'entertainment_books',
        'entertainment_film',
        'entertainment_music',
        'entertainment_misicals',
        'entertainment_telivision',
        'entertainment_video_games',
        'entertainment_board_games',
        'science_nature',
        'science_computers',
        'science_mathematics',
        'mythology',
        'sports',
        'geography',
        'history',
        'politics',
        'art',
        'celebrities',
        'animals',
        'vehicles',
        'entertainment_comics']

const categorySelect = document.querySelectorAll('.category')


for (i=0; i < categorySelect.length; i++){
    categories.forEach(function(item){
        let opt = item
        let el = document.createElement("option")
        el.text = opt
        el.value = opt
        el2 = el.cloneNode(true)
        categorySelect[i].appendChild(el)
    })
}


const questionField = document.querySelector('.question')
const correctAnswer = document.querySelector('.correct_answer')
const incorrectAnswer1 = document.querySelector('.incorrect_answer_1')
const incorrectAnswer2 = document.querySelector('.incorrect_answer_2')
const incorrectAnswer3 = document.querySelector('.incorrect_answer_3')
const difficultyField = document.querySelector('.difficulty')
const categoryField = document.querySelector('.category')

const fillQuestion = function(data){
    questionField.value = data.question
    correctAnswer.value = data.correct_answer
    difficultyField.value = data.difficulty
    categoryField.value = data.category
    incorrectAnswer1.value = data.incorrect_answers[0]
    incorrectAnswer2.value = data.incorrect_answers[1]
    incorrectAnswer3.value = data.incorrect_answers[2]
}

const dateField = document.querySelector('.date-input')


if (typeof questionData !== 'undefined'){
    fillQuestion(questionData)
    dateField.value = '1990-01-01'
} else {
    let today = new Date()
    dateField.value = today.toISOString().split('T')[0]
}

