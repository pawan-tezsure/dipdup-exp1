from tortoise import Model, fields


class Holder(Model):
    holderAddress = fields.CharField(max_length=100)
    balance = fields.DecimalField(max_digits=10,decimal_places=18)
