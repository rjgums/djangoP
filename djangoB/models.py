from django.db import models

class Gender(models.Model):
    gender_id = models.BigAutoField(primary_key=True)
    # gender_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY - SQL EQUIVALENT
    gender = models.CharField(max_length=55) #gender VARCHAR(55) NOT NULL - sql equivalent
    created_at = models.DateTimeField(auto_now_add=True) # TIMESTAMP DEFAULT CURRENT TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    class Meta:
        db_table = 'genders'
    
    def __str__(self):
        return self.gender
    
   
class User (models.Model):
    user_id = models.BigAutoField(primary_key=True, blank=False)
    first_name = models.CharField(max_length=55, blank=False)
    middle_name = models.CharField(max_length=55, blank=True)
    last_name = models.CharField(max_length=55, blank=False)  
    age = models.IntegerField(blank=False)
    birth_date = models.DateField(blank=False)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    username = models.CharField(max_length=55, blank=False)
    password = models.CharField(max_length=255, blank=False)
    created_at = models.DateTimeField(auto_now_add=True) # TIMESTAMP DEFAULT CURRENT TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    class Meta:
        db_table = 'users'
        
        
class Section(models.Model):
    section_id = models.BigAutoField(primary_key=True, blank=False) #gender_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    section = models.CharField(max_length=55, blank=False) #gender VARCHAR(55) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True) # created_at TIMESTAMP DEFAULT CURRENT TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # updated_at TIMESTAMP DEFAULT CURRENT_TIME UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'sections'

    def __str__(self):
        return self.section
    
class Year(models.Model):
    year_id = models.BigAutoField(primary_key=True, blank=False) #gender_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    year = models.CharField(max_length=55, blank=False) #gender VARCHAR(55) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True) # created_at TIMESTAMP DEFAULT CURRENT TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # updated_at TIMESTAMP DEFAULT CURRENT_TIME UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'years'

    def __str__(self):
        return self.year

class Course(models.Model):
    course_id = models.BigAutoField(primary_key=True, blank=False) #gender_id BIGINT NOT NULL AUTO_INCREMENT PRIMARY KEY
    course = models.CharField(max_length=55, blank=False) #gender VARCHAR(55) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True) # created_at TIMESTAMP DEFAULT CURRENT TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True) # updated_at TIMESTAMP DEFAULT CURRENT_TIME UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'courses'

    def __str__(self):
        return self.course
    
class Student(models.Model):
    student_id = models.BigAutoField(primary_key=True, blank=False)  # BIGINT NOT NULL AUTO INCREMENT PRIMARY KEY
    first_name = models.CharField(max_length=55, blank=False)  # VARCHAR(55) NOT NULL
    middle_name = models.CharField(max_length=55, blank=False)  # VARCHAR(55) NOT NULL
    last_name = models.CharField(max_length=55, blank=False)  # VARCHAR(55) NOT NULL
    age = models.IntegerField(blank=False, default=18)
    address = models.CharField(max_length=55, blank=False)  # VARCHAR(55) NOT NULL
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, default=1)
    created_at = models.DateTimeField(auto_now_add=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP

    class Meta:
        db_table = 'students'

class Academic(models.Model):
    student_id = models.BigAutoField(primary_key=True, blank=False)  # BIGINT NOT NULL AUTO INCREMENT PRIMARY KEY
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    year = models.ForeignKey(Year, on_delete=models.CASCADE)
    unit = models.IntegerField(blank=False, default=18)
    school_year = models.CharField(max_length=55, blank=False)  # VARCHAR(55) NOT NULL
    created_at = models.DateTimeField(auto_now_add=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    updated_at = models.DateTimeField(auto_now=True)  # TIMESTAMP DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
    

    class Meta:
       db_table = 'academics'
