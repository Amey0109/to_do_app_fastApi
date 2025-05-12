from fastapi import APIRouter, status, Depends, HTTPException
from .. import schemas, models
from ..database import get_db
from sqlalchemy.orm import Session
from ..hashing import Hash
from ..oauth2 import get_current_user

router= APIRouter(
    prefix='/my_app',
    tags=['User']
)

@router.post('/user', status_code=status.HTTP_201_CREATED)
def create_user(request: schemas.User, db: Session= Depends(get_db), current_user:schemas.User = Depends(get_current_user)):
    new_user= models.User(username= request.username, password= Hash.bcrypt(request.password), phone_number=request.phone_number)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user

@router.get('/user', status_code= status.HTTP_200_OK)
def show_user(db: Session= Depends(get_db), current_user:schemas.User = Depends(get_current_user)):
    user= db.query(models.User).filter(models.User.id==current_user.id).first()
    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f'No available user of id {id}')
    return user

@router.put('/user', status_code=status.HTTP_204_NO_CONTENT)
def update_user(request: schemas.User, db: Session= Depends(get_db), current_user:schemas.User = Depends(get_current_user)):
    user=db.query(models.User).filter(models.User.id==current_user.id) # Updating specific login user by fetching its id

    # Storing Hash password in DB after update
    if request.password:
        hashed_password = Hash.bcrypt(request.password)
        request.password = hashed_password

    
    user.update(request.model_dump())
    db.commit()