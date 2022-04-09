let data = JSON.parse(document.getElementById("jsonData").getAttribute("data-json"))

const calcHealth = () => {
    return ((data.level - 1) * 20 + 100)
}

const calcMana = () => {
    return ((data.level - 1) * 10 + 50)
}

if(data.page === "charInfo") {
    document.getElementById("health").innerText = `Health: ${calcHealth()}`
    document.getElementById("mana").innerText = `Mana: ${calcHealth()}`
    document.getElementById("exp").value = data.exp
    document.getElementById("exp").max = data.expReq
}

console.log(data)