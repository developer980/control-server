from django.core.mail import send_mail

import json
import jwt
import random

def genetate_otp_code(user_id, user_email):
    key = "secret"
    otp_code = random.randint(100000, 999999)
    token = jwt.encode({"id":user_id, "otp_code":otp_code}, key, algorithm="HS256")
    
    send_mail("Your OTP Code", 
        f"Your OTP code is: {otp_code}",
        "tudordin2002@gmail.com",
        [user_email], 
        fail_silently=False,
    )

    return token

def otp_verify(request):
    body = json.loads(request.body)
    input_otp = body.get("otp")
    token = request.COOKIES.get("verification_token")

    print("token", token)

    if not token:
        return {"status": "error", "message": "Verification token not found."}

    key = "secret"
    try:
        decoded_token = jwt.decode(token, key, algorithms=["HS256"])
    except jwt.ExpiredSignatureError:
        print("decoded_token", decoded_token)
        return {"status": "error", "message": "Verification token has expired."}
    except jwt.InvalidTokenError:
        print("decoded_token", decoded_token)
        return {"status": "error", "message": "Invalid verification token."}

    if str(decoded_token.get("otp_code")) != str(input_otp):
        print("decoded_token", decoded_token)
        return {"status": "error", "message": "Invalid OTP code."}
    
    return {"status": "ok", "message": "OTP verified successfully.", "decoded_token": decoded_token}