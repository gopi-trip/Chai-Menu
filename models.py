from pydantic import BaseModel

class MenuItem(BaseModel):
    id:int
    name:str
    category:str
    price:int
    description:str
    available:bool

class MenuResponse(BaseModel):
    status:str = "Success"
    count: int
    items: list[MenuItem]
