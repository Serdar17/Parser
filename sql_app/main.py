from fastapi import Depends, FastAPI, HTTPException, Response
from sqlalchemy.orm import Session
from fastapi.responses import FileResponse
from typing import List

from . import crud_utils, models, schemas
from .database import SessionLocal, engine
from .background_task import periodic
import asyncio
from .generate_image import generate_image

models.Base.metadata.create_all(bind=engine)

app = FastAPI()


# Dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.on_event("startup")
async def schedule_periodic():
    loop = asyncio.get_event_loop()
    loop.create_task(periodic())


@app.post("/product/", response_model=schemas.ProductCreate)
def create_product(product: schemas.ProductCreate, db: Session = Depends(get_db)):
    product_exists = crud_utils.get_product_by_name(db, name=product.name)
    if product_exists and product_exists.price == product.price:
        raise HTTPException(status_code=400, detail=f"Product with this name=\'{product.name}\' already exists")
    return crud_utils.create_product(db=db, product=product)


@app.get("/products/", response_model=List[schemas.Product])
def read_products(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    products = crud_utils.get_products(db, skip=skip, limit=limit)
    return products


@app.get("/product/{product_id}", response_model=schemas.Product)
def read_product_by_id(product_id: int, db: Session = Depends(get_db)):
    db_product = crud_utils.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail=f"Product with id=\'{product_id}\' not found")
    return db_product


@app.get("/product/get-product-by-name/{product_name}", response_model=schemas.Product)
def read_product_by_name(product_name: str, db: Session = Depends(get_db)):
    db_product = crud_utils.get_product_by_name(db, name=product_name)
    if db_product is None:
        raise HTTPException(status_code=404, detail=f"Product with name=\'{product_name}\' not found")
    return db_product


@app.put("/product/{product_id}", response_model=schemas.Product)
def update_product(product_id: int, product: schemas.ProductUpdate, db: Session = Depends(get_db)):
    db_product = crud_utils.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail=f"Product with id=\'{product_id}\' not found")
    return crud_utils.update_product(db, product=product, product_id=product_id)


@app.delete("/product/{product_id}", response_model=dict)
def delete_product(product_id: int, db: Session = Depends(get_db)):
    db_product = crud_utils.get_product_by_id(db, product_id=product_id)
    if db_product is None:
        raise HTTPException(status_code=404, detail=f"Product with id=\'{product_id}\' not found")
    crud_utils.delete_product(db, product_id=product_id)

    return {
        "status": "ok",
        "message": "Deletion was successful"
    }


@app.get("/product/get-statistics/{product_name}",
         responses={
             200: {
                 "content": {"image/png": {}}
             }
         },
         response_class=Response
         )
def get_statistics_by_product_name(product_name: str, db: Session = Depends(get_db)):
    db_product = crud_utils.get_product_by_name(db, name=product_name)
    if db_product is None:
        raise HTTPException(status_code=404, detail=f"Product with id=\'{product_name}\' not found")
    generate_image(db, product_name=product_name)
    return FileResponse("sql_app/images/statistics.png")
