from pydantic import BaseModel,Field

class Candidate(BaseModel):
    name:str
    experience:int = Field(ge = 0)
    skills:list[str]  
class CandidateEvaluationResult(BaseModel):
    name:str
    experience:int
    matching_skills:set[str]
    missing_skills:set[str]
    experience_passed:bool
