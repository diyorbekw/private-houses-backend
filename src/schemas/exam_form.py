from pydantic import BaseModel

class ExamFormBase(BaseModel):
    name: str

class ExamFormResponse(ExamFormBase):
    id: int

class ExamFormFilter(BaseModel):
    name: str | None = None

class ExamFormUpdate(BaseModel):
    name: str | None = None


