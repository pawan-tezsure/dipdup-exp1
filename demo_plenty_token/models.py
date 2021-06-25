from tortoise import Model, fields


class Holder(Model):
    holderAddress = fields.CharField(pk=True,max_length=36)
    balance = fields.BigIntField(null=False)