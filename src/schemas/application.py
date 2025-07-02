from pydantic import BaseModel
from .passport_data import PassportDataResponse
from .study_info import StudyInfoResponse


class ApplicationBase(BaseModel):
    study_info_id: int
    passport_data_id: int



class ApplicationResponse(ApplicationBase):
    id: int
    study_info: StudyInfoResponse
    passport_data : PassportDataResponse
