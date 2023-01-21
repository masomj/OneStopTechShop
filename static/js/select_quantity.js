incrementBtn = document.getElementById('increment-qty');
decrementBtn = document.getElementById('decrement-qty');
function handleIncrement(evnt){
    evnt.preventDefault();
    qty = parseInt(document.getElementById('id-qty').value);
    qty++;
    handleValueChange(qty);
}

function handleDecrement(evnt){
    evnt.preventDefault();
    qty = parseInt(document.getElementById('id-qty').value);
    --qty;
    handleValueChange(qty);
}

function handleValueChange(qty){
    if (qty >= 1 && qty <= 99){
        document.getElementById('id-qty').value = qty;
    } else{
        evnt.target.disabled=true;
    } 
}

incrementBtn.addEventListener('click',handleIncrement);
decrementBtn.addEventListener('click',handleDecrement);

