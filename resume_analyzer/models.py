from pydantic import BaseModel,Field,field_validator

class CandidateEducationModel(BaseModel):
    degree : str = Field(min_length = 1)
    university:str = Field(min_length = 1)
    year_of_passing:int = Field(ge=0)
    percentage: float|None = None

class CandidateModel(BaseModel):
    name:str = Field(min_length=1, description="Name must be a non-empty string")

    #custom validation
    @field_validator('name')
    @classmethod
    def name_must_be_non_empty(cls,value):
        value = value.strip()
        if not value:
            raise ValueError("Name must be non empty")
        return value    


    experience:int = Field(ge=0, description="Years of experience must be a non-negative integer")
    skills:list[str] = Field(min_length=1, description="Skills must be a non-empty list of strings")
    education : CandidateEducationModel

class CandidateEvaluationResultModel(BaseModel):
    name:str
    experience:int
    matching_skills:set[str]
    missing_skills:set[str]
    experience_passed:bool
    matching_score:float = Field(ge=0, le=100, description="Matching score must be between 0 and 100")
    education : str




 