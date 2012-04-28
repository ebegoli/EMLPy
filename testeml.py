
import unittest
import xml.dom.minidom
import emldoc

class TestEmotionMLGeneration(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_representation(self):
        doc = xml.dom.minidom.Document()
        em1 = EmotionRepresentation()
        em2 = EmotionRepresentation()

        rep = Representation('dimension')
        rep.value = '100'
        #traces = []
        rep.name = 'aggitation'
        rep.confidence = '0.5'   
        repr = rep.to_xml(doc).toprettyxml()

if __name__ == '__main__':
    unittest.main()