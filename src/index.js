console.log('loaded js')

let addClass = (node, classname) => {
    if(!(classname in body.classList))
        body.classList.add(classname);
}


let ip = '0.0.0.0:8000';
// y[0].options[y[0].selectedIndex].text
let body = document.getElementsByClassName('container')[0];

let submit = document.getElementById('submit');
submit.addEventListener('click', () => {
    addClass(body, 'anime');
    let price = document.getElementsByClassName('form-control')[0].value;
    let p1 = document.getElementsByClassName('custom-select')[0].value;
    let p2 = document.getElementsByClassName('custom-select')[1].value;
    let url = `${ip}/query/?price${price}=&p1=${p1}&p2=${p2}`;
    console.log(url);
    // fetch(url).then((res) => res.)
});