function updateDate() {
    const date = new Date;
    const day = date.getDate();  
    const month = date.getMonth() + 1;  
    const year = date.getFullYear();
    const hours = date.getHours();
    const minutes = date.getMinutes();
    const seconds = date.getSeconds();
  
    const formattedDate = `${month}/${day}/${year} ${hours}:${minutes}:${seconds}`;
  
    const date_p = document.querySelector('#current-date');
    date_p.innerHTML = formattedDate;
}
  
updateDate();
setInterval(updateDate,1000);