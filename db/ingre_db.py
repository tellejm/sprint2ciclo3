from models.ingresos import Ingresos
from typing import Dict



database_ingresos = Dict[str,Ingresos]

database_ingresos = {

    1: Ingresos(**{

                     "Idigresos": 1  ,
                     "descripcion":"regalo" ,
                     "frecuencia":"repite"  ,
                     "importe":200.0   ,
                     "fecha_de_vencimiento":"2020-12-10 23:57:55.058617" ,
                     "estado":"pendiente" ,
                     "categoría":"Bono",
                     "fecha_lanzamiento":"2020-12-10 23:57:55.058617" ,
                     "fecha_pago":"2020-12-10 23:57:55.058617" ,
                     "observaciones":"Bueno",
                      "username":"Juan"   
                      })
                        ,

   2: Ingresos(**{
                     "Idigresos": 1  , 
                     "descripcion":"Arriendo" ,
                     "frecuencia":"repite"  ,
                     "importe":200.0   ,
                     "fecha_de_vencimiento":"2020-12-10 23:57:55.058617" ,
                     "estado":"pendiente" ,
                     "categoría":"Bono",
                     "fecha_lanzamiento":"2020-12-10 23:57:55.058617" ,
                     "fecha_pago":"2020-12-10 23:57:55.058617",
                     "observaciones":"Bueno" ,
                      "username":"Juan"  
                    
                    }), 
                                                                        

}

def get_ingresos(Idigresos:int):
    if Idigresos in database_ingresos.keys():
        return database_ingresos[Idigresos]
    else:
        return None

def set_ingresos(ingreso_in_db: Ingresos):
    database_ingresos[ingreso_in_db.Idigresos] = ingreso_in_db
    return ingreso_in_db 