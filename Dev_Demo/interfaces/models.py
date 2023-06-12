from django.db import models
# from projects.models import Projects

# Create your models here.

# Projects & Interfaces: 一对多


class Interfaces(models.Model):
    id = models.IntegerField(auto_created=True, primary_key=True, verbose_name='接口id', help_text='接口id')
    name = models.CharField(max_length=20, unique=True, verbose_name='接口名称', help_text='接口名称')
    tester = models.CharField(max_length=10, verbose_name='当前接口测试人员', help_text='当前接口测试人员')

    # 在一堆多的关系中，在多的一侧模型类中创建外键ForeignKey字段
    # 在一对一的关系中，可以在任意一侧模型类中创建OneToOneField
    # 在多对多的关系中，可以在任意一侧模型类中创建ManyToManyField
    # to：关联附表模型类
    # 1）使用父表模型类的引用，需要先导入附表模型类
    # 2）可以使用'子应用名称.父表模型类名'
    # on_delete：级联删除策略
    # 1)CASECADE: 父表数据删除时，相对应的从表数据会被自动删除
    # 2)SET_NULL: 父表数据删除时，相对应的从表数据会被自动设置为null值
    # 3)SET_DEFAULT: 父表数据删除时，相对应的从表数据会被自动设置为default值，还需要额外指定default
    # 4)PROTECT: 父表数据删除时，如果有相应的从表数据会抛出异常
    # projects = models.ForeignKey(Projects)
    # projects = models.ForeignKey(to=Projects)
    projects = models.ForeignKey(to='projects.Projects', on_delete=models.CASCADE,
                                 verbose_name='所属项目', help_text='所属项目')
    create_time = models.DateTimeField(auto_now_add=True, verbose_name='接口创建时间', help_text='接口创建时间')
    update_time = models.DateTimeField(auto_now=True, verbose_name='接口更新时间', help_text='接口更新时间')

    class Meta:
        # 可以在任意一个模型类中创建一个Meta内部类，用于修改数据库的源数据信息
        # 指定数据库名
        db_table = 'tb_interfaces'
        verbose_name = '接口表'
        verbose_name_plural = '接口表'
