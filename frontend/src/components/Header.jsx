import React from 'react'
import { BrowserRouter as Routers, Routes, Route, NavLink } from 'react-router-dom'
import Home from '../pages/Home'
import Login from '../pages/Login'
import LoginOTP from '../pages/LoginOTP'

function Header() {
    return (
        <div>
            <Routers>
                <NavLink to="/">Home</NavLink>
                <NavLink to="/login">Login</NavLink>
                <Routes>
                    <Route path='/' element={<Home />} />
                    <Route path='/login' element={<Login />} />
                    <Route path='/login-otp' element={<LoginOTP />} />
                </Routes>
            </Routers>
        </div>
    )
}

export default Header
