from fastapi import FastAPI

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

