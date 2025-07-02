from pydantic import BaseModel

class StudyFormBase(BaseModel):
    name: str

class StudyFormResponse(StudyFormBase):
    id: int

class StudyFormFilter(BaseModel):
    name: str | None = None

class StudyFormUpdate(BaseModel):
    name: str | None = None


