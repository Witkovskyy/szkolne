document.addEventListener("DOMContentLoaded", () => {

    const date = new Date;

    const day = date.getDate();  
    const month = date.getMonth() + 1;  
    const year = date.getFullYear();
    const hours = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();

    const formattedDate = `${month}/${day}/${year} ${hours}:${minutes}:${seconds}`;

    const date_p = document.querySelector('#current-date');
    date_p.innerHTML += formattedDate;
})


const submit = document.querySelector('#submit');
const newElement=document.createElement('p');
document.querySelector('form').appendChild(newElement);

submit.addEventListener('click', (e)=> {
    e.preventDefault();
    const pierwsza_waluta = document.querySelector('#waluta-z').value;
    const druga_waluta = document.querySelector('#waluta-po').value;
    const ilosc = document.querySelector('#ilosc').value;
    const kursy = [0.23, 4.42];
    //console.log(pierwsza_waluta);
    //console.log(druga_waluta);
    //console.log(ilosc);
    if(pierwsza_waluta ==="eur" && 
        druga_waluta!='' && 
        druga_waluta!=pierwsza_waluta)
        {
            let wynik = (ilosc *  kursy[1]).toFixed(2);
            newElement.innerHTML = wynik + " Pln";
    }
    else if(pierwsza_waluta ==="pln" && 
        druga_waluta!='' && 
        druga_waluta!=pierwsza_waluta)
        {
            let wynik = (ilosc *  kursy[0]).toFixed(2);
            newElement.innerHTML = wynik + " Euro";
    }
    else 
        {
            alert("Wybierz dwie różne waluty");
            newElement.innerHTML = "";
    }
})