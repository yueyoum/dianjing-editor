# -*- coding: utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

class SkillType(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32)
    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'skill_type'
        ordering = ('id',)
        verbose_name = '技能类型'
        verbose_name_plural = '技能类型'


class SkillAddition(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name="名字")
    add_property = models.CharField(max_length=32, verbose_name="增加属性")
    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'skill_addition'
        ordering = ('id',)
        verbose_name = '技能加成'
        verbose_name_plural = '技能加成'


class Skill(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=32, verbose_name='名字')
    race = models.ForeignKey('staff.StaffRace', verbose_name="种族")
    icon = models.CharField(max_length=255, verbose_name="图标")
    type_id = models.ForeignKey(SkillType, db_column='type_id', verbose_name="类型")
    addition_ids = models.CharField(max_length=255, verbose_name="加成ID列表",
                                                     help_text='id:value,id:value'
                                                     )

    value_base = models.IntegerField("基础值")
    level_grow = models.IntegerField("等级增长", help_text="百分比数值")

    des = models.TextField(blank=True, verbose_name="描述")

    def __unicode__(self):
        return self.name

    class Meta:
        db_table = 'skill'
        ordering = ('id',)
        verbose_name = '技能'
        verbose_name_plural = '技能'


    @staticmethod
    def parse_addition_ids(addition_ids):
        id_values = []
        additions = addition_ids.split(',')

        for addition in additions:
            a, b = addition.split(':')
            add_property = SkillAddition.objects.get(id=int(a)).add_property
            id_values.append((add_property, int(b)))

        return id_values


    def clean(self):
        try:
            Skill.parse_addition_ids(self.addition_ids)
        except:
            raise ValidationError("加成ID列表填错了")


    @classmethod
    def patch_fixture(cls, fixture):
        for f in fixture:
            f['fields']['addition_ids'] = Skill.parse_addition_ids(f['fields']['addition_ids'])
            skill_levels = SkillLevel.objects.filter(id=f['pk']).order_by('level')
            levels = {}
            for l in skill_levels:
                data = {
                    'upgrade_training_id': l.upgrade_training_id,
                    'upgrade_training_amount': l.upgrade_training_amount
                }

                levels[l.level] = data

            f['fields']['levels'] = levels
            f['fields']['max_level'] = max(levels.keys())

        return fixture


class SkillLevel(models.Model):
    skill = models.ForeignKey(Skill)
    level = models.IntegerField(verbose_name='等级')
    upgrade_training_id = models.ForeignKey('training.TrainingSkill', verbose_name='升级所需技能训练ID')
    upgrade_training_amount = models.IntegerField(verbose_name='升级所需技能训练数量')

    def __unicode__(self):
        return "level {0}".format(self.level)

    class Meta:
        db_table = 'skill_level'
