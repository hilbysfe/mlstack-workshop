import unittest
from mlstack.utils.model import Model
from mlstack.utils.model import get_prediction
import numpy as np

class TestModel(unittest.TestCase):
    # Test model output
    def test_model(self):
        model = Model()
        self.assertEqual(model.predict([1,1,1]), 1)
        self.assertEqual(model.predict(np.array([1,2,3])), 2.0)

    # Verify model input types
    def test_input_value(self):
        model = Model()
        self.assertRaises(TypeError, model.predict, True)