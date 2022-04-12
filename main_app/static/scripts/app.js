let data = JSON.parse(document.getElementById("jsonData").getAttribute("data-json"))

const calcHealth = () => {
    return ((data.level - 1) * 20 + 100)
}

const calcMana = () => {
    return ((data.level - 1) * 10 + 50)
}

const calcAttack = () => {
    return ((data.level - 1) * 3 + 7)
}

if(data.page === "charInfo") {
    document.getElementById("health").innerText = `Health: ${calcHealth()}`
    document.getElementById("mana").innerText = `Mana: ${calcMana()}`
    document.getElementById("attack").innerText = `Attack: ${calcAttack()}`
}

if(data.page === "battle") {
    const player = document.getElementById("player").innerText
    const monster = document.getElementById("monster").innerText
    let playerHP = calcHealth()
    let playerMP = calcMana()
    let playerAttack = calcAttack()
    document.getElementById("playerHealth").max = calcHealth()
    document.getElementById("playerMana").max = calcMana()
    let monsterHP = document.getElementById("monsterHealth").max
    let monsterMP = document.getElementById("monsterMana").max
    const log = document.getElementById("combatLog")
    let turn = true

    const refresh = () => {
        document.getElementById("playerHealth").value = playerHP
        document.getElementById("playerMana").value = playerMP
        document.getElementById("monsterHealth").value = monsterHP
        document.getElementById("monsterMana").value = monsterMP
    }

    refresh()

    const monsterAttack = () => {
        playerHP -= 10
        let p = document.createElement("p")
        log.append(`${monster} attacks ${player} and deals ${10} damage!`, p)
        refresh()
        turn = true
    }

    const attack = () => {
        if(turn) {
            turn = false
            monsterHP -= playerAttack
            let p = document.createElement("p")
            log.append(`${player} attacks ${monster} and deals ${playerAttack} damage!`, p)
            refresh()
            setTimeout(() => { monsterAttack()}, 700)
        }
    }

    document.getElementById("attack").addEventListener("click", () => {
        attack()
    })

}

console.log(data)