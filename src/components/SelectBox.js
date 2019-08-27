import '@vaadin/vaadin-select';

let select = 
`<vaadin-select>
<template>
    <vaadin-item>Supplier rating</vaadin-item>
    <vaadin-item>Component performance</vaadin-item>
</template>
</vaadin-select>`

let render = (template, node) => {
    if(!node)
        return;
    node.innerHTML = template
}

module.exports = select;