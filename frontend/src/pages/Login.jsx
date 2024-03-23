import React, { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import LoginHandler from '../auth/LoginHandler'

const Login = () => {
    const [phone, setPhone] = useState("")
    const [password, setPassword] = useState("")
    const [isLoggedIn, setIsLoggedIn] = useState(false)

    const navigate = useNavigate()

    useEffect(() => {
        console.log(phone);
    }, [phone])

    useEffect(() => {
        setIsLoggedIn(true)
    }, [isLoggedIn])

    const loginHandler = (e) => {
        e.preventDefault()

        const { error } = LoginHandler(phone, password)

        if (error) {
            alert(error)
        } else {
            navigate('/login-otp')
            // resetForm()
        }
    }

    return (
        <>
            <form onSubmit={loginHandler}>
                <label>
                    Phone
                </label>
                <input type="number" name='phone' className='input' value={phone} onChange={(e) => setPhone(e.target.value)} />
                <br />
                <br />
                <label>
                    Password
                </label>
                <input type="password" name='password' value={password} onChange={(e) => setPassword(e.target.value)} />
                <br />
                <br />
                <button type="submit">
                    Login
                </button>
            </form>
        </>
    )
}

export default Login 