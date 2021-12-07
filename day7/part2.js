const fs = require('fs');

fs.readFile('input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }
    let crabs = data.split(",").map(Number);
    let maxPos = Math.max(...crabs);
    let fuelPerPosition = new Array(maxPos).fill(0);
    for (const crabPos of crabs) {
        for (let pos = 0; pos < maxPos; pos++) {
            let distance = Math.abs(crabPos - pos);
            for (let j = 1; j < distance + 1; j++) {
                fuelPerPosition[pos] += j;
            }
        }
    }
    minFuel = 0
    optimalPos = 0;
    for (let pos = 0; pos < fuelPerPosition.length; pos++) {
        if (pos == 0) {
            minFuel = fuelPerPosition[pos];
            optimalPos = pos;
        }
        else if (fuelPerPosition[pos] < minFuel) {
            minFuel = fuelPerPosition[pos];
            optimalPos = pos;
        }
    }
    console.log("Position: " + optimalPos + " Fuel: " + minFuel);
})
