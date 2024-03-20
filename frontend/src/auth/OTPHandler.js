import APICall from '../utils/APICall';

const OTPHandler = async (otp) => {
    try {
        const { data, status } = await APICall.post("user/token/otp/", { otp })

        if (status === 200) {
            console.log('accepted!');
            localStorage.setItem("access", data.tokens.access)
            localStorage.setItem("refresh", data.tokens.refresh)
        }

    } catch (error) {
        console.log(error);
    }
}

export default OTPHandler