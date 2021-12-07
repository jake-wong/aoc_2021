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
            fuelPerPosition[pos] += Math.abs(crabPos - pos);
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
