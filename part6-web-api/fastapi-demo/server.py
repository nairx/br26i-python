from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def home():
    return JSONResponse(status_code=200,content={"message":"Hello World"})

@app.get("/services")
def home():
    return JSONResponse(status_code=200,content={"message":"Service"})


@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id":user_id}


#/products?limit=10&search=iphone
@app.get("/products")
def get_products(limit:int=10,search:str|None=None):
    return {"limit":limit,"search":search}

from pydantic import BaseModel

class Product(BaseModel):
    name:str
    price:float
    in_stock:bool=True

@app.post("/products")
def create_product(product:Product):
    print(product.name)
    return {"message":"Product Created","product":product}



# @app.post("/products")
# async def create_product(product:Product):
#     #user = await #db crud
#     print(product.name)
#     return {"message":"Product Created","product":product}


