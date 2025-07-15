from fastapi import HTTPException, status
from src.service import BasicCrud
from sqlalchemy import select 
from sqlalchemy.orm import joinedload
from sharq_models.models import StudyDirection  #type: ignore
from src.schemas.study_direction import (
    StudyDirectionBase,
    StudyDirectionUpdate,
    StudyDirectionResponse,
)
from sqlalchemy.ext.asyncio import AsyncSession
from typing import List


class StudyDirectionCrud(BasicCrud[StudyDirection, StudyDirectionBase]):
    def __init__(self, db: AsyncSession):
        super().__init__(db)

    async def create_study_direction(
        self, obj: StudyDirectionBase
    ) -> StudyDirectionResponse:
        existing = await super().get_by_field(
            model=StudyDirection,
            field_name="study_code",
            field_value=obj.study_code,
        )
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Bunday fan mavjud",
            )

        return await super().create(model=StudyDirection, obj_items=obj)

    async def get_by_study_direction_id(
        self,
        direction_id: int,
    ) -> StudyDirectionResponse:
        stmt = (
            select(StudyDirection)
            .options(
                joinedload(StudyDirection.study_form),
                joinedload(StudyDirection.study_language),
                joinedload(StudyDirection.study_type),
                joinedload(StudyDirection.education_type),
            )
            .where(StudyDirection.id == direction_id)
        )

        result = await self.db.execute(stmt)
        direction_data = result.scalars().first()  

        if not direction_data:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Yo'nalish topilmadi"
            )

        return StudyDirectionResponse.model_validate(direction_data)

    async def get_study_direction_all(
        self, limit: int = 100, offset: int = 0
    ) -> List[StudyDirectionResponse]:
        stmt = (
            select(StudyDirection)
            .options(
                joinedload(StudyDirection.study_form),
                joinedload(StudyDirection.study_language),
                joinedload(StudyDirection.study_type),
                joinedload(StudyDirection.education_type),
            )
            .limit(limit)
            .offset(offset)
        )
        result = await self.db.execute(stmt)
        direction_data = result.scalars().all()

        return [
            StudyDirectionResponse.model_validate(item, from_attributes=True)
            for item in direction_data
        ]
        

    async def update_study_direction(
        self, direction_id: int, obj: StudyDirectionUpdate
    ) -> StudyDirectionResponse:
        await self.get_by_study_direction_id(direction_id)  
        await super().update(model=StudyDirection, item_id=direction_id, obj_items=obj)
        return await self.get_by_study_direction_id(direction_id)

    async def delete_study_direction(self, direction_id: int) -> dict:
        await self.get_by_study_direction_id(direction_id)
        return await super().delete(model=StudyDirection, item_id=direction_id)
