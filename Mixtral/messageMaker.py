from Reader.pdfReader import get_pdf_text
from Reader.docxReader import extract_text_from_docx


def extract_text(file_path):
    if file_path.split(".")[-1] == "pdf":
        return get_pdf_text(file_path)
    else:
        return extract_text_from_docx(file_path)
    

def create_evaluation_message(Resume,JD):
    system_message = {
            "role": "system",
            "content": """Evaluate the given resume in relation to the provided job description and assign a score on a scale of 1 to 10. 
            Consider the alignment of skills, experience, and qualifications with the requirements outlined in the job description. Matching skills along with more experience should be given more score
            .Use this list to score Work [Relevance to Job Description,Experience,Achievements and Accomplishments,Skills and Competencies,Quantifiable Metrics,Education and Qualifications,Career Objectives,Professional Development,Networking and Professional Affiliations,Online Presence,Language Proficiency,Publications and Presentations,Customization,Keywords and Buzzwords,Adaptability and Flexibility,Cultural Fit,References and Recommendations,Attention to Detail,Formatting and Structure,Overall Impression]
            more score to those who qualify first and more properties
            Provide only the numerical score and ensure it falls within the specified range. output content should only be score, output should be like socre = ?  reason = ?"""
            }
    user_message= {
            "role": "user",
            "content": f"""Resume: {Resume} Job_Description : {JD} """
        }
    return [system_message,user_message]

    
