let readEditBtn = document.getElementById('readonly_edit')

readEditBtn.addEventListener('click', function(){
event.preventDefault()
document.getElementById('postcode').removeAttribute('readonly')
document.getElementById('street').removeAttribute('readonly')
document.getElementById('city').removeAttribute('readonly')
document.getElementById('number').removeAttribute('readonly')
document.getElementById('readonly_edit').classList.add('d-none')
document.getElementById('submit').classList.remove('d-none')
}
);
