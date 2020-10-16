from import_export import resources,fields
from .models import *

class TecResource(resources.ModelResource):
    depart = fields.Field()
    class Meta:
        model = Technics
        fields = ('name','serial')
        
    def dehydrate_depart(self,technics):
        return technics.depart.name