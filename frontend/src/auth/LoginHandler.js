import React from 'react'
import APICall from '../utils/APICall';
import jwt_decode from 'jwt-decode'
// import { json } from 'react-router-dom';

const LoginHandler = async (phone, password) => {
    try {
        const { data, status } = await APICall.post("user/token/",
            { phone, password }
        )

        if (status === 200) {
            localStorage.setItem('access', data.tokens.access);
            localStorage.setItem('refresh', data.tokens.refresh);
            console.log("accepted!");
            const refreshToken = data.tokens.refresh;
            const accessToken = data.tokens.access;
            console.log(accessToken, refreshToken);
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
