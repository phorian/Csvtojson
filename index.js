const csvtojson = require('csvtojson')
const fs = require('fs')

const csvfilepath = "HNGi9CSV.csv"

csvtojson()
    .fromFile(csvfilepath)
    .then((json) => {
        console.log(json)

        fs.writeFileSync("Output.json", JSON.stringify(json), "utf-8", (err) => {
            if(err) console.log(err)
        })
    
        fs.appendFile('Output.json', 'HASH: c837ee57adf906d2efe7e1bdd7154c6f4e9df98d0256e1e34ebecf37f464fd72', (error) => {
            if(error) console.log(error);
            console.log('hash updated')
        })
    })