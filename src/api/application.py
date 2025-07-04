from fastapi import APIRouter, Depends, Query , Security
from typing import Annotated
from src.utils import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from src.service.application import ApplicationCrud
from src.schemas.application import (
    ApplicationFilter,
    ApplicationResponse
)
from sharq_models.models import User
from sharq_models.db import get_db

application_router = APIRouter(
    prefix="/application",
    tags=["Application"]
)


def get_service_crud(db: AsyncSession = Depends(get_db)):
    return ApplicationCrud(db)


@application_router.get("/get_by_id/{applicationd_id}", response_model=ApplicationResponse)
async def get_application_by_id(
    applicationd_id: int,
    service: Annotated[ApplicationCrud, Depends(get_service_crud)],
    current_user: Annotated[User , Security(get_current_user , scopes=["admin"])]
):
    return await service.get_application_with_nested_info(application_id=applicationd_id)
     



@application_router.get("/get_all/",response_model=list[ApplicationResponse])
async def get_all_applications(
    current_user: Annotated[User , Security(get_current_user , scopes=["admin"])],
    service: Annotated[ApplicationCrud, Depends(get_service_crud)],
    filter_data: ApplicationFilter = Depends(),
    limit: int = Query(10, ge=1),
    offset: int = Query(0, ge=0),

):
    return await service.get_all_application_with_nested_info(
        filter_data=filter_data,
        limit=limit,
        offset=offset
    )


@application_router.delete("/delete/{application_id}")
async def delete_application(
    service: Annotated[ApplicationCrud, Depends(get_service_crud)],
    application_id: int ,
    current_user: Annotated[User , Security(get_current_user , scopes=["admin"])]

):
    return await service.delete_application(application_id=application_id)
