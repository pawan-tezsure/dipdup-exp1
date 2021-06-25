from tortoise import Model, fields


class Holder(Model):
    holderAddress = fields.CharField()
    balance = fields.BigIntField()