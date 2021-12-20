from tortoise import fields, models, Tortoise, run_async
from tortoise.contrib.pydantic import pydantic_model_creator
from enum import Enum, IntEnum
from typing import List
from tortoise.exceptions import NoValuesFetched
from tortoise.models import Model
from tortoise.signals import post_delete, post_save, pre_delete, pre_save


    
class BroadCastUser(models.Model):
    username = fields.CharField(max_length=400, index=True,unique=True)
    password = fields.CharField(max_length=100)
    created = fields.DatetimeField(auto_now_add=True)
    updated = fields.DatetimeField(auto_now=True)
    active = fields.BooleanField(default=False)
    
