from pydantic import BaseModel, ConfigDict
from .study_form import StudyFormResponse
from .study_type import StudyTypeResponse
from .study_language import StudyLanguageResponse
from .education_type import EducationTypeResponse



class StudyDirectionBase(BaseModel):
    name: str 
    exam_title: str 
    
    education_years: int
    contract_sum: float 
    study_code: str 
    
    study_form_id: int
    study_type_id: int
    study_language_id: int
    education_type_id: int


class StudyDirectionResponse(BaseModel):
    id: int
    name: str 
    exam_title: str 
    
    education_years: int
    contract_sum: float 
    study_code: str 
    
    study_form: StudyFormResponse
    study_type: StudyTypeResponse
    study_language: StudyLanguageResponse
    education_type: EducationTypeResponse
    
    
    model_config = ConfigDict(from_attributes=True)


class StudyDirectionUpdate(BaseModel):
    name: str  | None = None
    exam_title: str  | None = None
    
    education_years: int | None = None
    contract_sum: float  | None = None
    study_code: str  | None = None
    
    study_form_id: int | None = None
    study_type_id: int | None = None
    study_language_id: int | None = None
    education_type_id: int  | None = None






