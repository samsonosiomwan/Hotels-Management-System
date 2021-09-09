
from django.db import models
from django.db.models.deletion import CASCADE
import uuid
from django.contrib.auth.models import AbstractBaseUser,BaseUserManager



class MyAccountManager(BaseUserManager):
    use_in_migrations=True
    def create_user(self,username,email,phone, password=None):
        if not username:
            raise ValueError('users must have an username')
        if not email:
            raise ValueError('users must have an email')
        if not phone:
            raise ValueError('users must have an phone')

        user = self.model(
            email = self.normalize_email(email),
            username=username,
            phone=phone,
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self,username, email, password, phone):
        user = self.create_user(
            email = self.normalize_email(email),
            username=username,
            phone=phone,
            password=password
        )

        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user




class User(AbstractBaseUser):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)

    # id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=15, unique=True)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=12)
    password = models.CharField(max_length=100)
    otp_code = models.CharField(max_length=5)
    email_verified = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    USERNAME_FIELD ='username'
    REQUIRED_FIELDS =['email','phone']

    objects=MyAccountManager()

    def __str__(self):
        return self.username

    def has_perm(self,perm,obj=None):
        return self.is_staff
    
    def has_module_perms(self, app_label):
        return True



class Receptionist(models.Model):
    GENDER = (('M', 'Male'),('F', 'Female'),)
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    #id=models.AutoField(primary_key=True)
    user_id =models.ForeignKey(User,on_delete=models.CASCADE)
    first_name= models.CharField(max_length=20)
    last_name=models.CharField(max_length=20)
    gender= models.CharField(max_length=1,choices=GENDER)
    avatar_url=models.CharField(max_length=200)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.first_name,self.last_name



class PaymentType(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    name = models.CharField(max_length=50)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Payment(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    payment_type_id = models.ForeignKey(PaymentType, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    amount = models.CharField(max_length=200)
    created_at = models.DateField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)

    def __str__(self):
        return self.amount


class RoomType(models.Model):
    ROOM_TYPES = (
        ('King', 'King'),
        ('Luxury', 'Luxury'),
        ('Normal', 'Normal'),
        ('Economic', 'Economic'),
    )
    id = models.UUIDField(
        primary_key=True, editable=False, default=uuid.uuid4,)
    room_type = models.CharField(max_length=20, choices=ROOM_TYPES)
    price = models.FloatField()
    image = models.ImageField(upload_to='images/')
    room_description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.room_type


class RoomStatus(models.Model):
    ROOM_STATUS = (
        ('Available', 'Available'),
        ('Unavailable', 'Unavailable'),
    )
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    status = models.CharField(max_length=20, choices=ROOM_STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.status


class Room(models.Model):
    id = models.UUIDField(primary_key=True, editable=False)
    room_type_id = models.ForeignKey(RoomType, on_delete=models.CASCADE)
    room_status_id = models.ForeignKey(RoomStatus, on_delete=models.CASCADE)
    room_no = models.IntegerField()
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id


class Booking(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    room_id = models.ForeignKey(Room, on_delete=models.CASCADE)
    customer_id = models.ForeignKey(User, on_delete=models.CASCADE)
    staff_id = models.ForeignKey(Receptionist, on_delete=models.CASCADE)
    payment_id = models.ForeignKey(Payment, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.id
