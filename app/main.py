import uvicorn
import logging
from fastapi import FastAPI, Request
from pathlib import Path
from .api import users
from .services.custom_logging import CustomizeLogger

logger = logging.getLogger(__name__)


def create_app() -> FastAPI:
    app = FastAPI(title='CustomLogger', debug=False)
    logger = CustomizeLogger.make_logger()
    app.logger = logger
    return app


app = create_app()
app.include_router(users.router, tags=["users"])

@app.get('/')
def customize_logger(request: Request):
    request.app.logger.info("We are Ready")
    return {'data': "Successfully Implemented Custom Log"}

@app.on_event("startup")
def startup_event():
    app.logger.info("Event Start Up")
    

if __name__ == '__main__':
      uvicorn.run(app, port=8000)