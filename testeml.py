
import unittest
from xml.dom.minidom import Document, parseString
from emldoc import EmotionRepresentation, Representation, Trace

class TestEmotionMLGeneration(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_trace(self):
        trace = Trace(5,[1,2,3])
        doc = Document()
        print trace.to_xml(doc).toprettyxml()

    def test_representation(self):
        doc = Document()
        em1 = EmotionRepresentation()
        em2 = EmotionRepresentation()

        rep = Representation('dimension')
        rep.value = '100'
        rep.name = 'aggitation'
        rep.confidence = '0.5'   
        print rep.to_xml(doc).toprettyxml()
        #TODO: parse back into XML and make sure 
        # xml is well formed
            
        doc = Document() 
        rep = Representation('dimension')
        rep.value = '100'
        rep.trace = Trace(4,['0.5','0.6','0.7'])
        rep.name = 'happiness'
        rep.confidence = '0.8'   
        self.assertRaises(ValueError, rep.to_xml, doc)

        doc = Document() 
        rep = Representation('dimension')
        rep.trace = Trace(5,['0.5','0.6','0.7'])
        rep.name = 'anger'
        rep.confidence = '0.8'   
        print rep.to_xml(doc).toprettyxml()

if __name__ == '__main__':
    unittest.main()