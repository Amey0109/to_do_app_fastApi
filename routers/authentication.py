from fastapi import APIRouter, Depends, HTTPException, status
from .. import schemas, database, models, token
from ..hashing import Hash
from sqlalchemy.orm import Session
from fastapi.security import OAuth2PasswordRequestForm


router= APIRouter(
    prefix='/login',
    tags=['Authentication']
)

@router.post('/')
def login(request: OAuth2PasswordRequestForm = Depends() , db: Session = Depends(database.get_db)):
    user= db.query(models.User).filter(models.User.username== request.username).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Credentails')
    
    if not Hash.verify(user.password, request.password):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'Invalid Password')
    
    #generate a JWT token 
    access_token = token.create_access_token(
        data={"sub": user.username}
    )
    return {'access_token':access_token, 'token_type': "bearer"}
