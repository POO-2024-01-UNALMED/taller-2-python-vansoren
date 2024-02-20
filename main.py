class Auto:
  cantidadCreados=0
  def __init__(self,modelo,precio,asientos,marca,motor,registro):
    self.modelo=modelo
    self.precio=precio
    self.asientos=asientos
    self.marca=marca
    self.motor=motor
    self.registro=registro

  def cantidadAsientos(self):
    a=0
    for i in self.asientos:
      if str(type(i))=="<class '__main__.Asiento'>":
        a+=1
    return a

  def verificarIntegridad(self):
    if self.registro==self.motor.registro:
      for i in self.asientos:
        if i.registro!=self.registro:
          return "las piezas no son originales"
        break 
      return "Auto original"
    else:
      return "las piezas no son originales"



class Asiento:
  colores=["rojo","verde","amarillo","negro","blanco"]
  def __init__(self,color,precio,registro):
    self.color=color
    self.precio=precio
    self.registro=registro

  def cambiarColor(self,color):
    if color in self.colores:
      self.color=color



class Motor:
  def __init__(self,numeroCilindros,tipo,registro):
    self.numeroCilindros=numeroCilindros
    self.tipo=tipo
    self.registro=registro

  def cambiarRegistro(self,registro):
    self.registro=registro

  def asignarTipo(self,tipo):
    if tipo=="electrico" or tipo=="gasolina":
      self.tipo=tipo