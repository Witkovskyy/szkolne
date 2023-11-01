const baseUrl = 'http://api.nbp.pl/api/exchangerates/rates/a/';

//tworzenie paragrafu na wynik
const newElement = document.createElement('p');
newElement.classList.add('result');
const form = document.querySelector('form');
form.appendChild(newElement);

//funckja z submita
form.addEventListener('submit', async (e) => {
  e.preventDefault();

  //dane
  const first_currency = document.querySelector('#currency-before').value;
  const second_currency = document.querySelector('#currency-after').value;
  const amount = parseFloat(document.querySelector('#amount').value);

  //obliczenia
  if (first_currency === 'eur' && second_currency !== '' && second_currency !== first_currency) {
      const apiUrl = baseUrl + 'eur';
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        const currency = data.rates[0].mid;
        let wynik = (amount * currency).toFixed(2);
        newElement.innerHTML = wynik + ' PLN';
      } 
      catch (error) {
        console.error('There was a problem with the fetch operation:', error);
      }
  } else if (first_currency === 'pln' && second_currency !== '' && second_currency !== first_currency) {
      const apiUrl = baseUrl + 'eur';
      try {
        const response = await fetch(apiUrl);
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        const data = await response.json();
        const currency = data.rates[0].mid;
        let wynik = (amount / currency).toFixed(2);
        newElement.innerHTML = wynik + ' EUR';
      } 
      catch (error) {
        console.error('There was a problem with the fetch operation:', error);
      }
  } else {
      alert('Pick two different currencies');
      newElement.innerHTML = '';
  }
});

