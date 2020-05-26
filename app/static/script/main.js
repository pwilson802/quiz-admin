let showButton = document.querySelector('.show-api')
let apiSection = document.querySelector('.get-api')

showButton.addEventListener('click', function(){
    apiSection.classList.remove("hide")
})

console.log(questionData)

const questionField = document.querySelector('.question')
const correctAnswer = document.querySelector('.correct_answer')
const 