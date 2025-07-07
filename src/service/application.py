from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select, and_
from sqlalchemy.orm import joinedload

from src.service import BasicCrud
from sharq_models.models import (
    Application,
    PassportData,
    StudyInfo,
    StudyDirection,
    StudyLanguage,
    StudyForm,
)
from src.schemas.application import ApplicationBase, ApplicationFilter


class ApplicationCrud(BasicCrud[Application, ApplicationBase]):
    def __init__(self, db: AsyncSession):
        super().__init__(db)

    async def get_application_with_nested_info(self, application_id: int):
        stmt = (
            select(Application)
            .options(
                joinedload(Application.passport_data),
                joinedload(Application.study_info).joinedload(StudyInfo.study_form),
                joinedload(Application.study_info).joinedload(StudyInfo.study_language),
                joinedload(Application.study_info).joinedload(
                    StudyInfo.study_direction
                ),
            )
            .where(Application.id == application_id)
        )

        result = await self.db.execute(stmt)
        application = result.scalars().first()

        if not application:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Application not found"
            )

        return application

    async def get_all_application_with_nested_info(
        self, filter_data: ApplicationFilter, limit: int = 10, offset: int = 0
    ):
        stmt = select(Application).options(
            joinedload(Application.passport_data),
            joinedload(Application.study_info).joinedload(StudyInfo.study_form),
            joinedload(Application.study_info).joinedload(StudyInfo.study_language),
            joinedload(Application.study_info).joinedload(StudyInfo.study_direction),
        )

        filters = []

        # PassportData filters
        if filter_data.passport_series_number:
            filters.append(
                Application.passport_data.has(
                    PassportData.passport_series_number
                    == filter_data.passport_series_number
                )
            )
        if filter_data.issue_date:
            filters.append(
                Application.passport_data.has(
                    PassportData.issue_date == filter_data.issue_date
                )
            )
        if filter_data.issuing_authority:
            filters.append(
                Application.passport_data.has(
                    PassportData.issuing_authority == filter_data.issuing_authority
                )
            )
        if filter_data.authority_code:
            filters.append(
                Application.passport_data.has(
                    PassportData.authority_code == filter_data.authority_code
                )
            )
        if filter_data.place_of_birth:
            filters.append(
                Application.passport_data.has(
                    PassportData.place_of_birth == filter_data.place_of_birth
                )
            )
        if filter_data.date_of_birth:
            filters.append(
                Application.passport_data.has(
                    PassportData.date_of_birth == filter_data.date_of_birth
                )
            )
        if filter_data.gender:
            filters.append(
                Application.passport_data.has(PassportData.gender == filter_data.gender)
            )
        if filter_data.nationality:
            filters.append(
                Application.passport_data.has(
                    PassportData.nationality == filter_data.nationality
                )
            )

        # StudyInfo filters
        if filter_data.study_direction_name:
            filters.append(
                Application.study_info.has(
                    StudyInfo.study_direction.has(
                        StudyDirection.name == filter_data.study_direction_name
                    )
                )
            )
        if filter_data.study_form_name:
            filters.append(
                Application.study_info.has(
                    StudyInfo.study_form.has(
                        StudyForm.name == filter_data.study_form_name
                    )
                )
            )
        if filter_data.study_language_name:
            filters.append(
                Application.study_info.has(
                    StudyInfo.study_language.has(
                        StudyLanguage.name == filter_data.study_language_name
                    )
                )
            )

        if filters:
            stmt = stmt.where(and_(*filters))

        stmt = stmt.limit(limit).offset(offset)

        result = await self.db.execute(stmt)
        return result.scalars().all()

    async def delete_application(self, application_id: int):
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
