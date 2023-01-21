allToasts = document.getElementsByClassName('custom-toast')

for(let i = 0; i< allToasts.length; i++){
    allToasts[i].addEventListener('click', (evnt) => {
        evnt.target.remove()
    })
}