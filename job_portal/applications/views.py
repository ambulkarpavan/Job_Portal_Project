from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .serializers import ApplicationSerializer
from .decorators import candidate_required

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from jobs.decorators import recruiter_required
from .models import Application
from .utils import extract_text_from_pdf
from .analyzer import analyze_resume

@api_view(['POST'])
@permission_classes([IsAuthenticated])
@candidate_required
def apply_job(request, job_id):
    data = request.data.copy()
    data['job'] = job_id

    serializer = ApplicationSerializer(data=data)
    if serializer.is_valid():
        serializer.save(candidate=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
@permission_classes([IsAuthenticated])
@recruiter_required
def view_applications(request, job_id):
    applications = Application.objects.filter(job_id=job_id)

    result = []

    for app in applications:
        resume_text = extract_text_from_pdf(app.resume.path)
        match_percent, missing = analyze_resume(resume_text, app.job.skills)

        app.match_percentage = match_percent
        app.missing_skills = ", ".join(missing)
        app.save()

        result.append({
            "candidate": app.candidate.username,
            "match_percentage": match_percent,
            "missing_skills": missing,
            "resume": app.resume.url
        })

    return Response(result)
