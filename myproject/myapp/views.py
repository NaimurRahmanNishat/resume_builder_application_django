from django.shortcuts import get_object_or_404, render, redirect
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



# ================= VIEW RESUME =================
def viewResume(request, id):
    person = Resume.objects.get(id=id)
    edecation = Education.objects.get(id=id)
    work_experience = WorkExperience.objects.get(id=id)
    skill = Skill.objects.get(id=id)

    personDict = {
        'person':person,
        'education': edecation,
        'work_experience':work_experience,
        'skill': skill
    }
    return render(request, 'viewResume.html', personDict)


# def viewResume(request, id):
#     person = get_object_or_404(Resume, id=id)
#     context = {
#         'person': person,
#         'education': person.educations.all(),
#         'work_experience': person.experiences.all(),
#         'skill': person.skills.all()
#     }
#     return render(request, 'viewResume.html', context)


# ================= EDIT RESUME =================
def editResume(request, id):
    person = Resume.objects.filter(id=id).first()
    education = Education.objects.get(id=id)
    work_experience = WorkExperience.objects.get(id=id)
    skill = Skill.objects.get(id=id)

    if request.method == 'POST':
        person.full_name = request.POST.get('full_name')
        person.profile_pic = request.POST.get('profile_pic')
        person.address = request.POST.get('address')
        person.phone = request.POST.get('phone')
        person.email = request.POST.get('email')
        person.career_objective = request.POST.get('career_objective')
        person.certification = request.POST.get('certification')
        person.project = request.POST.get('project')
        person.reference = request.POST.get('reference')
        education.degree = request.POST.get('degree')
        education.institution = request.POST.get('institution')
        education.graduation_year = request.POST.get('graduation_year')
        work_experience.company = request.POST.get('company')
        work_experience.position = request.POST.get('position')
        work_experience.start_date = request.POST.get('start_date')
        work_experience.end_date = request.POST.get('end_date')
        skill.name = request.POST.get('name')
        skill.type = request.POST.get('type')
        person.save()
        return redirect('home')
    
    personDict = {
        'person': person,
        'education': education,
        'work_experience': work_experience,
        'skill': skill
    }
    return render(request, 'editResume.html', personDict)



# ================= DELETE RESUME =================
# def deleteResume(request, id):
#     person = Resume.objects.get(id=id)
#     work_experience = WorkExperience.objects.get(id=id)
#     education = Education.objects.get(id=id)
#     skill = Skill.objects.get(id=id)

#     return render(request, 'deleteResume.html')

def deleteResume(request, id):
    person = get_object_or_404(Resume, id=id)

    if request.method == 'POST':
        person.delete()   # This deletes EVERYTHING (cascade)
    return redirect('home')

    # return render(request, 'deleteResume.html', {'person': person})


