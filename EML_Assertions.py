import unittest
from xml.dom.minidom import Document, parseString
from emldoc import *
import time
import datetime

class TestEMLAssertions(unittest.TestCase):
	#TODO
	#not sure how to do this one
	'''def test_100(self):'''

	def test_101(self):
		eml=EmotionML()
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		
		self.assertEqual(doc.documentElement.tagName,'emotionml',printOutcome("101","fail","The root element of standalone EmotionML documents is not <emotionml>."))
		print printOutcome("101","pass","The root element of standalone EmotionML documents is <emotionml>.")
		
	def test_102(self):
		eml=EmotionML()
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertEqual(doc.documentElement.getAttribute('xmlns'), "http://www.w3.org/2009/10/emotionml", printOutcome('102', 'fail', 'The <emotionml> element does not define the EmotionML namespace: "http://www.w3.org/2009/10/emotionml".'))
		print printOutcome("102","pass",'The <emotionml> element defines the EmotionML namespace: "http://www.w3.org/2009/10/emotionml".')


	def test_103(self):
		eml=EmotionML()
		emotion=Emotion()
		rep=Representation('anger', 'category')
		emotion.categories.append(rep)
		eml.emotions.append(emotion)
		emotion=Emotion()
		rep=Representation('sadness', 'category')
		emotion.categories.append(rep)
		eml.emotions.append(emotion)
		emxml= eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(len(doc.getElementsByTagName("emotion")) > 0,
			printOutcome('103', 'fail', 'The <emotionml> element cannot contain one or more <emotion> elements.'))
		print printOutcome("103","pass","The <emotionml> element may contain one or more <emotion> elements.")
	
	#TODO
	'''def test_104(self):'''

	def test_105(self):
		eml=EmotionML()
		info= Info()
		eml.info=info
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.getElementsByTagName("info"), printOutcome('105', 'fail', 'The <emotionml> element cannot contain a single <info> element.'))
		print printOutcome("105","pass","The <emotionml> element MAY contain a single <info> element.") 

	def test_110(self):
		eml=EmotionML()
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('version'), printOutcome('110', 'fail', 'The root element of a standalone EmotionML document does not have an attribute "version".'))
		print printOutcome("110","pass",'The root element of a standalone EmotionML document has an attribute "version".')
	

	def test_111(self):
		eml=EmotionML()
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertEqual(doc.documentElement.getAttribute('version'), "1.0", printOutcome('111', 'fail', 'The "version" attribute of <emotionml> does not have the value "1.0"'))
		print printOutcome("111","pass",'The "version" attribute of <emotionml> has the value "1.0"')
	

	def test_112(self):
		eml= EmotionML()
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('category-set'), printOutcome("112", 'fail', 'The <emotionml> element cannot contain an attribute "category-set".'))
		print printOutcome("112", 'pass', 'The <emotionml> element  MAY contain an attribute "category-set".')

	#TODO
	'''
	def test_113(self):
	def test_114(self):
	'''
	
	def test_115(self):
		eml=EmotionML()
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('dimension-set'), printOutcome('115', 'fail', 'The <emotionml> element cannot contain an attribute "dimension-set".'))
		print printOutcome('115', 'pass', 'The <emotionml> element MAY contain an attribute "dimension-set".')

	#TODO
	'''
	def test_116(self):
	def test_117(self):
	'''

	def test_118(self):
		eml= EmotionML()
		eml.appraisal_set="http://www.example.com/emotion/appraisal/scherer.xml"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('appraisal-set'), printOutcome("118", 'fail', 'The <emotionml> element cannot contain an attribute "appraisal-set".'))
		print printOutcome("118", 'pass', 'The <emotionml> element  MAY contain an attribute "appraisal-set".')

	#TODO
	'''
	def test_119(self):
	def test_120(self):
	'''
	
	def test_121(self):
		eml=EmotionML()
		eml.action_tendency_set="http://www.example.com/emotion/action/frijda.xml"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('action-tendency-set'), printOutcome('121', 'fail', 'The <emotionml> element cannot contain an attribute "action-tendency-set".'))
		print printOutcome('121', 'pass', 'The <emotionml> element MAY contain an attribute "action-tendency-set".')

	#TODO
	'''
	def test_122(self):
	def test_123(self):
	def test_124(self):
	'''
	def test_150(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('disappointment', 'category')
		emo.categories.append(rep)
		rep=Representation('despair', 'category')
		emo.categories.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertEqual(len(doc.getElementsByTagName('category')), 2, printOutcome('150', 'fail', 'The <emotion> element cannot contain one or more <category> elements.'))
		print printOutcome('150', 'pass', 'The <emotion> element  contains one or more <category> elements.')

	def test_151(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='pleasure', representation='dimension', value='.5')
		emo.dimensions.append(rep)
		rep=Representation(name='dominance', representation='dimension', value='.2')
		emo.dimensions.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)

		self.assertEqual(len(doc.getElementsByTagName('dimension')), 2, printOutcome('151', 'fail', 'The <emotion> element cannot contain one or more <dimension> elements.'))
		print printOutcome('151', 'pass', 'The <emotion> element  contains one or more <dimension> elements.')
		
	def test_152(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('desirability', 'appraisal')
		emo.appraisals.append(rep)
		rep=Representation('appealingness', 'appraisal')
		emo.appraisals.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)

		self.assertEqual(len(doc.getElementsByTagName('appraisal')), 2, printOutcome('152', 'fail', 'The <emotion> element cannot contain one or more <appraisal> elements.'))
		print printOutcome('152', 'pass', 'The <emotion> element  contains one or more <appraisal> elements.')

	def test_153(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('interrupting', 'action-tendency')
		emo.action_tendencies.append(rep)
		rep=Representation('dominating', 'action-tendency')
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)

		self.assertEqual(len(doc.getElementsByTagName('action-tendency')), 2, printOutcome('153', 'fail', 'The <emotion> element cannot contain one or more <action-tendency> elements.'))
		print printOutcome('153', 'pass', 'The <emotion> element  contains one or more <action-tendency> elements.')
#TODO
	'''
	def test_113(self):
	def test_114(self):
	'''
	
	def test_115(self):
		eml=EmotionML()
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('dimension-set'), printOutcome('115', 'fail', 'The <emotionml> element cannot contain an attribute "dimension-set".'))
		print printOutcome('115', 'pass', 'The <emotionml> element MAY contain an attribute "dimension-set".')

	#TODO
	'''
	def test_116(self):
	def test_117(self):
	'''

	def test_118(self):
		eml= EmotionML()
		eml.appraisal_set="http://www.example.com/emotion/appraisal/scherer.xml"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('appraisal-set'), printOutcome("118", 'fail', 'The <emotionml> element cannot contain an attribute "appraisal-set".'))
		print printOutcome("118", 'pass', 'The <emotionml> element  MAY contain an attribute "appraisal-set".')

	#TODO
	'''
	def test_119(self):
	def test_120(self):
	'''
	
	def test_121(self):
		eml=EmotionML()
		eml.action_tendency_set="http://www.example.com/emotion/action/frijda.xml"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('action-tendency-set'), printOutcome('121', 'fail', 'The <emotionml> element cannot contain an attribute "action-tendency-set".'))
		print printOutcome('121', 'pass', 'The <emotionml> element MAY contain an attribute "action-tendency-set".')

	def test_154(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('pride', 'category')
		emo.categories.append(rep)
		ref=Reference("http://www.example.com/data/video/v1/avi?t=2,13", 'expressedBy', 'audio')
		emo.references.append(ref)
		ref=Reference("http://www.example.com/events/e12.xml")
		emo.references.append(ref)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertEqual(len(doc.getElementsByTagName('reference')), 2, printOutcome('154', 'fail', 'The <emotion> element cannot contain one or more <reference> elements.'))
		print printOutcome('154', 'pass', 'The <emotion> element  contains one or more <reference> elements.')

	
	def test_155(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('effort', 'appraisal')
		emo.appraisals.append(rep)
		info=Info()
		emo.info=info
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		self.assertTrue(doc.getElementsByTagName('info'), printOutcome('155', 'fail', 'The <emotion> element MAY contain a single <info> element.'))
		print printOutcome('155', 'pass', 'The <emotion> element MAY contain a single <info> element.')#TODO
	'''
	def test_113(self):
	def test_114(self):
	'''
	
	def test_115(self):
		eml=EmotionML()
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('dimension-set'), printOutcome('115', 'fail', 'The <emotionml> element cannot contain an attribute "dimension-set".'))
		print printOutcome('115', 'pass', 'The <emotionml> element MAY contain an attribute "dimension-set".')

	#TODO
	'''
	def test_116(self):
	def test_117(self):
	'''

	def test_118(self):
		eml= EmotionML()
		eml.appraisal_set="http://www.example.com/emotion/appraisal/scherer.xml"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('appraisal-set'), printOutcome("118", 'fail', 'The <emotionml> element cannot contain an attribute "appraisal-set".'))
		print printOutcome("118", 'pass', 'The <emotionml> element  MAY contain an attribute "appraisal-set".')

	#TODO
	'''
	def test_119(self):
	def test_120(self):
	'''
	
	def test_121(self):
		eml=EmotionML()
		eml.action_tendency_set="http://www.example.com/emotion/action/frijda.xml"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('action-tendency-set'), printOutcome('121', 'fail', 'The <emotionml> element cannot contain an attribute "action-tendency-set".'))
		print printOutcome('121', 'pass', 'The <emotionml> element MAY contain an attribute "action-tendency-set".')


	#TODO Need help with this
	'''
	def test_156(self):
		eml=EmotionML()
		emo=Emotion()
		eml.emotions.append(emo)
		self.assertRaises(ValueError,eml.to_xml) 
		self.assertTrue(ValueError.message.find('At least one of the category or dimension or appraisal or action-tendency must be provided'), printOutcome('156', 'fail', 'The <emotion> element does not require at least one <category> or <dimension> or <appraisal> or <action-tendency> element.'))

		print printOutcome('156', 'pass', 'The <emotion> element does requires at least one <category> or <dimension> or <appraisal> or <action-tendency> element.')
'''	
	#TODO
	'''
	#not sure how to test these two one
	def test_157(self):
	def test_158(self):
	'''


	def test_159(self):
		eml= EmotionML()
		emo= Emotion()
		emo.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		rep=Representation('anger', 'category')
		emo.categories.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('category-set'), printOutcome("159", 'fail', 'The <emotionml> element cannot contain an attribute "category-set".'))
		print printOutcome("159", 'pass', 'The <emotionml> element  MAY contain an attribute "category-set".')

	#TODO
	'''
	def test_160(self):
	def test_161(self):
	'''
	
	def test_162(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name="arousal", representation='dimension', value='.5')
		emo.dimensions.append(rep)
		emo.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('dimension-set'), printOutcome('162', 'fail', 'The <emotionml> element cannot contain an attribute "dimension-set".'))
		print printOutcome('162', 'pass', 'The <emotionml> element MAY contain an attribute "dimension-set".')

	#TODO
	'''
	def test_163(self):
	def test_164(self):
	'''

	def test_165(self):
		eml= EmotionML()
		emo=Emotion()
		rep=Representation('suddenness', 'appraisal')
		emo.appraisals.append(rep)
		emo.appraisal_set="http://www.example.com/emotion/appraisal/scherer.xml"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('appraisal-set'), printOutcome("165", 'fail', 'The <emotionml> element cannot contain an attribute "appraisal-set".'))
		print printOutcome("165", 'pass', 'The <emotionml> element  MAY contain an attribute "appraisal-set".')

	#TODO
	'''
	def test_166(self):
	def test_167(self):
	'''
	
	def test_168(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('agnostic', 'action-tendency')
		emo.action_tendencies.append(rep)
		emo.action_tendency_set="http://www.example.com/emotion/action/frijda.xml"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('action-tendency-set'), printOutcome('168', 'fail', 'The <emotionml> element cannot contain an attribute "action-tendency-set".'))
		print printOutcome('168', 'pass', 'The <emotionml> element MAY contain an attribute "action-tendency-set".')

	'''
	def test_169(self):
	def test_170(self):
	'''

	def test_171(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('agnostic', 'action-tendency')
		emo.action_tendencies.append(rep)
		emo.version='1.0'
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('version'), printOutcome('171', 'fail', '	The <emotion> element MAY have an attribute "version".'))
		print printOutcome("171","pass","The <emotion> element can't have an attribute 'version'.")
	

	def test_172(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('agnostic', 'action-tendency')
		emo.action_tendencies.append(rep)
		emo.version='1.0'
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		#print '*****************************************'
		#print emxml
		#print '*****************************************'
		emotions=doc.getElementsByTagName('emotion')
		self.assertEqual(emotions[0].getAttribute('version'), "1.0", printOutcome('172', 'fail', "The 'version' attribute of <emotion> doesn't have the value '1.0'."))
		print printOutcome("172","pass",'The "version" attribute of <emotion> has the value "1.0".')
	
	def test_173(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('anger', 'category')
		emo.categories.append(rep)
		#I don't know what this is supposed to look like!
		emo.emotion_id='xsd:Angry'
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		#print '*****************************************'
		#print emxml
		#print '*****************************************'
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('id'), printOutcome('173', 'fail',"The <emotion> element can't contain an attribute 'id'."))
		print printOutcome("173","pass",'The <emotion> element MAY contain an attribute "id".')
	
	#TODO
	'''
	def test_174(self):
	'''
	def test_175(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('love', 'category')
		emo.categories.append(rep)
		emo.start= time.time()
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('start'), printOutcome('175', 'fail',"The <emotion> element cannot have an attribute 'start'."))
		print printOutcome('175', 'pass',"The <emotion> element has an attribute 'start'.")

	def test_176(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('predictability', 'appraisal')
		emo.appraisals.append(rep)
		emo.end= time.time()
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('end'), printOutcome('176', 'fail',"The <emotion> element does not have an attribute 'end'."))
		print printOutcome('176', 'pass',"The <emotion> element has an attribute 'end'.")

	def test_177(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('deservingness', 'appraisal')
		emo.appraisals.append(rep)
		emo.duration= '150'
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('duration'), printOutcome('177', 'fail','The <emotion> element does not have an attribute "duration".'))
		print printOutcome('177', 'pass','The <emotion> element  has an attribute "duration".')

	def test_178(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('deservingness', 'appraisal')
		emo.appraisals.append(rep)
		emo.time_ref_uri= "#test_uri"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('time-ref-uri'), printOutcome('178', 'fail','The <emotion> element does not have an attribute "time-ref-uri".'))
		print printOutcome('178', 'pass','The <emotion> element has an attribute "time-ref-uri".')


	def test_179(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('deservingness', 'appraisal')
		emo.appraisals.append(rep)
		emo.time_ref_anchor_point= "start"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('time-ref-anchor-point'), printOutcome('179', 'fail','The <emotion> element does not have an attribute "time-ref-anchor-point".'))
		print printOutcome('179', 'pass','The <emotion> element has an attribute "time-ref-anchor-point".')

	def test_180(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('deservingness', 'appraisal')
		emo.appraisals.append(rep)
		emo.offset_to_start= "2000"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('offset-to-start'), printOutcome('180', 'fail','The <emotion> element does not have an attribute "offset-to-start".'))
		print printOutcome('180', 'pass','The <emotion> element has an attribute "offset-to-start".')
	
	def test_181(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('indifference', 'category')
		emo.categories.append(rep)
		emo.expressed_through= "voice"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('expressed-through'), printOutcome('181', 'fail','The <emotion> element MAY have an attribute "expressed-through".'))
		print printOutcome('181', 'pass','The <emotion> element MAY have an attribute "expressed-through".')
	
	#TODO
	'''def test_182(self):'''


	


def printOutcome( ID, result, notes ):
	return "<assert id=\"%s\" res=\"%s\">%s</assert>" % (ID,result,notes)	

if __name__ == '__main__':
        unittest.main()
