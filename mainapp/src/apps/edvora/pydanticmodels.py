from src.apps.edvora.models import BroadCastUser
from tortoise.contrib.pydantic import pydantic_model_creator

CREATE_USER = pydantic_model_creator(
    BroadCastUser, name="FeedUserCreate", exclude=("created","updated",'id','active'))
GET_USER = pydantic_model_creator(
    BroadCastUser, name="FeedUserGet")
