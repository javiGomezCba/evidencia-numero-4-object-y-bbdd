import unittest

from detector_de_radiacion import DetectorDeRadiacion

class TestDetectorDeRadiacion(unittest.TestCase):
    def setUp(self):
        self.detector = DetectorDeRadiacion()
        
    def test_activar(self):
        self.detector.activar()
        self.assertTrue(self.detector.activo, "El detector deberia estar activo.")
        
    def test_desactivar(self):
        self.detector.activar()
        self.detector.desactivar()
        self.assertFalse(self.detector.activo, "El detector deberia estar inactivo.")
        
    def test_medir_radiacion_activo(self):
        self.detector.activar()
        nivel_radiacion = self.detector.medir_radiacion()
        self.assertIsNotNone(nivel_radiacion, "El nivel de radiación debería ser medido.")
        self.assertGreaterEqual(nivel_radiacion, 0, "El nivel de radiación debería ser mayor o igual a 0.")
        self.assertLessEqual(nivel_radiacion, 100, "El nivel de radiación debería ser menor o igual a 100.")
    
    def test_medir_radiacion_inactivo(self):
        nivel_radiacion = self.detector.medir_radiacion()
        self.assertIsNone(nivel_radiacion, "El nivel de radiación no debería ser medido cuando el detector está inactivo.")

if __name__ == '__main__':
    unittest.main()