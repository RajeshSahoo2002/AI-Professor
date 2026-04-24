import bcrypt

#BELOW FUNCTION HASH_PASSWORD IS USED TO RETURN A SECURE,HASH PASSWORD BY TAKING THE PLAIN-PASSWORD AS THE INPUT SO THAT THE HASHED PASSWORD CAN BE STORED IN THE DB AND DURING THE AUTHENTICATION PROCESS THE USER CAN PROVIDE THE PLAIN-PASSWORD AND IT CAN BE CHECKED WITH THE HASHED PASSWORD STORED IN THE DB USING THE BELOW FUNCTION VERIFY_PASSWORD
def hash_password(plain_password: str) -> str:
	# This function is used to hash the password using the bycrypt package
    hashed=bcrypt.hashpw(plain_password.encode('utf-8'),bcrypt.gensalt())
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # This function checks if the plain password is same as of the hashed_password which will be used by the user during authentication process
	return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    