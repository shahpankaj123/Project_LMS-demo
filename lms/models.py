from django.db import models
from datetime import timedelta

#Barcode Library
import barcode
from barcode.writer import ImageWriter
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO

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
        "Part_Time":"Part_Time",
        "Teaching":"Teaching",
        "Non_Teaching":"Non_Teaching"
    }
    dep_choices={
        "Civil":"Civil",
        "IT":"IT",
        "Software":"Software",
        "Management":"Management"

    }
    library_id = models.PositiveIntegerField(primary_key=True, unique=True)
    name=models.CharField(max_length=100)
    number_card=models.CharField(max_length=100)
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
    status=models.BooleanField(default=False)

    def __str__(self):
        return f'{self.pk}'

class Author(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    

class Publisher(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Editor(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Supplier(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Subject(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name

class Language(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name
    
class Location(models.Model):  
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name  

class Book_Type(models.Model):
    name=models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name 
    
class Remark(models.Model):  
    name=models.CharField(max_length=100,unique=True)

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
    book_barcode_image= models.ImageField(upload_to="book_barcode_images/",blank=True)
    book_image= models.ImageField(upload_to="book_images/",blank=True)
    desc = models.TextField(blank=True)  # Assuming desc can be blank

    def __str__(self):
        return self.title  

    def save(self, *args, **kwargs):
        if not self.book_barcode_image:
            accession_barcode = barcode.Code128("Accn No: "+str("{:04d}".format(self.accession_number)), writer=ImageWriter())
            
            # Create a BytesIO buffer to hold the barcode image
            barcode_buffer = BytesIO()
            
            # Save the barcode image to the buffer
            accession_barcode.write(barcode_buffer)
            
            # Seek to the beginning of the buffer
            barcode_buffer.seek(0)
            
            # Open the barcode image using Pillow
            barcode_image = Image.open(barcode_buffer)
            
            # Create a blank image with white background for the composite image
            composite_image = Image.new('RGB', (barcode_image.width, barcode_image.height + 20), 'white')
            
            # Paste the barcode image onto the composite image
            composite_image.paste(barcode_image, (0, 0))
            
            # Draw text on the composite image
            draw = ImageDraw.Draw(composite_image)
            font = ImageFont.load_default()  # You can change the font as needed
            text = f'Accn No: {self.accession_number}'
            draw.text((10, barcode_image.height), text, fill='black', font=font)
            
            filename = f"barcode_{self.accession_number}"
            filepath = f"media/barcode_images/{filename}"
            accession_barcode.save(filepath)
            self.book_barcode_image.name = f"barcode_images/{filename}.png"
        super().save(*args, **kwargs)



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
                elif isinstance(self.borrower, Visitor):   
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
        elif self.borrower_type == "Visitor" and self.book.copies <= 0:
            raise ValidationError("No copies of the book available for Visitor")


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

        




