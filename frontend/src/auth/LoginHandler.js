import React from 'react'
import APICall from '../utils/APICall';

const LoginHandler = async (phone, password) => {
    try {
        const { data, status } = await APICall.post("user/token/",
            { phone, password }
        )

        if (status === 200) {
            alert('enter the otp!')
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
