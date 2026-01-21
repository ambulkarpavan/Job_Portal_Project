def analyze_resume(resume_text, job_skills):
    job_skills_list = [skill.strip().lower() for skill in job_skills.split(',')]

    matched = []
    missing = []

    for skill in job_skills_list:
        if skill in resume_text:
            matched.append(skill)
        else:
            missing.append(skill)

    match_percentage = (len(matched) / len(job_skills_list)) * 100 if job_skills_list else 0

    return match_percentage, missing
