let data = JSON.parse(document.getElementById("jsonData").getAttribute("data-json"))

if(data.page === "battle") {
    const player = document.getElementById("player").innerText
    const monster = document.getElementById("monster").innerText
    let playerHP = document.getElementById("playerHealth").max
    let playerMP = document.getElementById("playerMana").max
    let playerAttack = data.charAttack
    let monsterHP = document.getElementById("monsterHealth").max
    let monsterMP = document.getElementById("monsterMana").max
    let monsterAttack = data.monAttack
    const log = document.getElementById("combatLog")
    let turn = true

    const refresh = () => {
        document.getElementById("playerHealth").value = playerHP
        document.getElementById("playerMana").value = playerMP
        document.getElementById("monsterHealth").value = monsterHP
        document.getElementById("monsterMana").value = monsterMP
    }

    const monsterTurn = () => {
        if(monsterHP > 0) {
            playerHP -= monsterAttack
            let p = document.createElement("p")
            log.append(`${monster} attacks ${player} and deals ${monsterAttack} damage!`, p)
            p.scrollIntoView()
            refresh()
            if(playerHP > 0) {
                turn = true
            } else {
                document.getElementById("defeat").style.display = "block"
            }
        } else {
            document.getElementById("victory").style.display = "block"
        }
    }

    const attack = () => {
        if(turn && playerHP > 0 && monsterHP > 0) {
            turn = false
            monsterHP -= playerAttack
            let p = document.createElement("p")
            log.append(`${player} attacks ${monster} and deals ${playerAttack} damage!`, p)
            p.scrollIntoView()
            refresh()
            setTimeout(() => { monsterTurn()}, 700)
        }
    }

    document.getElementById("attack").addEventListener("click", () => {
        attack()
    })
}