# Import FastAPI and necessary packages
from fastapi import FastAPI,Query
import uvicorn
import logging
# Initialize FastAPI app
app = FastAPI()

@app.get("/")
async def index() -> dict:
    """
    Index route to check if the API is working.
    Returns:
        dict: The status of the API.
    """
    logging.info("Index is working")
    return {
        "Status": True,
        "message": "API is working.."
    }

@app.post("/welcome")
async def welcome_message(
    name: str = Query(..., description="Enter your name"),
    surname: str = Query(..., description="Enter your surname")
) -> dict:
    
    return {
        "message":f"Hello {name} {surname}"
    }

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8800)
