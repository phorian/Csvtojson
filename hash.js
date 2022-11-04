const crypto = require('crypto')
const fs = require('fs')

const data = fs.readFileSync("./Output.json");

const hash = crypto.createHash('sha256')
const fhex = hash.update(data).digest('hex')

console.log(fhex)

module.exports = fhex