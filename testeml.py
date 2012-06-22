
import unittest
from xml.dom.minidom import Document, parseString
from emldoc import *

class TestEmotionMLGeneration(unittest.TestCase):

    #skipping this one for the moment
    @unittest.skip("skipping to test mine")
    def test_trace(self):
        trace = Trace(5,[1,2,3])
        doc = Document()
        print trace.to_xml(doc).toprettyxml()
    
    #skipping this one for the moment
    @unittest.skip("skipping to test mine")
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

        #check that info has id "some-id" 
        infos = dom3.getElementsByTagName("info")
        self.assertEqual( str(infos[0].getAttribute("id")), "some-id"  )


        #check that reference is present and that its role is "triggeredBy" 
        references = dom3.getElementsByTagName("reference")
        self.assertEqual( str(references[0].getAttribute("role")),"triggeredBy")
    #skipping this one for the moment
    @unittest.skip("skipping to test mine")
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
   
    ##Chelsey's Testing Function
    def test_emotionml(self):
	eml= EmotionML()
	
	#check there's nothing in it
	theEml=eml.to_xml().toprettyxml()
	check= parseString(theEml)
	self.assertFalse(check.getElementsByTagName("emotion"))
	#first emotion
	emotion= Emotion()
	emotion.emotion_id='fear'
	
	#category
	rep=Representation(name='fear', representation='category', value='100', confidence='.8')
	emotion.categories.append(rep)
	
	#dimension
	rep=Representation(name="unpredictability", representation='dimension', confidence='.5', value='50')
	emotion.dimensions.append(rep)
	
	#action-tendency
	rep=Representation(name="avoidance", representation='action-tendency', confidence='.3', value='.4')
	emotion.action_tendencies.append(rep)

	#Appraisal
	rep=Representation(name='unexpectedness', representation='appraisal', confidence='.2', value='90')
	emotion.appraisals.append(rep)
	eml.emotions.append(emotion)
	
	#See what the structure is at this point
	theEml=eml.to_xml().toprettyxml()
	check= parseString(theEml)
	self.assertTrue(len(check.getElementsByTagName("emotion"))==1)
	self.assertTrue(len(check.getElementsByTagName("category"))==1)
	

	#Second Emotion
	emotion2=Emotion()
	emotion2.emotion_id="Happy"
	
	rep=Representation(name='happiness', representation='category', value='30')
	emotion2.categories.append(rep)
	eml.emotions.append(emotion2)

	#testing after the second emotion
	theEml=eml.to_xml().toprettyxml()
	check= parseString(theEml)
	self.assertTrue(len(check.getElementsByTagName("emotion"))==2)
	print len(check.getElementsByTagName("category"))	
	self.assertTrue(len(check.getElementsByTagName("category"))==2)
	

	#Third Emotion
	emotion3=Emotion()
	emotion3.emotion_id="Confused"
	
	rep=Representation(name='confusion', representation='category', value='20')
	emotion3.categories.append(rep)
	eml.emotions.append(emotion3)
	print eml.to_xml().toprettyxml()
	
	# Do some tests on the structure
	theEml=eml.to_xml().toprettyxml()
	check= parseString(theEml)
	self.assertTrue(len(check.getElementsByTagName("emotion"))==3)
if __name__ == '__main__':
    unittest.main()
