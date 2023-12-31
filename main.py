import uvicorn
from fastapi import FastAPI
from handlers import router

def get_application() -> FastAPI:
    application = FastAPI()
    application.include_router(router)
    return application

app = get_application()

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port="8080", log_level="info")