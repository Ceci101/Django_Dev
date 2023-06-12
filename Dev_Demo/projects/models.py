from django.db import models


# Create your models here.


class Animal(models.Model):
    # varchar
    name = models.CharField(max_length=50)
    age = models.IntegerField()
    gender = models.BooleanField()


class Projects(models.Model):
    # CharField必须制定max_length参数；
    # verbose_name，help_text：提示信息
    # 如果需要给一个字段添加唯一约束，unique=True，默认为False
    # id = models.IntegerField(auto_created=True, primary_key=True, verbose_name='项目id', help_text='项目id')
    name = models.CharField(max_length=20, verbose_name='项目名称', help_text='项目名称',
                            unique=True, db_column='projects_name')
    leader = models.CharField(max_length=10, verbose_name='项目负责人', help_text='项目负责人')
    # default：设置默认值
    is_executed = models.BooleanField(verbose_name='是否启动项目', help_text='是否启动项目',
                                      default=True)
    # null=True:
    desc = models.TextField(verbose_name='项目描述信息', help_text='项目描述信息',
                            null=True, blank=True, default='')
    # auto_now_add：指定auto_now_add=True，在创建一条记录时，会自动将创建记录时的时间作为该字段的值
    # auto_now_add：指定auto_now=True，在更新一条记录时，会自动将更新记录时的时间作为该字段的值
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='项目创建时间', help_text='项目创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='项目更新时间', help_text='项目更新时间')

    class Meta:
        # 可以在任意一个模型类中创建一个Meta内部类，用于修改数据库的源数据信息
        # 指定数据库名
        db_table = 'tb_projects'

