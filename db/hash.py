import bcrypt

class Hash:
    @staticmethod
    def bcrypt(password: str) -> str:
        # Convert the string password to bytes
        pwd_bytes = password.encode('utf-8')
        # Generate a salt and hash the password
        salt = bcrypt.gensalt()
        hashed = bcrypt.hashpw(pwd_bytes, salt)
        # Convert back to a string for database storage
        return hashed.decode('utf-8')
    
    @staticmethod
    def verify(hashed_password: str, plain_password: str) -> bool:
        # Convert both strings back to bytes to compare them safely
        return bcrypt.checkpw(
            plain_password.encode('utf-8'), 
            hashed_password.encode('utf-8')
        )
