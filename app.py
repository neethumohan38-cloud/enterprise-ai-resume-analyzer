import json
from resume_analyzer.models import CandidateEvaluationResult,Candidate
from resume_analyzer.evaluation import candidate_evaluation
# min experience : 7 yrs
# required skills : Python, .Net and Angular, AWS
# Find matching skills, missing skills, matching score with candidate skills

def main():
    min_experience = 7
    required_skills = ['Python','.Net','Angular','AWS']

    # open the candidate.json to get the info
    try:
        with open("candidate.json","r") as file:
            candidate:Candidate = json.load(file)
            result:CandidateEvaluationResult = candidate_evaluation(candidate,required_skills,min_experience)
        print(result)
    except FileNotFoundError:
        print("File not Found!!")

if __name__ == "__main__":
    main()