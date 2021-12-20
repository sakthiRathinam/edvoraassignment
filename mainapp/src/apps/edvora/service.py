from pydantic import BaseModel, conint
from fastapi_pagination import Params
from typing import TypeVar, Generic, Sequence
from fastapi_pagination.bases import AbstractPage, AbstractParams
from typing import TypeVar, Type, Optional, Union
from fastapi import Request, Response
from fastapi import HTTPException
from pydantic import BaseModel
from tortoise.models import Model
from .pydanticmodels import *
from tortoise import models
from fastapi_pagination.ext.tortoise import paginate
from tortoise.queryset import QuerySet
from .auth import verify_password,get_password_hash


ModelType = TypeVar("ModelType", bound=models.Model)
CreateSchemaType = TypeVar("CreateSchemaType", bound=BaseModel)
UpdateSchemaType = TypeVar("UpdateSchemaType", bound=BaseModel)
GetSchemaType = TypeVar("GetSchemaType", bound=BaseModel)
QuerySchemaType = TypeVar("QuerySchemaType", bound=BaseModel)


class BaseService:
    model: Type[ModelType]
    create_schema: CreateSchemaType
    update_schema: UpdateSchemaType
    query_schema: QuerySchemaType
    get_schema: GetSchemaType

    async def user_create(self, user: CREATE_USER):
        user_dict = user.dict()
        user_dict['active'] = True
        hashed_password = get_password_hash(user_dict.pop('password'))
        return await self.model.create(**user_dict,password=hashed_password)
    async def create(self, schema, *args, **kwargs) -> Optional[CreateSchemaType]:
        obj = await self.model.create(**schema.dict(exclude_unset=True), **kwargs)
        return await self.get_schema.from_tortoise_orm(obj)

    async def update(self, schema, **kwargs) -> Optional[UpdateSchemaType]:
        await self.model.filter(**kwargs).update(**schema.dict(exclude_unset=True))
        return await self.get_schema.from_queryset_single(self.model.get(**kwargs))

    async def update_extra(self, id, schema, **kwargs) -> Optional[UpdateSchemaType]:
        obj = await self.model.get(id=id).update(**schema.dict(exclude_unset=True), **kwargs)
        return obj

    async def delete(self, **kwargs):
        obj = await self.model.filter(**kwargs).delete()
        if not obj:
            raise HTTPException(
                status_code=404, detail='Object does not exist')

    async def all(self) -> Optional[GetSchemaType]:
        return await self.get_schema.from_queryset(self.model.all())

    async def filter(self, **kwargs) -> Optional[GetSchemaType]:
        return await self.get_schema.from_queryset(self.model.filter(**kwargs))

    async def get(self, **kwargs) -> Optional[GetSchemaType]:
        return await self.get_schema.from_queryset_single(self.model.get(**kwargs))

    async def get_obj(self, **kwargs) -> Optional[ModelType]:
        return await self.model.get_or_none(**kwargs)
    async def authenticate(self,username:str,password:str):
        user = await self.model.get(username=username)
        if not verify_password(password,user.password):
            return False
        return True
    async def get_or_create(self, **kwargs) -> Optional[ModelType]:
        return await self.model.get_or_create(**kwargs)

    async def paginate_data(query: QuerySet):
        if not isinstance(query, QuerySet):
            query = await query.all()
        paginated_data = await paginate(query)
        print(request.query_params)
        extra = {'previous': False, "next": True}
        if request.query_params['page'] != str(1):
            extra['previous'] = True
        if (int(request.query_params['page']) * int(request.query_params['size']))+1 > paginated_data.total:
            extra['next'] = False
        data = {**paginated_data.dict(), **extra}
        return data

    async def limited_data(self, offset, limit, **kwargs) -> Optional[ModelType]:
        toReturn = {
            'total': None,
            'prev': False,
            'next': True,
            'data': None,
        }
        print(kwargs)
        toReturn['total'] = await self.model.filter(**kwargs).count()
        if offset+limit+1 > toReturn['total']:
            toReturn['next'] = False
        if offset != 0:
            toReturn['prev'] = True
        toReturn['data'] = await self.model.filter(**kwargs).offset(offset).limit(limit)
        return toReturn


class FeedUserViewSet(BaseService):
    model = BroadCastUser
    get_schema = GET_USER


broadcast_user = FeedUserViewSet()