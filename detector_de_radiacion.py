import random

class DetectorDeRadiacion:
    def __init__(self):
        # Inicialmente el detector está apagado
        self.activo = False
        self.nivel_radiacion = 0.0

    def activar(self):
        if not self.activo:
            self.activo = True
            print("Detector activado.")
        else:
            print("El detector ya está activo.")

    def desactivar(self):
         if self.activo:
            self.activo = False
            print("Detector desactivado.")
         else: 
             print("El detector ya está inactivo.")

    def medir_radiacion(self):
        if self.activo:
            self.nivel_radiacion = random.uniform(0, 100)
            print(f"Nivel de radiación medido: {self.nivel_radiacion:.2f} unidades.")
            return self.nivel_radiacion
        else:
            print("El detector está inactivo. Actívelo primero para medir la radiación.")
            return None

        
detector = DetectorDeRadiacion()

detector.activar()
detector.medir_radiacion()

detector.desactivar()
detector.medir_radiacion()        