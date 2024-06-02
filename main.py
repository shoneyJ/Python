import asyncio
import uvicorn
from fastapi import  FastAPI, Request, Response
from sqlalchemy.orm import Session

import models
from database import SessionLocal, engine
from routers import users

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router)


@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# Dependency



# @app.get("/items/", response_model=list[schemas.Item])
# def read_items(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
#     items = crud.get_items(db, skip=skip, limit=limit)
#     return items

async def main():
    config = uvicorn.Config("main:app",host="0.0.0.0", port=8083, log_level="info")
    server = uvicorn.Server(config)
    await server.serve()

if __name__ == "__main__":
    asyncio.run(main())
    
