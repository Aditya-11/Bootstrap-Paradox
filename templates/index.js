import {table, render} from './components/dataTable'

console.log('loaded js')
// console.log(sum)
// console.log(render)
// console.log(table)
// let table1 = table;
// let render1 = render;
// let sum1 = console.log(sum);

let addClass = (node, classname) => {
    if(!(classname in node.classList))
        node.classList.add(classname);
}


let ip = 'localhost:5000';
// y[0].options[y[0].selectedIndex].text
let inputContainer = document.getElementsByClassName('container')[0];
let body = document.getElementsByTagName('body')[0];
console.log(body);
let tableNodes;

let submit = document.getElementById('submit');
submit.addEventListener('click', async () => {
    addClass(inputContainer, 'anime');
    
    let price = document.getElementsByClassName('form-control')[0].value;
    let p1 = document.getElementsByClassName('custom-select')[0].value;
    let p2 = document.getElementsByClassName('custom-select')[1].value;
    let url = `http://${ip}/query/?price${price}=&p1=${p1}&p2=${p2}`;
    console.log(url);
    // tableNodes = document.getElementsByClassName('dtable');
    // if(tableNodes) {
    //     tableNodes.forEach(element => {
    //         element.remove();
    //     });
    // }
    // let data = await fetch(url).then((res) => res.text());
    // console.log(data);
    let myRegex = table.replace(/^th>.*$/m, '');
    console.log(myRegex);
    let dtable = document.createElement('div');
    body.appendChild(dtable);
    dtable.classList.add('dtable');
    // render(data, dtable);
    render(myRegex, dtable); 
    // body.appendChild()
});