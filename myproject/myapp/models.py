from django.db import models

# ================= Resume Model =================
class Resume(models.Model):
    profile_pic = models.ImageField(upload_to='profile_pics/', null=True, blank=True)
    full_name = models.CharField(max_length=100)
    address = models.TextField()
    phone = models.CharField(max_length=15)
    email = models.EmailField()
    career_objective = models.TextField()
    certification = models.CharField(max_length=100, blank=True)
    project = models.CharField(max_length=100, blank=True)
    reference = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.full_name + "-" + self.email + "-" + self.phone


# ================= Education Model =================
class Education(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='educations')
    degree = models.CharField(max_length=100)
    institution = models.CharField(max_length=150)
    graduation_year = models.IntegerField()

    def __str__(self):
        return f"{self.degree} - {self.institution}"


# ================= Work Experience Model =================
class WorkExperience(models.Model):
    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='experiences')
    company = models.CharField(max_length=150)
    position = models.CharField(max_length=100)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.company + "-" + self.position


# ================= Skills Model =================
class Skill(models.Model):
    SKILL_TYPE = [
        ('hard', 'Hard'),
        ('soft', 'Soft'),
    ]

    resume = models.ForeignKey(Resume, on_delete=models.CASCADE, related_name='skills')
    name = models.CharField(max_length=100)
    type = models.CharField(max_length=10, choices=SKILL_TYPE)

    def __str__(self):
        return self.name
