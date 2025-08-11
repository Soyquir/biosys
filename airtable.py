#from pyairtable import Api
from pyairtable.orm import Model
from pyairtable.orm import fields

class Usuario (Model):
    clave=fields.TextField("clave")
    contra=fields.TextField("contra")
    nombre=fields.TextField("nombre")
    admin=fields.CheckboxField("admin")


    class Meta:
        api_key="pat81Apk92CVnEQlf.54197eabffa1531e1f94835d5f6f006b2f3e6ea593ed4cd4ce109f9adc9dbdc4"
        base_id="appFRo8CEre58zIr5"
        table_name="USUARIO"


class Bioenergia(Model):
    cultivo=fields.TextField("cultivo")
    parte=fields.TextField("parte")
    cantidad=fields.FloatField("cantidad")
    area = fields.FloatField("area")
    energia = fields.FloatField("energia")
    municipio=fields.SelectField("municipio")
    latitud=fields.FloatField("latitud")
    longitud = fields.FloatField("longitud")
    class Meta:
        api_key="pat81Apk92CVnEQlf.54197eabffa1531e1f94835d5f6f006b2f3e6ea593ed4cd4ce109f9adc9dbdc4"
        base_id="appFRo8CEre58zIr5"
        table_name="bioenergia"



#api=Api ("pat81Apk92CVnEQlf.54197eabffa1531e1f94835d5f6f006b2f3e6ea593ed4cd4ce109f9adc9dbdc4")
#tabla = api.table("appFRo8CEre58zIr5","usuario")


#yo= {'clave': 'quiroga', 
# 'contra': 'quiroga',
#'nombre': 'jesus quiroga', 
# 'admin': 1
# }

#tabla.create(yo)
#registros= tabla.all()
#for r in registros:
#    print(r["fields"])