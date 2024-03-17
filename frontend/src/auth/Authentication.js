import axios from 'axios'
import rootURL from '../constants/urlConstants'

const APICall = axios.create({
    baseURL: rootURL,
    timeout: 5000,

    headers: {
        "Content-Type": "application/json",
        Accept: "application/json"
    }
})


export default APICall