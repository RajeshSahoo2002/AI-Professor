import bcrypt

#BELOW FUNCTION HASH_PASSWORD IS USED TO RETURN A SECUREC,HASH PASSWORD BY TAKING THE PLAIN-PASSWORD AS THE INPUT SO THAT IT CAN BE REPLACED WITH THE ORIGINAL ONE
def hash_password(plain_password: str) -> str:
	# This function is used to hash the password using the bycrypt package
    hashed=bcrypt.hashpw(plain_password.encode('utf-8'),bcrypt.gensalt())
    return hashed.decode('utf-8')


def verify_password(plain_password: str, hashed_password: str) -> bool:
    # This function checks if the plain password is same as of the hashed_password which will be used by the user during authentication process
	return bcrypt.checkpw(plain_password.encode('utf-8'), hashed_password.encode('utf-8'))
    
    