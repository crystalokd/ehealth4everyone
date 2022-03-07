from django.db import models
from django.contrib.auth import get_user_model


departments=[('Cardiologist','Cardiologist'),
('Dermatologists','Dermatologists'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]


class Doctor(models.Model):
	user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
	profile_pic= models.ImageField(upload_to='profile_pic/DoctorProfilePic/',null=True,blank=True)
	address = models.CharField(max_length=40)
	mobile = models.CharField(max_length=20,null=True)
	department= models.CharField(max_length=50,choices=departments,default='Cardiologist')
	status=models.BooleanField(default=False)

    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return "{} ({})".format(self.user.first_name,self.department)




class Patient(models.Model):
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    profile_pic= models.ImageField(upload_to='profile_pic/PatientProfilePic/',null=True,blank=True)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=False)
    symptoms = models.CharField(max_length=100,null=False)
    assignedDoctorId = models.PositiveIntegerField(null=True)
    admitDate=models.DateField(auto_now=True)
    status=models.BooleanField(default=False)

    def get_absolute_url(self):
        return reverse('patient-book-appointment', args=[str(self.id)])
    @property
    def get_name(self):
        return self.user.first_name+" "+self.user.last_name
    @property
    def get_id(self):
        return self.user.id
    def __str__(self):
        return self.user.first_name+" ("+self.symptoms+")"


class Appointment(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    doctorId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40,null=True)
    doctorName=models.CharField(max_length=40,null=True)
    appointmentDate=models.DateField(auto_now=True)
    description=models.TextField(max_length=500)
    status=models.BooleanField(default=False)



class PatientDischargeDetails(models.Model):
    patientId=models.PositiveIntegerField(null=True)
    patientName=models.CharField(max_length=40)
    assignedDoctorName=models.CharField(max_length=40)
    address = models.CharField(max_length=40)
    mobile = models.CharField(max_length=20,null=True)
    symptoms = models.CharField(max_length=100,null=True)

    admitDate=models.DateField(null=False)
    releaseDate=models.DateField(null=False)
    daySpent=models.PositiveIntegerField(null=False)

    roomCharge=models.PositiveIntegerField(null=False)
    medicineCost=models.PositiveIntegerField(null=False)
    doctorFee=models.PositiveIntegerField(null=False)
    OtherCharge=models.PositiveIntegerField(null=False)
    total=models.PositiveIntegerField(null=False)




class Profile(models.Model):
    choices = (("Yes", 'Yes'), ("No", 'No'))
    user = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    Email = models.EmailField(default='none@email.com')
    Malaria = models.CharField(max_length=255, choices=choices)
    Diarrheal_Diseases = models.CharField(max_length=255, choices=choices)
    Road_Injuries = models.CharField(max_length=255, choices=choices)
    Tuberculosis = models.CharField(max_length=255, choices=choices)
    Cough = models.CharField(max_length=255, choices=choices)

    def __str__(self):
        return f'{self.user.username} Profile'