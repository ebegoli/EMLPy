
#!/usr/bin/env python
''' 
Copyright 2012 Edmon Begoli

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
'''
'''
An EmotionML document generator
'''

__author__ = 'Edmon Begoli'
__author__ = 'Chelsey Dunivan'

import unittest
from xml.dom.minidom import Document, parseString
from emldoc import *

class TestEmotionMLGeneration(unittest.TestCase):
   """ Unit test for set of EmotionML generators defined in emldoc."""
   
   def test_trace(self):
        trace = Trace(5,[1,2,3])
        doc = Document()
        #print trace.to_xml(doc).toprettyxml()

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
        #print emotion.to_xml(emotionml.to_xml()).toprettyxml()
        
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

   def test_representation(self):

        doc = Document() 
        rep = Representation('test dim 1','dimension')
        rep.value = '100'
        rep.name = 'aggitation'
        rep.confidence = '0.5'
        doc = Document() 
        rep = Representation('test dim 2','dimension')
        rep.value = '100'
        rep.trace = Trace(4,['0.5','0.6','0.7'])
        rep.name = 'happiness'
        rep.confidence = '0.8'
        self.assertRaises(ValueError, rep.to_xml, doc)

        doc = Document() 
        trace = Trace(5,['0.5','0.6','0.7'])
        rep = Representation(name='test dim 3',representation='dimension',
                trace=trace,confidence='0.8')

        rep = rep.to_xml(doc).toprettyxml()

   def test_categoryRepresentation(self):
	doc= Document()
	rep=Representation(name='satisfaction', representation='category', value='.4', confidence='.3')
	rep = rep.to_xml(doc).toprettyxml()
	
	#this should pass, doesn't require value or trace
	doc=Document() 
	rep=Representation('satisfaction', 'category')
	rep = rep.to_xml(doc).toprettyxml()

	#this should fail for having both
	doc= Document()
	trace=Trace(2,[2,3,4,5])
	rep=Representation('satisfaction', 'category', trace, '.4')
	self.assertRaises(ValueError, rep.to_xml, doc)

   def test_appraisalRepresentation(self):
	doc= Document()
	rep=Representation(name='suddenness', representation='appraisal', value='.6', confidence='.1')
	rep = rep.to_xml(doc).toprettyxml()
	
	#this should pass, doesn't require value or trace
	doc=Document() 
	rep=Representation('suddenness', 'appraisal')
	rep = rep.to_xml(doc).toprettyxml()

	#this should fail for having both
	doc= Document()
	trace=Trace(5,[9,8,7,6,5,4,3,2,1])
	rep=Representation('suddenness', 'appraisal', trace, '.6')
	self.assertRaises(ValueError, rep.to_xml, doc)

   def test_actTendRepresentation(self):
	doc= Document()
	rep=Representation(name='approach', representation='action-tendency', value='.7', confidence='.1')
	rep = rep.to_xml(doc).toprettyxml()
	
	#this should pass, doesn't require value or trace
	doc=Document() 
	rep=Representation('approach', 'action-tendency')
	rep = rep.to_xml(doc).toprettyxml()

	#this should fail for having both
	doc= Document()
	trace=Trace(5,[.5,.7,.2])
	rep=Representation('approach', 'action-tendency', trace, '.7')
	self.assertRaises(ValueError, rep.to_xml, doc)

    
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
	self.assertTrue(len(check.getElementsByTagName("action-tendency"))==1)
	self.assertTrue(len(check.getElementsByTagName("appraisal"))==1)

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
	self.assertTrue(len(check.getElementsByTagName("category"))==2)
	

	#Third Emotion
	emotion3=Emotion()
	emotion3.emotion_id="Confused"
	
	rep=Representation(name='confusion', representation='category', value='20')
	emotion3.categories.append(rep)
	eml.emotions.append(emotion3)

	#Do some tests on the structure
	theEml=eml.to_xml().toprettyxml()
	check= parseString(theEml)
	self.assertTrue(len(check.getElementsByTagName("emotion"))==3 )
	self.assertTrue(len(check.getElementsByTagName("category"))==3)
	#print theEml
    
   #the following test cases are to check examples from the W3 site
   def test_category(self):
	
	#create the emotionalml
	emoML= EmotionML()

	#add emotion
	emo=Emotion()
	rep=Representation(name='satisfaction', representation='category', value='1')
	emo.categories.append(rep)
	emoML.emotions.append(emo)
	
	#add another
	emo=Emotion()
	rep=Representation(name="distant", representation='category', value='1')
	emo.categories.append(rep)
	emoML.emotions.append(emo)
	#print emoML.to_xml().toprettyxml()

   #Testing Dimension
   def test_dimension(self):
	
	#create the emotionalml
	emoML= EmotionML()
	emo=Emotion()
	rep=Representation(name='arousal', value="0.3", representation='dimension')
	emo.dimensions.append(rep)

	rep=Representation(name='pleasure', value="0.9", representation='dimension')
	emo.dimensions.append(rep)

	rep=Representation(name='dominance', value="0.8", representation='dimension')
	emo.dimensions.append(rep)
	emoML.emotions.append(emo)

	emo=Emotion()
	rep=Representation(name='friendliness', representation='dimension', value='0.2')
	emo.dimensions.append(rep)
	emoML.emotions.append(emo)
	#print emoML.to_xml().toprettyxml()

   #Testing Appraisal
   def test_appraisal(self):
	
	#create the emotionalml
	emoML= EmotionML()
	emo=Emotion()
	rep=Representation(name="novelty", representation="appraisal", value='0.8')
	emo.appraisals.append(rep)
	
	rep=Representation(name='intrinsic-pleasantness', value="0.2", representation='appraisal')
	emo.appraisals.append(rep)
	emoML.emotions.append(emo)
	
	emo=Emotion()
	rep=Representation(name='likelihood', value="5.0", representation='appraisal')
	emo.appraisals.append(rep)
	emoML.emotions.append(emo)
	#print emoML.to_xml().toprettyxml()

   #Testing Action-tendency
   def test_actionTendency(self):
	
	#create the emotionalml
	emoML= EmotionML()
	emo=Emotion()
	rep=Representation(name='approach', value="0.7", representation='action-tendency')
	emo.dimensions.append(rep)

	rep=Representation(name='being-with', value="0.8", representation='action-tendency')
	emo.dimensions.append(rep)

	rep=Representation(name='attending', representation='action-tendency', value='0.7')
	emo.dimensions.append(rep)

	rep=Representation(name='dominating', representation='action-tendency', value='0.7')
	emo.dimensions.append(rep)

	emoML.emotions.append(emo)
	#print emoML.to_xml().toprettyxml()

   def test_vocabulary(self):
	emoML= EmotionML()
	emoML.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
	
	emotion=Emotion()
	emotion.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
	rep=Representation(name='pleasure', representation='dimension', value='0.5')
	emotion.dimensions.append(rep)
	emoML.emotions.append(emotion)
	#print emoML.to_xml().toprettyxml()
	
	
if __name__ == '__main__':
        unittest.main()
