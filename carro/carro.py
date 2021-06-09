class Carro:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        carro=self.session.get("carro")
    # Para corroborar si tenia un carrito previamente guardado en la sesion
        if not carro:
            carro=self.session["carro"]={}
        #else:
        self.carro=carro

    def agregar(self, insumo):
        if(str(insumo.id)not in self.carro.keys()):
            self.carro[insumo.id]={
                "insumo_id":insumo.id,
                "nombre": insumo.nombre,
                "precio": str(insumo.precio),
                "cantidad":1,
                "imagen": insumo.imagen.url
            }
        else:
            for key, value in self.carro.items():
                if key==str(insumo.id):
                    value["cantidad"]=value["cantidad"]+1
                    break
        self.guardar_carrito()

    def guardar_carrito(self):
        self.session["carro"]=self.carro
        self.session.modified=True

    def eliminar(self, insumo):
        insumo.id=str(insumo.id)
        if insumo.id in self.carro:
            del self.carro[insumo.id]
            self.guardar_carrito()    

    def restar_producto(self,insumo):
        for key, value in self.carro.items():
                if key==str(insumo.id):
                    value["cantidad"]=value["cantidad"]-1
                    if value["cantidad"]<1:
                        self.eliminar(insumo)
                    break
        self.guardar_carrito()
    
    def limpiar_carro(self):
        self.session["carro"]={}
        self.session.modified=True