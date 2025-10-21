import os
from pathlib import Path 
from dotenv import load_dotenv
from fastapi import APIRouter
from models import User

ENV_PATH = Path(__file__).parent / '.env'

load_dotenv(ENV_PATH)

router = APIRouter(prefix='/user', tags=['유저'])

@router.get('')
def get_user():
    pass

@router.post('')
def create_user():
    pass
