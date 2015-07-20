# -*- coding: utf-8 -*-

from django.db import models

class TrainingType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32, verbose_name="名称")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'training_type'
        ordering = ('id',)
        verbose_name = "训练类型"
        verbose_name_plural = "训练类型"



class Training(models.Model):
    COST_TYPE = (
        (1, "软妹币"),
        (2, "钻石")
    )

    id = models.IntegerField(primary_key=True)
    name = models.CharField(unique=True, max_length=32, verbose_name="名称")
    building = models.ForeignKey('building.Building', verbose_name="所属建筑")

    tp = models.ForeignKey(TrainingType, db_column='tp', verbose_name="类型")
    icon = models.CharField(max_length=32, verbose_name="图标")
    des = models.TextField(blank=True)

    cost_type = models.IntegerField(choices=COST_TYPE, default=1, verbose_name="花费类型")
    cost_value = models.IntegerField(verbose_name="花费金额")
    need_building_level = models.IntegerField(verbose_name="所需建筑物等级")

    minutes = models.IntegerField(verbose_name="训练所需分钟")
    package = models.ForeignKey('package.Package', verbose_name="物品包")


    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'training'
        ordering = ('id',)
        verbose_name = "训练"
        verbose_name_plural = "训练"
