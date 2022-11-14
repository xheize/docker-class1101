import express from 'express'
import * as dotenv from 'dotenv'

dotenv.config()

const app = express()
const port = process.env.port

app.listen( port, () => {
    console.log(`This Server Running 5000 Port Number`)
})


app.get('/', (res, req) => {
    res.status(200).json({"heartBeat": True})
})

app.post('/', (res, req) => {
    res.status(200).json({"heartBeat": True})   
})