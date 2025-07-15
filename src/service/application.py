from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from sqlalchemy.orm import joinedload

from src.service import BasicCrud
from sharq_models.models import (  # type: ignore
    Application,
    StudyInfo,
    StudyDirection,
)
from src.schemas.application import (
    ApplicationBase,
    ApplicationResponse,
)


class ApplicationCrud(BasicCrud[Application, ApplicationBase]):
    def __init__(self, db: AsyncSession):
        super().__init__(db)

    async def get_application_by_application_id(self, application_id: int) -> ApplicationResponse:
        stmt = (
            select(Application)
            .options(
                joinedload(Application.passport_data),
                joinedload(Application.study_info).joinedload(StudyInfo.study_form),
                joinedload(Application.study_info).joinedload(StudyInfo.study_language),
                joinedload(Application.study_info).joinedload(StudyInfo.study_type),
                joinedload(Application.study_info).joinedload(StudyInfo.education_type),
                joinedload(Application.study_info)
                    .joinedload(StudyInfo.study_direction)
                    .joinedload(StudyDirection.study_type),
                joinedload(Application.study_info)
                    .joinedload(StudyInfo.study_direction)
                    .joinedload(StudyDirection.education_type),
                joinedload(Application.study_info)
                    .joinedload(StudyInfo.study_direction)
                    .joinedload(StudyDirection.study_language),  
            )
            .where(Application.id == application_id)
        )

        result = await self.db.execute(stmt)
        application = result.scalars().first()

        if not application:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Application topilmadi"
            )

        return ApplicationResponse.model_validate(application, from_attributes=True)

    async def get_all_application_with_nested_info(
        self, limit: int = 10, offset: int = 0
    ) -> list[ApplicationResponse]:
        stmt = (
            select(Application)
            .options(
                joinedload(Application.passport_data),
                joinedload(Application.study_info).joinedload(StudyInfo.study_form),
                joinedload(Application.study_info).joinedload(StudyInfo.study_language),
                joinedload(Application.study_info).joinedload(StudyInfo.study_type),
                joinedload(Application.study_info).joinedload(StudyInfo.education_type),
                joinedload(Application.study_info)
                    .joinedload(StudyInfo.study_direction)
                    .joinedload(StudyDirection.study_type),
                joinedload(Application.study_info)
                    .joinedload(StudyInfo.study_direction)
                    .joinedload(StudyDirection.education_type),
                joinedload(Application.study_info)
                    .joinedload(StudyInfo.study_direction)
                    .joinedload(StudyDirection.study_language),  
            )
            .limit(limit)
            .offset(offset)
        )

        result = await self.db.execute(stmt)
        applications = result.scalars().all()

        return [
            ApplicationResponse.model_validate(app, from_attributes=True)
            for app in applications
        ]

    async def delete_application(self, application_id: int) -> dict:
        stmt = select(Application).where(Application.id == application_id)
        result = await self.db.execute(stmt)
        application = result.scalars().first()

        if not application:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Ariza topilmadi yoki sizga tegishli emas",
            )

        await self.db.delete(application)
        await self.db.commit()
        return {"detail": "Ariza muvaffaqiyatli o'chirildi"}
