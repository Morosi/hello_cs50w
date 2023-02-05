let countEl = document.getElementById("count-el")

let count = -1

function increment(){
    count += 1
    countEl.innerText = count
}


increment()

function save(){
    let saveEl = document.getElementById("save-el")
    let entryNum = saveEl.childElementCount + 1
    saveEl.textContent += count + "  " +  " - "
    
    console.log(count)
}

