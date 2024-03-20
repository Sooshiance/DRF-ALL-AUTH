import { useState, useEffect } from 'react'
import { useNavigate } from 'react-router-dom'
import OTPHandler from '../auth/OTPHandler'

const LoginOTP = () => {
    const [otp, setOTP] = useState("")
    const navigate = useNavigate()

    useEffect(() => {
        console.log(otp);
    }, [otp])

    const OtpHandler = (e) => {

        const { error } = OTPHandler(otp)

        if (error) {
            alert(error)
        }
        else {
            return navigate('/')
        }

        e.preventDefault()
    }
    return (
        <>
            <form onSubmit={OtpHandler}>
                <label htmlFor="otp">
                    OTP
                </label>
                <input type="number" id='otp' placeholder='Enter the six characters recieved' name="otp" className='input' value={otp} onChange={(e) => { setOTP(e.target.value) }} />
                <button type="submit">
                    Send OTP
                </button>
            </form>
        </>
    )
}

export default LoginOTP