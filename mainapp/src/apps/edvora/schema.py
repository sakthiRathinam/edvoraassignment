from uuid import UUID
from pydantic import BaseModel
from typing import List, Optional



class LoginSchema(BaseModel):
    username:str
    password:str