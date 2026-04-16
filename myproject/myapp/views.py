from django.shortcuts import render, redirect
from myapp.models import Resume, Education, WorkExperience, Skill


def home(request):
    person = Resume.objects.all()
    return render(request, 'home.html', {'person': person})


# ================= ADD RESUME =================
def addResume(request):
    if request.method == 'POST':
        full_name = request.POST.get('full_name')
        profile_pic = request.FILES.get('profile_pic')
        address = request.POST.get('address')
        phone = request.POST.get('phone')
        email = request.POST.get('email')
        career_objective = request.POST.get('career_objective') or "N/A"
        certification = request.POST.get('certification') or ""
        project = request.POST.get('project') or ""
        reference = request.POST.get('reference') or ""

        resume = Resume.objects.create(
            full_name=full_name,
            profile_pic=profile_pic,
            address=address,
            phone=phone,
            email=email,
            career_objective=career_objective,
            certification=certification,
            project=project,
            reference=reference
        )

        degrees = request.POST.getlist('degree[]')
        institutions = request.POST.getlist('institution[]')
        years = request.POST.getlist('year[]')

        for degree, institution, year in zip(degrees, institutions, years):
            if degree:
                Education.objects.create(
                    resume=resume,
                    degree=degree,
                    institution=institution,
                    graduation_year=year
                )

        companies = request.POST.getlist('company[]')
        positions = request.POST.getlist('position[]')
        starts = request.POST.getlist('start_date[]')
        ends = request.POST.getlist('end_date[]')

        for i in range(len(companies)):
            if companies[i]:
                WorkExperience.objects.create(
                    resume=resume,
                    company=companies[i],
                    position=positions[i],
                    start_date=starts[i],
                    end_date=ends[i] if ends[i] else None
                )

        skill_names = request.POST.getlist('skill_name[]')
        skill_types = request.POST.getlist('skill_type[]')

        for i in range(len(skill_names)):
            if skill_names[i]:
                Skill.objects.create(
                    resume=resume,
                    name=skill_names[i],
                    type=skill_types[i]
                )
        return redirect('home') 
    return render(request, 'addResume.html')




def viewResume(request, id):
    pass
    # return render(request, 'viewResume.html')


def editResume(request, id):
    pass
    # return render(request, 'editResume.html')


def deleteResume(request, id):
    pass
    # return render(request, 'deleteResume.html')

