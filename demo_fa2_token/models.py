from tortoise import Model, fields


# class ExampleModel(Model):
#     id = fields.IntField(pk=True)
#     ...

#     class Meta:
#         table = 'example_models'


class wLINKHolder(Model):
    holderAddress = fields.CharField(max_length=100)
    balance = fields.DecimalField(max_digits=6,decimal_places=5)