
document.addEventListener('DOMContentLoaded', function(){
    const button1 = document.getElementById('myButton');
    const title = document.getElementsByClassName('first-text')[0];

    function logEvent(event){
        console.log("Event type: " + event.type);
    }

    function changeButtonText(event){
        event.target.textContent = 'Are you sure you?';
    }

    function changeButtonTextDefault(event){
        event.target.textContent = 'Click Title with Log';
    }

    function removeElement(event){
        if(event.key == 'Backspace')
        {
            const nextParagraph = document.getElementsByTagName('p')[0];
            document.body.removeChild(nextParagraph)
        }
    }    

    button1.addEventListener('click', logEvent);
    button1.addEventListener('mouseover', changeButtonText);
    button1.addEventListener('mouseout', changeButtonTextDefault);

    title.addEventListener('click', changeButtonText);

    document.addEventListener('keydown', logEvent);
    document.addEventListener('keydown', removeElement);
});

function showAlert(){
    const title = document.getElementsByClassName('first-text')[0];

    title.textContent = 'Uncle Scrooge is the richest duck in the world!';
    title.outerHTML = '<h6 class="first-text">Uncle Scrooge is the richest duck in the world!</h6>';

    console.log(title);
}

function changeLink(){
    const link = document.getElementById('link');
    link.href = 'https://en.wikipedia.org/wiki/Scrooge_McDuck';
    link.textContent = 'click this link to learn more about Uncle Scrooge';
}

function doNotClick(){
    const snake = document.getElementsByTagName('img');
    for(let i = 0; i < snake.length; i++){
        snake[i].src = '../images/Snake.jpg';
        snake[i].alt = 'Snakes attacked';
    }
}