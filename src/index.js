import {table, render} from './components/dataTable'

console.log('loaded js');


let addClass = (node, classname) => {
    if(!(classname in node.classList))
        node.classList.add(classname);
}


// let ip = 'localhost:5000';
let ip = '192.168.43.193:5000';
// y[0].options[y[0].selectedIndex].text
let inputContainer = document.getElementsByClassName('container')[0];
let body = document.getElementsByTagName('body')[0];
console.log(body);
let tableNodes = 0;


let submit = document.getElementById('submit');
submit.addEventListener('click', async () => {
    addClass(inputContainer, 'anime');
    
    let price = document.getElementsByClassName('custom-select')[0].value;
    let p1 = document.getElementsByClassName('custom-select')[1].value;
    // let p2 = document.getElementsByClassName('custom-select')[2].value;
    // let optiNo;
    // if(p1=='' || p2=='')
    //     optiNo = 1;
    // else
    //     optiNo = 2;
    
    // let url = `http://${ip}/query/?optiNo=${optiNo}&price=${price}&p1=${p1}&p2=${p2}`;
    let url = `http://${ip}/query/?&price=${price}&p1=${p1}`;
    console.log(url);
    tableNodes = document.getElementsByClassName('dtable');
    if(tableNodes) {
        [...tableNodes].forEach(element => {
            element.remove();
        });
    }
    let data = await fetch(url).then((res) => res.text());
    console.log(data);
    // let myRegex = table.replace(/^<th>/, '');
    // console.log(myRegex);
    let dtable = document.createElement('div');
    body.appendChild(dtable);
    dtable.classList.add('dtable');
    render(data, dtable);
    let t = document.getElementsByTagName('table')[0];
    t.classList.add('table');
    t.classList.add('table-borderless');
    t.classList.add('table-striped');
    t.classList.add('table-hover'); 
    let th = document.getElementsByTagName('thead')[0];
    th.classList.add('thead-dark');



    // render(myRegex, dtable);
});