from django.db import models
from datetime import timedelta

from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.fields import GenericRelation
from django.core.exceptions import ValidationError

class Student(models.Model):
    name=models.CharField(max_length=100)
    status=models.BooleanField(default=False)

    def __str__(self):
        return self.name

class Staff(models.Model):

    member_choices={
        "Part_Time":"Part Time",
        "Teaching":"Teaching",
        "Non_Teaching":"Non Teaching"
    }
    dep_choices={
        "Civil":"Civil",
        "IT":"IT",
        "Software":"Software",
        "Management":"Management"

    }
    library_id = models.PositiveIntegerField(primary_key=True, unique=True)
    name=models.CharField(max_length=100)
    number_card=models.IntegerField()
    membership_type= models.CharField(max_length=255,choices=member_choices) 
    Department= models.CharField(max_length=255,choices=dep_choices)
    email=models.EmailField(max_length=255,blank=True)
    phone= models.CharField(max_length=20, blank=True)

class Visitor(models.Model):
    member_choices={
        "Guest_Visistor":"Guest_Visistor",
    }
    visit_choices={
        "Principal":"Principal",
        "Teacher":"Teacher",
        "Chairman":"Chairman"
    }
    name=models.CharField(max_length=100)
    phone= models.CharField(max_length=20, blank=True)
    designation=models.CharField(max_length=255,blank=True)
    Referred_by=models.CharField(max_length=255)
    Referrer_phone= models.CharField(max_length=20, blank=True)
    membership_type= models.CharField(max_length=255,choices=member_choices) 
    visit_type=models.CharField(max_length=255,choices=visit_choices)
    email=models.EmailField(max_length=255,blank=True)
    address=models.CharField(max_length=255,blank=True)

class Author(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    

class Publisher(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Editor(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name

class Language(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Location(models.Model):  
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name  

class Book_Type(models.Model):
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name 
    
class Remark(models.Model):  
    name=models.CharField(max_length=100)

    def __str__(self):
        return self.name      

class Book(models.Model):

    status_choices={
        "Available":"Available",
        "UnAvailable":"UnAvailable"
    }

    accession_number = models.PositiveIntegerField(primary_key=True, unique=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books_written')
    co_author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books_coauthored', blank=True, null=True)
    editor = models.ForeignKey(Editor, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    translator=models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    sub_title = models.CharField(max_length=255,blank=True)
    volume = models.CharField(max_length=25)
    copies = models.PositiveIntegerField()
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
    isbn = models.CharField(max_length=13, unique=True)
    date = models.DateField()
    bill_number = models.PositiveIntegerField()
    bill_date = models.DateField()
    book_image= models.ImageField(upload_to="book_images/",blank=True)
    desc = models.TextField(blank=True)  # Assuming desc can be blank

    def __str__(self):
        return self.title    


class Transaction(models.Model):

    borrower_type = models.ForeignKey(ContentType, on_delete=models.CASCADE, limit_choices_to={'model__in': ('staff', 'student', 'visitor')})
    borrower_id = models.PositiveIntegerField()
    borrower = GenericForeignKey('borrower_type', 'borrower_id')

    book = models.ForeignKey(Book,on_delete=models.CASCADE)
    issue_date = models.DateField()
    due_date = models.DateField(blank=True)
    return_date = models.DateField(blank=True, null=True)
    return_status = models.CharField(max_length=20, choices=(('Y', 'Yes'), ('N', 'No')),default="N")

    def save(self, *args, **kwargs):
        if not self.pk:
            if self.book.copies > 0:
                if isinstance(self.borrower, Student):
                    self.due_date = self.issue_date + timedelta(days=14)
                elif isinstance(self.borrower, Staff):
                    self.due_date = self.issue_date + timedelta(days=30)
                self.book.copies -= 1
                self.book.save()
            else:
                raise ValueError("Book copies are not available")
        super().save(*args, **kwargs)

        if self.pk:
            if self.return_status == 'Y':
                self.book.copies += 1
                self.book.save()


    def clean(self):
        if self.borrower_type== "Student" and self.book.copies <= 0:
            raise ValidationError("No copies of the book available for students")
        elif self.borrower_type == "Staff" and self.book.copies <= 0:
            raise ValidationError("No copies of the book available for staff")


class FineSetting(models.Model):
    choices={
        "Staff":"Staff",
        "Student":"Student",
        "Visitor":"Visitor"
    }

    member_type=models.CharField(max_length=50,choices=choices)
    book_type=models.ForeignKey(Book_Type,on_delete=models.CASCADE)
    no_of_days=models.PositiveIntegerField()
    fine_amt=models.PositiveIntegerField()
    date=models.DateField()


class CollectFine(models.Model):
    transction_id=models.ForeignKey(Transaction,on_delete=models.CASCADE)
    fine=models.ForeignKey(FineSetting,on_delete=models.CASCADE)
    total_fine=models.PositiveIntegerField()

    def save(self, *args, **kwargs):
        if not self.pk:
            print(self.transction_id.return_status)
            if self.transction_id.return_status =='Y':
                raise ValueError("Book already Returned")          
        super().save(*args, **kwargs)    

        




