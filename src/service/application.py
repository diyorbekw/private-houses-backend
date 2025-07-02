from fastapi import HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select

from src.service import BasicCrud
from src.models import Application, PassportData, StudyInfo
from src.schemas.application import ApplicationBase, ApplicationResponse
from src.schemas.passport_data import PassportDataResponse
from src.schemas.study_info import StudyInfoResponse


class ApplicationCrud(BasicCrud[Application, ApplicationBase]):
    def __init__(self, db: AsyncSession):
        super().__init__(db)

    async def application_creation(self, user_id: int) -> ApplicationResponse:
        passport_data = await super().get_by_field(
            model=PassportData, field_name="user_id", field_value=user_id
        )
        study_info = await super().get_by_field(
            model=StudyInfo, field_name="user_id", field_value=user_id
        )

        if not passport_data or not study_info:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Passport yoki Ta'lim ma'lumotlari topilmadi"
            )

        stmt = select(Application).where(
            Application.passport_data_id == passport_data.id,
            Application.study_info_id == study_info.id
        )
        result = await self.db.execute(stmt)
        existing = result.scalar_one_or_none()
        if existing:
            raise HTTPException(
                status_code=status.HTTP_409_CONFLICT,
                detail="Bu foydalanuvchi uchun ariza allaqachon mavjud"
            )

        # Create application
        application_data = ApplicationBase(
            passport_data_id=passport_data.id,
            study_info_id=study_info.id
        )
        application = await super().create(model=Application, obj_items=application_data)

        # Return full response
        return ApplicationResponse(
            id=application.id,
            passport_data_id=passport_data.id,
            study_info_id=study_info.id,
            passport_data=PassportDataResponse.model_validate(passport_data),
            study_info=StudyInfoResponse.model_validate(study_info)
        )
    
    async def get_by_id_application(self , application_id: int, user_id: int):
        stmt = select(Application)
        return
