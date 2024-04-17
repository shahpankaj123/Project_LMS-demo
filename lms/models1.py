from django.db import models

class CBSESchool(models.Model):
    SchoolID = models.CharField(max_length=32, primary_key=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    SchoolDiseCode = models.CharField(max_length=50, null=True, blank=True)
    Landline = models.CharField(max_length=15, null=True, blank=True)
    Website = models.CharField(max_length=100, null=True, blank=True)
    ESTDate = models.DateField(null=True, blank=True)
    History = models.CharField(max_length=2000, null=True, blank=True)
    GSTNo = models.CharField(max_length=50, null=True, blank=True)
    PanNo = models.CharField(max_length=50, null=True, blank=True)
    RegistrationNo = models.CharField(max_length=50, null=True, blank=True)
    InstitutionCode = models.CharField(max_length=50, null=True, blank=True)
    CreatedAt = models.DateTimeField(null=True, blank=True)
    UpdatedAt = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'CBSESchool'

class CBSESchoolStaff(models.Model):
    SchoolStaffID = models.CharField(max_length=32, primary_key=True)
    DOB = models.DateField()
    TemporaryAddressLine1 = models.CharField(max_length=50, null=True, blank=True)
    TemporaryAddressLine2 = models.CharField(max_length=50, null=True, blank=True)
    PermanentAddressLine1 = models.CharField(max_length=50, null=True, blank=True)
    PermanentAddressLine2 = models.CharField(max_length=50, null=True, blank=True)
    WhatsappNo = models.CharField(max_length=15, null=True, blank=True)
    DateOfAppointment = models.DateField(null=True, blank=True)
    DateOfRetirement = models.DateField(null=True, blank=True)
    ProvidentFund = models.BooleanField(null=True, blank=True)
    ESI = models.BooleanField(null=True, blank=True)
    ProfessionalTax = models.BooleanField(null=True, blank=True)
    Gratuity = models.BooleanField(null=True, blank=True)
    CautionDeposit = models.BooleanField(null=True, blank=True)
    ProfileImage = models.CharField(max_length=300, null=True, blank=True)
    AppToken = models.CharField(max_length=300, null=True, blank=True)
    IsActive = models.BooleanField(default=True)
    SchoolID = models.ForeignKey('CBSESchool', on_delete=models.SET_NULL, null=True, blank=True)
    AccountNumber = models.CharField(max_length=30, null=True, blank=True)
    AdhaarNo = models.CharField(max_length=25, null=True, blank=True)
    BankAddress = models.CharField(max_length=100, null=True, blank=True)
    BranchName = models.CharField(max_length=25, null=True, blank=True)
    FatherMobileNo = models.CharField(max_length=25, null=True, blank=True)
    FatherName = models.CharField(max_length=25, null=True, blank=True)
    IFSCCode = models.CharField(max_length=25, null=True, blank=True)
    MotherMobileNo = models.CharField(max_length=25, null=True, blank=True)
    MotherName = models.CharField(max_length=25, null=True, blank=True)
    PanNo = models.CharField(max_length=25, null=True, blank=True)
    PassportNo = models.CharField(max_length=25, null=True, blank=True)
    SpouseMobileNo = models.CharField(max_length=25, null=True, blank=True)
    SpouseName = models.CharField(max_length=25, null=True, blank=True)
    PlaceOfBirth = models.CharField(max_length=50, null=True, blank=True)
    CreatedAt = models.DateTimeField(null=True, blank=True)
    UpdatedAt = models.DateTimeField(null=True, blank=True)  
    StaffCode = models.IntegerField(null=True, blank=True)  
    FirebaseToken = models.CharField(max_length=500, null=True, blank=True)
    IsLoggedIn = models.BooleanField(default=False)

    class Meta:
        db_table = 'CBSESchoolStaff'



# Define other related models (AcademicYear, CBSESchool, CBSESchoolStaff, Status, Designation) similarly
