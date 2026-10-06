from fastapi import FastAPI, Query, HTTPException
from models import MenuItem, MenuResponse
from data import menu_items

app = FastAPI(
    title="Chai-Menu API",
    description=(
        "Read-only menu API for Kiosk/App displays"
    ),
)

@app.get("/")
def root():
    return {
        "Message":"Welcome to the Chai-Menu API"
    }

@app.get("/menu",response_model=MenuResponse)
def get_menu(category:str | None = Query(None,description="Filter by chai, snack or combo")):
    if category:
        filtered = [item for item in menu_items if item["category"] == category.lower()]

        if not filtered:
            raise HTTPException(status_code=404, detail=f"No Item found in the category: {category}")

        return MenuResponse(count=len(filtered),items=filtered)

    return MenuResponse(count=len(menu_items),items=menu_items)


@app.get("/menu/{item_id}",response_model=MenuItem)
def get_item_by_id(item_id:int):
    for item in menu_items:
        if(item["id"] == item_id):
            return item
    raise HTTPException(status_code=404,detail=f"No item found with the id: {item_id}")
