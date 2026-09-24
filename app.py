import json
from resume_analyzer.models import CandidateEvaluationResultModel,CandidateModel
from resume_analyzer.evaluation import Evaluation
# min experience : 7 yrs
# required skills : Python, .Net and Angular, AWS
# Find matching skills, missing skills, matching score with candidate skills

def main():
    min_experience = 7
    required_skills = ['Python','.Net','Angular','AWS']

    # open the candidate.json to get the info
    try:
        with open("candidate.json","r") as file:
            data = json.load(file)
            candidate = CandidateModel.model_validate(data)
            evaluation = Evaluation(candidate,required_skills,min_experience)
            output = evaluation.candidate_evaluation()
            result= CandidateEvaluationResultModel.model_validate(output)
        print(result)
        print(result.model_dump())
        print(result.model_dump_json())

    except FileNotFoundError:
        print("File not Found!!")

if __name__ == "__main__":
    main()