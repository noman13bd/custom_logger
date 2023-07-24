from fastapi import APIRouter, Request

router = APIRouter(prefix="/users")

@router.get("/")
def get_users(request: Request):
    request.app.logger.info("Users ALL")
    return {'all': True}