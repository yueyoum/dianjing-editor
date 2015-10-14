# -*- coding:utf-8 -*-

from django.db import models
from django.core.exceptions import ValidationError

from apps.building.models import Building
from apps.match.models import ChallengeMatch
# Create your models here.


class Conversation(models.Model):
    TRIGGER_TYPE = (
        (1, '点击建筑'),
        (2, '挑战关卡'),
        (3, '点击按钮')
    )

    TRIGGER_TIME = (
        (1, '战斗开始触发'),
        (2, '战斗结束触发'),
    )

    id = models.IntegerField(primary_key=True, verbose_name='会话id')
    tp = models.IntegerField(choices=TRIGGER_TYPE, verbose_name='触发条件')
    condition_value = models.CharField(max_length=64, verbose_name='条件值')
    is_loop = models.BooleanField(verbose_name='是否循环')
    time_tp = models.IntegerField(choices=TRIGGER_TIME, verbose_name='触发时间')
    conversation = models.TextField(blank=True, verbose_name='剧情')

    def clean(self):
        if self.tp == 1:
            if not self.condition_value.isdigit() or \
                    not Building.objects.filter(id=int(self.condition_value)).exists():
                raise ValidationError("Building {0} not exists".format(self.condition_value))

        if self.tp == 2:
            if not self.condition_value.isdigit() or \
                    not ChallengeMatch.objects.filter(id=int(self.condition_value)).exists():
                raise ValidationError("ChallengeMatch {0} not exists".format(self.condition_value))

    class Meta:
        db_table = 'conversation'
        verbose_name = "剧情"
        verbose_name_plural = "剧情"

    @classmethod
    def _patch_fixture(cls, fixture_b):
        fixture_a = _patch_conversation_fixture(fixture_b)
        for f in fixture_a:
            conversation_info = {}
            for _r in ConversationInfo.objects.filter(conversation__conversation_info__=f['pk']):
                conversation_info['position'] = _r.position
                conversation_info['icon'] = _r.icon
                conversation_info['contain'] = _r.contain

            f['fields']['conversation_info'] = conversation_info

        return fixture_a


def _patch_conversation_fixture(fixture):
    for f in fixture:
        conversation_id = f['fields'].pop('conversation')
        conversation = Conversation.objects.get(id=conversation_id)
        f['pk'] = conversation.id
        f['fields']['tp'] = conversation.tp
        f['fields']['condition_value'] = conversation.condition_value
        f['fields']['is_loop'] = conversation.is_loop
        f['fields']['time_tp'] = conversation.time_tp
        f['fields']['conversation'] = conversation.conversation

    return fixture


class ConversationInfo(models.Model):
    POSITION_TYPE = (
        (1, '在左边'),
        (2, '在右边')
    )

    conversation_info = models.ForeignKey(Conversation)
    position = models.IntegerField(choices=POSITION_TYPE, verbose_name='会话者位置')
    icon = models.CharField(max_length=255, verbose_name='会话者图标')
    contain = models.CharField(max_length=255, verbose_name='会话内容')

    class Meta:
        db_table = 'conversation_info'
