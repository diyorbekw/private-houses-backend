from pydantic import BaseModel

class StudyLanguageBase(BaseModel):
    name: str

class StudyLanguageResponse(StudyLanguageBase):
    id: int

class StudyLanguageFilter(BaseModel):
    name: str | None = None

class StudyLanguageUpdate(BaseModel):
    name: str | None = None


