from fastapi import APIRouter, Depends, Security
from src.utils.auth import get_current_user
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated, List
from sharq_models.models import User
from src.service.study_form import StudyFormCrud
from src.schemas.study_form import (
    StudyFormBase,
    StudyFormUpdate,
    StudyFormResponse,
    StudyFormFilter,
)
from src.core.db import get_db

study_form_router = APIRouter(prefix="/study_form", tags=["Study Form"])


def get_service_crud(db: AsyncSession = Depends(get_db)):
    return StudyFormCrud(db)


@study_form_router.post("/create", response_model=StudyFormResponse)
async def create_study_form(
    item: StudyFormBase,
    service: Annotated[StudyFormCrud, Depends(get_service_crud)],
    current_user: Annotated[User, Security(get_current_user, scopes=["admin"])],
):
    return await service.create_study_form(obj=item)


@study_form_router.get("/get_by_id/{form_id}", response_model=StudyFormResponse)
async def get_by_study_form_id(
    form_id: int,
    service: Annotated[StudyFormCrud, Depends(get_service_crud)],
    current_user: Annotated[User, Security(get_current_user, scopes=["admin"])],
):
    return await service.get_by_study_form_id(form_id=form_id)


@study_form_router.get("/get_all", response_model=List[StudyFormResponse])
async def get_all_study_forms(
    current_user: Annotated[User, Security(get_current_user, scopes=["admin"])],
    service: Annotated[StudyFormCrud, Depends(get_service_crud)],
    filter_items: StudyFormFilter = Depends(),
    limit: int = 20,
    offset: int = 0,
):
    return await service.get_study_form_all(
        filter_obj=filter_items,
        limit=limit,
        offset=offset,
    )


@study_form_router.put("/update/{form_id}", response_model=StudyFormResponse)
async def update_study_form(
    form_id: int,
    update_data: StudyFormUpdate,
    service: Annotated[StudyFormCrud, Depends(get_service_crud)],
    current_user: Annotated[User, Security(get_current_user, scopes=["admin"])],
):
    return await service.update_study_form(
        form_id=form_id,
        obj=update_data,
    )


@study_form_router.delete("/delete/{form_id}")
async def delete_study_form(
    form_id: int,
    current_user: Annotated[User, Security(get_current_user, scopes=["admin"])],
    service: Annotated[StudyFormCrud, Depends(get_service_crud)],
):
    return await service.delete_study_form(form_id=form_id)
