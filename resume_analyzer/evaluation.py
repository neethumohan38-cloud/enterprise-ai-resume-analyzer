from resume_analyzer.models import CandidateEvaluationResultModel,CandidateModel

class Evaluation():
    #constructor
    def __init__(self,candidate:CandidateModel,required_skills:list[str],min_experience:int)->None:
          self.candidate = candidate
          self.required_skills = required_skills
          self.min_experience = min_experience


    def candidate_evaluation(self)-> CandidateEvaluationResultModel:

            #normalize the inputs by converting to lower
            required_skills_normalized = self.normalizedskills(self.required_skills)
            candidate_skills_normalized = self.normalizedskills(self.candidate.skills)
        
            #find intersection
            matching_skills = required_skills_normalized & candidate_skills_normalized
            #find missing
            missing_skills = required_skills_normalized - candidate_skills_normalized
        
            #calculate matching_score
            matching_score = self.calculate_matching_score(matching_skills,required_skills_normalized)
        
            #check experience meet?
            experience_check = self.candidate.experience>= self.min_experience
            
        
            return CandidateEvaluationResultModel (
                name = self.candidate.name,
                experience = self.candidate.experience,
                matching_skills = matching_skills,
                missing_skills = missing_skills,
                matching_score = matching_score,
                experience_passed = experience_check,
                education=self.candidate.education.degree
            )

    def normalizedskills(self,skills:list[str])->set[str]:
          return {skill.lower() for skill in skills}
    
    def calculate_matching_score(self,matching_skills:list[str],
                                 normalized_required_skills:list[str])->float:
          if(len(normalized_required_skills) > 0):
            return (len(matching_skills)/len(normalized_required_skills))*100
          else:
            return 0
          
            



    