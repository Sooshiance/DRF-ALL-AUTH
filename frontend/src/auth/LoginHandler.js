import React from 'react'
import { APICall } from '../utils/APICall'

export const LoginHandler = async (phone, password) => {
    try {
        const { data, status } = await APICall.post("user/token/",
            { phone, password }
        )

        if (status === 200) {
            console.log("accepted!");
            console.log(data.access);
            console.log(data.refresh);
        }
        return { data, error: null }
    } catch (error) {
        console.log(error)
        return {
            data: null,
            error: "something went wrong!"
        };
    }
}

export default LoginHandler
