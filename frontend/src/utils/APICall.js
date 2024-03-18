import axios from 'axios'

const APICall = axios.create({
    baseURL: "http://127.0.0.1:8000/api/",
    timeout: 5000,

    headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
    }
})


export default APICall