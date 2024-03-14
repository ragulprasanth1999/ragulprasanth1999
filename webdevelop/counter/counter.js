const dec = document.getElementById("b2");
const inc = document.getElementById("b1");
const res = document.getElementById("b3");
const counter = document.getElementById("counter");
let count = 1;
inc.onclick = function(){
    count +=1
    counter.textContent = count;
}
dec.onclick = function(){
    count -=1
    counter.textContent = count;
}
res.onclick = function(){
    count = 0
    counter.textContent = count;
}