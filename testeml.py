
import unittest
from xml.dom.minidom import Document, parseString
from emldoc import *

class TestEmotionMLGeneration(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_trace(self):
        trace = Trace(5,[1,2,3])
        doc = Document()
        print trace.to_xml(doc).toprettyxml()
    
    def test_parse_emotionml(self):
        emotionml = EmotionML()
        emotionml.dimension_set="http://someurl/dim-set"
        emotion = Emotion()

        emotion.emotion_id = "test id"
        emotion.expressed_through = "voice"
        emotion.action_tendency_set="http://someurl/action-tendency-set"

        rep = Representation(name='test',representation='action-tendency',
        value='0.5',confidence='1')

        trace = Trace( "2", ('1.5','1.5','1.6')) 

        info = Info("some-id")

        reference = Reference(uri="http://some-uri",role="triggeredBy",media_type="jpeg")

        emotion.action_tendencies.append(rep)
        emotion.info = info
        emotion.references.append(reference)

        #just for control purposes
        print emotion.to_xml(emotionml.to_xml()).toprettyxml()

        emotionml.emotions.append(emotion)


        emxml = emotionml.to_xml().toprettyxml()
        dom3 = parseString(emxml)

        #check that name of the root is there and it is a right one
        self.assertEqual( dom3.documentElement.tagName, "emotionml")

        #check that there is only one emotion child
        self.assertTrue( len( dom3.getElementsByTagName("emotion")) == 1 )
        emotions = dom3.getElementsByTagName("emotion")

        #check that first emotion has id "test id" 
        self.assertEqual( str(emotions[0].getAttribute("id")), "test id"  )
        infos = dom3.getElementsByTagName("info")

        #check that info has id "some-id" 
        self.assertEqual( str(infos[0].getAttribute("id")), "some-id"  )



    def test_representation(self):

        doc = Document() 
        rep = Representation('test dim 1','dimension')
        rep.value = '100'
        rep.name = 'aggitation'
        rep.confidence = '0.5'   
        print rep.to_xml(doc).toprettyxml()
        #TODO: parse back into XML and make sure 
        # xml is well formed
            
        doc = Document() 
        rep = Representation('test dim 2','dimension')
        rep.value = '100'
        rep.trace = Trace(4,['0.5','0.6','0.7'])
        rep.name = 'happiness'
        rep.confidence = '0.8'   
        self.assertRaises(ValueError, rep.to_xml, doc)

        doc = Document() 
        rep = Representation('test dim 3','dimension')
        rep.trace = Trace(5,['0.5','0.6','0.7'])
        rep.name = 'anger'
        rep.confidence = '0.8'   
        rep = rep.to_xml(doc).toprettyxml()

if __name__ == '__main__':
    unittest.main()