let showButton = document.querySelector('.show-api')
let apiSection = document.querySelector('.get-api')

showButton.addEventListener('click', function(){
    apiSection.classList.remove("hide")
})