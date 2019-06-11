import uvicorn
from src.app import application


if __name__ == "__main__":
    uvicorn.run(application, debug=True, host="0.0.0.0", port=8585)
