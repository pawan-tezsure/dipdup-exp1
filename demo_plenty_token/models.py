from tortoise import Model, fields


class Holder(Model):
    holderAddress = fields.CharField(max_length=100)
    balance = fields.BigIntField(null=False)