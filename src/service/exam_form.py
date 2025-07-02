from fastapi import HTTPException, status
from src.service import BasicCrud
from src.models import ExamForm
from src.schemas.exam_form import (
    ExamFormBase,
    ExamFormUpdate,
    ExamFormFilter,
    ExamFormResponse,
)
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


class ExamFormCrud(BasicCrud[ExamForm, ExamFormBase]):
    def __init__(self, db: AsyncSession):
        super().__init__(db)

    async def create_exam_form(self, obj: ExamFormBase) -> ExamFormResponse:
        existing = await super().get_by_field(
            model=ExamForm,
            field_name="name",
            field_value=obj.name,
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Bunday imtihon shakli allaqachon mavjud",
            )

        return await super().create(model=ExamForm, obj_items=obj)

    async def get_by_exam_form_id(self, form_id: int) -> ExamFormResponse:
        exam_form = await super().get_by_id(model=ExamForm, item_id=form_id)

        if not exam_form:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Imtihon shakli topilmadi"
            )

        return exam_form

    async def get_exam_form_all(
        self,
        filter_obj: ExamFormFilter,
        limit: int = 100,
        offset: int = 0
    ) -> List[ExamFormResponse]:
        filters = []

        if filter_obj.name:
            filters.append(ExamForm.name.ilike(f"%{filter_obj.name}%"))

        return await super().get_all(
            model=ExamForm,
            limit=limit,
            offset=offset,
            filters=filters or None
        )

    async def update_exam_form(self, form_id: int, obj: ExamFormUpdate) -> ExamFormResponse:
        await self.get_by_exam_form_id(form_id)
        return await super().update(model=ExamForm, item_id=form_id, obj_items=obj)

    async def delete_exam_form(self, form_id: int) -> dict:
        await self.get_by_exam_form_id(form_id)
        return await super().delete(model=ExamForm, item_id=form_id)
