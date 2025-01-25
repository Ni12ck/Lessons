import unittest
import test_calc2
import test_new_calc

calcTS = unittest.TestSuite()
# calcTS.addTest(unittest.makeSuite(test_calc2.CalcTest)) # Устаревший метод

# Тест из test_calc2
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_calc2.CalcTest))

# # Тест из test_new_calc
calcTS.addTest(unittest.TestLoader().loadTestsFromTestCase(test_new_calc.NewCalcTest))

runner = unittest.TextTestRunner(verbosity=2)
runner.run(calcTS)
