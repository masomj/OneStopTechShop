const readEditBtn = document.getElementById('readonly_edit')
readEditBtn.addEventListener('click', function(){
    event.preventDefault()
    let elements = document.getElementsByClassName('form-control profile-edit');
    for (let i = 0; i < elements.length; i++){
        elements[i].removeAttribute('readonly');
        console.log(elements[i]);
    }
    document.getElementById('readonly_edit').classList.add('d-none');
    document.getElementById('submit').classList.remove('d-none');
}
);


