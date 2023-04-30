from tortoise import fields, models
from tortoise.contrib.pydantic import pydantic_model_creator

class ChatCompletionModel(models.Model):
    id = fields.IntField(pk=True)
    messages = fields.JSONField()
    response = fields.JSONField()
    created_at = fields.DatetimeField(auto_now_add=True)
