from pydantic import BaseModel

class StudyInfoBase(BaseModel):
    study_language_id: int
    study_form_id: int
    study_direction_id: int
    exam_form_id: int



class StudyInfoCreate(StudyInfoBase):
    user_id: int



class StudyInfoUpdate(BaseModel):
    study_language_id: int | None = None
    study_form_id: int | None = None
    study_direction_id: int | None = None
    exam_form_id: int | None = None



class StudyInfoFilter(BaseModel):
    study_language: int | None = None
    study_form: int | None = None
    study_direction: int | None = None
    exam_form: int | None = None


class StudyInfoResponse(BaseModel):
    id: int
    user_id: int
    study_language: str
    study_form: str
    study_direction: str
    exam_form: str


