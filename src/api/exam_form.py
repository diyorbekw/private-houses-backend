from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession
from typing import Annotated, List

from src.service.exam_form import ExamFormCrud
from src.schemas.exam_form import (
    ExamFormBase,
    ExamFormUpdate,
    ExamFormResponse,
    ExamFormFilter,
)
from src.db.session import get_db

exam_form_router = APIRouter(
    prefix="/exam_form",
    tags=["Exam Form"]
)


def get_service_crud(db: AsyncSession = Depends(get_db)):
    return ExamFormCrud(db)


@exam_form_router.post("/create", response_model=ExamFormResponse)
async def create_exam_form(
    item: ExamFormBase,
    service: Annotated[ExamFormCrud, Depends(get_service_crud)],
):
    return await service.create_exam_form(obj=item)


@exam_form_router.get("/get_by_id/{form_id}", response_model=ExamFormResponse)
async def get_by_exam_form_id(
    form_id: int,
    service: Annotated[ExamFormCrud, Depends(get_service_crud)],
):
    return await service.get_by_exam_form_id(form_id=form_id)


@exam_form_router.get("/get_all", response_model=List[ExamFormResponse])
async def get_all_exam_forms(
    service: Annotated[ExamFormCrud, Depends(get_service_crud)],
    filter_items: ExamFormFilter = Depends(),
    limit: int = 20,
    offset: int = 0,
):
    return await service.get_exam_form_all(
        filter_obj=filter_items,
        limit=limit,
        offset=offset,
    )


@exam_form_router.put("/update/{form_id}", response_model=ExamFormResponse)
async def update_exam_form(
    form_id: int,
    update_data: ExamFormUpdate,
    service: Annotated[ExamFormCrud, Depends(get_service_crud)],
):
    return await service.update_exam_form(
        form_id=form_id,
        obj=update_data,
    )


@exam_form_router.delete("/delete/{form_id}")
async def delete_exam_form(
    form_id: int,
    service: Annotated[ExamFormCrud, Depends(get_service_crud)],
):
    return await service.delete_exam_form(form_id=form_id)
