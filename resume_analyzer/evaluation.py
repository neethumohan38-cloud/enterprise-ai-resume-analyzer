from resume_analyzer.models import CandidateEvaluationResult,Candidate

def candidate_evaluation(candidate:Candidate,
                         required_skills:list[str],
                         min_experience:int)-> CandidateEvaluationResult:

    #raise
    if(candidate["experience"]<0):
        raise ValueError("Experience cant be negative")
    if(len(candidate["skills"]) == 0):
        raise ValueError("Candidate should have atleast one skill!")

    #normalize the inputs by converting to lower
    required_skills_normalized = {skill.lower() 
                                  for skill in required_skills}
    candidate_skills_normalized = {skill.lower() 
                                   for skill in candidate['skills']}

    #find intersection
    matching_skills = required_skills_normalized & candidate_skills_normalized
    #find missing
    missing_skills = required_skills_normalized - candidate_skills_normalized

    #calculate matching_score
    if(len(required_skills_normalized) > 0):
        matching_score = (len(matching_skills)/len(required_skills_normalized))*100
    else:
        matching_score = 0

    #check experience meet?
    experience_check = candidate['experience']>= min_experience
    

    return{
        "name" : candidate["name"],
        "experience" : candidate["experience"],
        "matching_skills" : matching_skills,
        "missing_skills" : missing_skills,
        "matching_skills" : matching_score,
        "experience_passed" :experience_check
    }
