from time import sleep
from fastapi import APIRouter
from getsessionid import kernel

router = APIRouter()

@router.get('/reg')
def mainfunc():
    kernel()
    
    sleep(2)
    
    return {'status':200, 'msg': 'completed'}