// Select color input
const colour = document.querySelector("#colorPicker");
// Select size input
const height = document.querySelector("#inputHeight");
const width = document.querySelector("#inputWidth");

// When size is submitted by the user, call makeGrid()
const form = document.querySelector("#sizePicker");
form.addEventListener('submit', function(event){
    event.preventDefault();
    makeGrid();
});

function makeGrid() {

// Your code goes here!
const tbl = document.querySelector("#pixelCanvas");
tbl.innerHTML = '';

for (let i = 0; i < height.value; i++) {
    const row = t.insertRow();
    for (let f = 0; f < width.value; f++) {
            const col = row.insertCell(f);

            col.addEventListener('click', function(event){
                event.currentTarget.style.backgroundColor = colour.value;
            });

            col.addEventListener('dblclick', function(event){
                event.currentTarget.style.backgroundColor = '';
            });

        }
    }
}