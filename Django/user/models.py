from django.db import models

# Create your models here.


class US_User(models.Model):
    username = models.CharField(max_length=128, unique=True, db_index=True)
    password = models.CharField(max_length=64)
    uid = models.CharField(max_length=128, unique=True, db_index=True)
    name = models.CharField(max_length=32)
    number = models.CharField(max_length=16, db_index=True)
    sex = models.PositiveSmallIntegerField(default=1)  # 1 男 0 女
    school_id = models.IntegerField(db_index=True, default=0)
    role_id = models.SmallIntegerField(default=0)  # constants.roles
    # 学生端vip会员截止日期时间戳
    student_vip_expire = models.BigIntegerField(default=0)
    available = models.BooleanField(default=1)
    time_create = models.DateTimeField(auto_now_add=True)
    time_modify = models.DateTimeField(auto_now=True)