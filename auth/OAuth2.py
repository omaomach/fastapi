from fastapi.security import OAuth2PasswordBearer

OAuth2_schema = OAuth2PasswordBearer(tokenUrl='token')