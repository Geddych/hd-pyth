
from import_export import resources,fields
from .models import *

class TecResource(resources.ModelResource):
    depart = fields.Field()
    class Meta:
        model = Technics
        fields = ('name','serial')
        
    def dehydrate_depart(self,technics):
        return technics.depart.name

class SRResource(resources.ModelResource):
    technics = fields.Field()
    serial = fields.Field()

    class Meta:
        model = SendRecord
        fields = ('get_date','send_date','retus_date','ret_date','repair_reason')

    def dehydrate_technics(self,sendrecord):
        return sendrecord.technics.name
    def dehydrate_serial(self,sendrecord):
        return sendrecord.technics.serial