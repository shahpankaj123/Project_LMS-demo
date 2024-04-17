from django.db import models
from datetime import timedelta
from lms.models1 import CBSESchool
import uuid


class Student(models.Model):
    StudentID =models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    Photo = models.ImageField(upload_to="student_images/",blank=True)
    DOB = models.DateField(null=True, blank=True)
    BirthPlace = models.CharField(max_length=50, null=True, blank=True)
    IdentificationMark = models.CharField(max_length=50, null=True, blank=True)
    AdhaarNo = models.CharField(max_length=50, null=True, blank=True)
    PassportNo = models.CharField(max_length=50, null=True, blank=True)
    MedicalCondition = models.CharField(max_length=250, null=True, blank=True)
    PermanentAddressLine1 = models.CharField(max_length=100, null=True, blank=True)
    PermanentAddressLine2 = models.CharField(max_length=100, null=True, blank=True)
    TemporaryAddressLine1 = models.CharField(max_length=100, null=True, blank=True)
    TemporaryAddressLine2 = models.CharField(max_length=100, null=True, blank=True)
    IsActive = models.BooleanField(default=True)
    PanCardNo = models.CharField(max_length=25, null=True, blank=True)
    VoterID = models.CharField(max_length=25, null=True, blank=True)
    PreviousSchoolName = models.CharField(max_length=50, null=True, blank=True)
    PrevSchoolDiseCode = models.CharField(max_length=50, null=True, blank=True)
    TransferCertificateNo = models.CharField(max_length=50, null=True, blank=True)
    SATSNo = models.CharField(max_length=50, null=True, blank=True)
    SchoolID = models.ForeignKey(CBSESchool, on_delete=models.SET_NULL, null=True, blank=True)
    CreatedAt = models.DateTimeField(null=True, blank=True)
    UpdatedAt = models.DateTimeField(null=True, blank=True)
    AdmissionNo = models.CharField(max_length=100, null=True, blank=True)
    AdmissionDate = models.DateField(null=True, blank=True)

    class Meta:
        db_table = 'CBSESchoolStudents'

class Staff(models.Model):
    member_choices = {
        "Part_Time": "Part_Time",
        "Teaching": "Teaching",
        "Non_Teaching": "Non_Teaching"
    }
    dep_choices = {
        "Civil": "Civil",
        "IT": "IT",
        "Software": "Software",
        "Management": "Management"
    }

    library_id = models.PositiveIntegerField(primary_key=True, unique=True)
    school_id = models.ForeignKey(CBSESchool, on_delete=models.SET_NULL, null=True, blank=True)
    name = models.CharField(max_length=100)
    number_card = models.CharField(max_length=100)
    membership_type = models.CharField(max_length=255, choices=member_choices)
    Department = models.CharField(max_length=255, choices=dep_choices)
    email = models.EmailField(max_length=255, blank=True)
    phone = models.CharField(max_length=20, blank=True)

class Visitor(models.Model):

    member_choices={
        "Guest_Visistor":"Guest_Visistor",
    }
    visit_choices={
        "Principal":"Principal",
        "Teacher":"Teacher",
        "Chairman":"Chairman"
    }
    school_id = models.ForeignKey(CBSESchool, on_delete=models.SET_NULL, null=True, blank=True)
    name=models.CharField(max_length=100)
    phone= models.CharField(max_length=20, blank=True)
    designation=models.CharField(max_length=255,blank=True)
    Referred_by=models.CharField(max_length=255)
    Referrer_phone= models.CharField(max_length=20, blank=True)
    membership_type= models.CharField(max_length=255,choices=member_choices) 
    visit_type=models.CharField(max_length=255,choices=visit_choices)
    email=models.EmailField(max_length=255,blank=True)
    address=models.CharField(max_length=255,blank=True)
    status=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}'

class Author(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    

class Publisher(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Editor(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class Location(models.Model):  
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name  

class Book_Type(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name 
    
class Remark(models.Model):  
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name      

class Book(models.Model):

    status_choices={
        "Available":"Available",
        "UnAvailable":"UnAvailable"
    }

    accession_number = models.PositiveIntegerField(primary_key=True, unique=True)
    school_id  = models.ForeignKey(CBSESchool, on_delete=models.SET_NULL, null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books_written')
    co_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books_coauthored', blank=True, null=True)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    translator=models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255,blank=True)
    volume = models.CharField(max_length=25)
    call_number = models.CharField(max_length=20, blank=True)
    published_year = models.PositiveIntegerField()
    published_place = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    language = models.ForeignKey(Language, on_delete=models.CASCADE)
    remarks = models.ForeignKey(Remark,on_delete=models.CASCADE)  
    page_no = models.PositiveIntegerField()
    supplier = models.ForeignKey(Supplier, on_delete=models.CASCADE)
    location = models.ForeignKey(Location, on_delete=models.CASCADE)
    book_type = models.ForeignKey(Book_Type, on_delete=models.CASCADE)
    status = models.CharField(max_length=255,choices=status_choices)  
    isbn = models.CharField(max_length=13)
    date = models.DateField()
    bill_number = models.PositiveIntegerField()
    bill_date = models.DateField()
    book_image= models.ImageField(upload_to="book_images/",blank=True)
    book_summary = models.TextField(blank=True)  

    def __str__(self):
        return self.title  

class Transaction(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE,blank=True)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE,blank=True)
    visitor = models.ForeignKey(Visitor, on_delete=models.CASCADE,blank=True)

    school_id  = models.ForeignKey(CBSESchool, on_delete=models.SET_NULL,null=True)
    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField(blank=True)
    return_date = models.DateField(blank=True, null=True)
    return_status = models.CharField(max_length=20, choices=(('Y', 'Yes'), ('N', 'No')),default="N")


class FineSetting(models.Model):
    choices={
        "Staff":"Staff",
        "Student":"Student",
        "Visitor":"Visitor"
    }
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    member_type=models.CharField(max_length=50,choices=choices)
    book_type=models.ForeignKey(Book_Type,on_delete=models.CASCADE)
    no_of_days=models.PositiveIntegerField()
    fine_amt=models.PositiveIntegerField()
    date=models.DateField()


class CollectFine(models.Model):
    id=models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    transction_id=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    fine=models.ForeignKey(FineSetting,on_delete=models.CASCADE)
    total_fine=models.PositiveIntegerField()
    remark=models.CharField(max_length=255,blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:
            print(self.transction_id.return_status)
            if self.transction_id.return_status =='Y':
                raise ValueError("Book already Returned")          
        super().save(*args, **kwargs)    

        




