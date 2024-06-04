from fastapi import APIRouter, Depends, HTTPException
import models, schemas,crud
from database import SessionLocal, engine
from sqlalchemy.orm import Session
from dependencies import get_token_header, get_db
# from abstractCrud import CrudFactory
from models import Blog
models.Base.metadata.create_all(bind=engine)

# blogCrud = CrudFactory(Blog)

router = APIRouter(
    prefix="/blogs",
    dependencies=[Depends(get_db)],
    responses={404: {"Blogs": "Not found"}}
)


@router.post("/", response_model=schemas.Blog)
def create(blog: schemas.BlogCreate, db: Session = Depends(get_db)):
    return crud.create_blog(db,blog)
    
