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
		try:
			eml=EmotionML()
			eml.version='3.0'
			emxml=eml.to_xml().toprettyxml()
			doc=parseString(emxml)
		except:
			print printOutcome("111","pass",'The "version" attribute of <emotionml> has the value "1.0"')
			return
		fail(printOutcome('111', 'fail', 'The "version" attribute of <emotionml> does not have the value "1.0"'))
			
	

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
		doc=parseString(emxml)
		self.assertTrue(doc.getElementsByTagName('info'), printOutcome('155', 'fail', 'The <emotion> element MAY contain a single <info> element.'))
		print printOutcome('155', 'pass', 'The <emotion> element MAY contain a single <info> element.')

	
	def test_156(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError: 
			print printOutcome('156', 'pass', 'The <emotion> element requires at least one <category> or <dimension> or <appraisal> or <action-tendency> element.')
			return
		fail (printOutcome('156', 'fail', 'The <emotion> element does not require at least one <category> or <dimension> or <appraisal> or <action-tendency> element.'))

		
	
	#TODO
	#not sure how to test these two
	'''
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
		self.assertTrue(emotions[0].getAttribute('version'), printOutcome('171', 'fail', '	The <emotion> element cannot have an attribute "version".'))
		print printOutcome("171","pass","The <emotion> element has an attribute 'version'.")
	

	def test_172(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation('agnostic', 'action-tendency')
			emo.action_tendencies.append(rep)
			emo.version='3.0'
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except:
			print printOutcome("172","pass",'The "version" attribute of <emotion> has the value "1.0".')
			return
		fail(printOutcome('172', 'fail', "The 'version' attribute of <emotion> doesn't have the value '1.0'."))
			
	
	def test_173(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('anger', 'category')
		emo.categories.append(rep)
		#I don't know what this is supposed to look like!
		emo.emotion_id='Angry'
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
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
	#TODO need help!
	'''
	def test_210(self):
		eml= EmotionML()
		emo= Emotion()
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#occ-categories"
		#emo.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		#rep=Representation('anger', 'category')
		#emo.categories.append(rep)
		#eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue((doc.documentElement.getAttribute('category-set')) or (), printOutcome("210", 'fail', 'If the <category> element is used, a category vocabulary MUST be declared using a "category-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.'))
		print printOutcome("210", 'pass', 'If the <category> element is used, a category vocabulary MUST be declared using a "category-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.')'''

	def test_211(self):
		eml= EmotionML()
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#occ-categories"
		try:
			emo= Emotion()
			rep=Representation(representation='category', value='.5')
			emo.categories.append(rep)
			eml.emotions.append(emo)
		except:
			pass
		emo=Emotion()
		rep=Representation('anger', 'category')
		emo.categories.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		categories= doc.getElementsByTagName('category')
		self.assertTrue(categories[0].getAttribute('name'), printOutcome("211", 'fail', 'A <category> element does not contain a "name" attribute.'))
		print printOutcome("211", 'pass', 'A <category> element contains a "name" attribute.')
	
	#TODO
	'''
	def test_212(self):
	def test_213(self):
	''' 

	def test_214(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='anger', representation='category', value='.5')
		emo.categories.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		categories= doc.getElementsByTagName('category')
		self.assertTrue(categories[0].getAttribute('value'), printOutcome("214", 'fail', 'A <category> can not contain a "value" attribute.'))
		print printOutcome("214", 'pass', 'A <category> MAY contain a "value" attribute.')
	
	def test_215(self):
		eml=EmotionML()
		emo=Emotion()
		trace=Trace(100, [.2, .4, .6])
		rep=Representation('worried', 'category', trace)
		emo.categories.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.getElementsByTagName('trace'), printOutcome("215", 'fail', 'A <category> can not contain a <trace> element.'))
		print printOutcome("215", 'pass', 'A <category> MAY contain a <trace> element.')

	#TODO
	#need help with this as in 156
	def test_216(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			trace=Trace(50, [.8, .4, .2])
			rep=Representation(name='interested',representation= 'category', trace=trace, value= .5 )
			emo.categories.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("216", 'pass', 'A <category> cannot contain both a "value" attribute and a <trace> element.')
			return
		fail( printOutcome("216", 'fail', 'A <category> can contain both a "value" attribute and a <trace> element.'))

	def test_217(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='interested',representation= 'category', value= .5 , confidence= .8 )
		emo.categories.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		categories= doc.getElementsByTagName('category')
		self.assertTrue(categories[0].hasAttribute('confidence'), printOutcome("217", 'fail', 'A <category> element cannot contain a "confidence" attribute.'))
		print printOutcome("217", 'pass', 'A <category> element MAY contain a "confidence" attribute.')

	#TODO need help!
	'''
	def test_220(self):
		eml= EmotionML()
		emo= Emotion()
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		#emo.dimension_set="http://www.w3.org/TR/emotion-voc/xml#fsre-dimensions"
		#rep=Representation('valence', 'dimension')
		#emo.dimensions.append(rep)
		#eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue((doc.documentElement.getAttribute('dimension-set')) or (), printOutcome("210", 'fail', 'If the <dimension> element is used, a dimension vocabulary MUST be declared using a "dimension-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.'))
		print printOutcome("210", 'pass', 'If the <dimension> element is used, a dimension vocabulary MUST be declared using a "dimension-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.')'''

	def test_221(self):
		eml= EmotionML()
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		try:
			emo= Emotion()
			rep=Representation(representation='dimension', value='.5')
			emo.dimensions.append(rep)
			eml.emotions.append(emo)
		except:
			pass
		emo=Emotion()
		trace=Trace(50, [.8, .4, .2])
		rep=Representation('valence', 'dimension', trace)
		emo.dimensions.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		dimensions= doc.getElementsByTagName('dimension')
		self.assertTrue(dimensions[0].getAttribute('name'), printOutcome("221", 'fail', 'A dimension element does not contain a "name" attribute.'))
		print printOutcome("221", 'pass', 'A dimension element contains a "name" attribute.')
	
	#TODO
	'''
	def test_222(self):
	def test_223(self):
	''' 
	def test_224(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation('arousal','dimension')
			emo.dimensions.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("224", 'pass', 'A <dimension> MUST contain either a "value" attribute or a <trace> element.')
			return
		fail( printOutcome("224", 'fail', 'A <dimension> does not contain either a "value" attribute or a <trace> element.'))

	def test_225(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='pleasure',representation= 'dimension', value= .5 , confidence= .8 )
		emo.dimensions.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		dimensions= doc.getElementsByTagName('dimension')
		self.assertTrue(dimensions[0].hasAttribute('confidence'), printOutcome("225", 'fail', 'A <dimension> element cannot contain a "confidence" attribute.'))
		print printOutcome("225", 'pass', 'A <dimension> element MAY contain a "confidence" attribute.')

	#TODO need help!
	'''
	def test_230(self):
		eml= EmotionML()
		emo= Emotion()
		eml.appraisal_set="http://www.w3.org/TR/emotion-voc/xml#ema-appraisals"
		#emo.appraisal_set="http://www.w3.org/TR/emotion-voc/xml#scherer-appraisals"
		#rep=Representation('suddenness', 'appraisal')
		#emo.appraisals.append(rep)
		#eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue((doc.documentElement.getAttribute('appraisal-set')) or (), printOutcome("230", 'fail', 'If the <appraisal> element is used, an appraisal vocabulary MUST be declared using an "appraisal-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.'))
		print printOutcome("230", 'pass', 'If the <appraisal> element is used, an appraisal vocabulary MUST be declared using an "appraisal-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.')'''

	def test_231(self):
		eml= EmotionML()
		eml.appraisal_set="http://www.w3.org/TR/emotion-voc/xml#occ-categories"
		try:
			emo= Emotion()
			rep=Representation(representation='appraisal', value='.9')
			emo.categories.append(rep)
			eml.emotions.append(emo)
		except:
			#we expect it to enter here for throwing an exception for not having a name
			pass
		emo=Emotion()
		rep=Representation('urgency', 'appraisal')
		emo.appraisals.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		appraisals= doc.getElementsByTagName('appraisal')
		self.assertTrue(appraisals[0].getAttribute('name'), printOutcome("231", 'fail', 'An appraisal element does not contain a "name" attribute.'))
		print printOutcome("231", 'pass', 'An appraisal element contains a "name" attribute.')
	
	#TODO
	'''
	def test_232(self):
	def test_233(self):
	''' 

	def test_234(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='power', representation='appraisal', value='.5')
		emo.appraisals.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		appraisals= doc.getElementsByTagName('appraisal')
		self.assertTrue(appraisals[0].getAttribute('value'), printOutcome("234", 'fail', 'A <appraisal> can not contain a "value" attribute.'))
		print printOutcome("234", 'pass', 'A <appraisal> MAY contain a "value" attribute.')
	
	def test_235(self):
		eml=EmotionML()
		emo=Emotion()
		trace=Trace(90, [.6, .4, .8])
		rep=Representation('power', 'appraisal', trace)
		emo.appraisals.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.getElementsByTagName('trace'), printOutcome("235", 'fail', 'A <appraisal> can not contain a <trace> element.'))
		print printOutcome("235", 'pass', 'A <appraisal> MAY contain a <trace> element.')

	def test_236(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			trace=Trace(50, [.8, .4, .2])
			rep=Representation(name='control',representation= 'appraisal', trace=trace, value= .5 )
			emo.appraisals.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("236", 'pass', 'A <appraisal> cannot contain both a "value" attribute and a <trace> element.')
			return
		fail( printOutcome("236", 'fail', 'A <appraisal> can contain both a "value" attribute and a <trace> element.'))
			

	def test_237(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='control',representation= 'appraisal', value= .5 , confidence= .8 )
		emo.appraisals.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		appraisals= doc.getElementsByTagName('appraisal')
		self.assertTrue(appraisals[0].hasAttribute('confidence'), printOutcome("237", 'fail', 'A <appraisal> element cannot contain a "confidence" attribute.'))
		print printOutcome("237", 'pass', 'A <appraisal> element MAY contain a "confidence" attribute.')

	#TODO need help!
	'''
	def test_240(self):
		eml= EmotionML()
		emo= Emotion()
		rep=Representation('attending', 'action-tendency')
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		at= doc.getElementsByTagName('action-tendency')
		self.assertTrue((doc.documentElement.getAttribute('action-tendency-set')), printOutcome("240", 'fail', 'If the <action-tendency> element is used, an action tendency vocabulary MUST be declared using an "action-tendency-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.'))
		print printOutcome("240", 'pass', 'If the <action-tendency> element is used, an action tendency vocabulary MUST be declared using an "action-tendency-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.')'''

	def test_241(self):
		eml= EmotionML()
		eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
		try:
			emo= Emotion()
			rep=Representation(representation='action-tendency', value='.9')
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
		except:
			#we expect it to enter here for throwing an exception for not having a name
			pass
		emo=Emotion()
		rep=Representation('nonattending', 'action-tendency')
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		action_tendencies= doc.getElementsByTagName('action-tendency')
		self.assertTrue(action_tendencies[0].getAttribute('name'), printOutcome("241", 'fail', 'An action-tendency element does not contain a "name" attribute.'))
		print printOutcome("241", 'pass', 'An action-tendency element contains a "name" attribute.')
	
	#TODO
	#Check these after checks are implemented
	def test_242(self):
		try:
			eml=EmotionML()
			eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
			emo=Emotion()
			rep=Representation('notSpecifying', 'action-tendency')
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except:
			print printOutcome("242", 'pass', "SUB CONSTRAINT: The value of the 'name' attribute of the <action-tendency> element MUST be contained in the declared action tendency vocabulary. If both the <emotionml> and the <emotion> element has an 'action-tendency-set' attribute, then the <emotion> element's attribute defines the declared action tendency vocabulary.")
			return
		fail(printOutcome("242", 'fail', 'SUB CONSTRAINT: The value of the "name" attribute of the <action-tendency> element MUST be contained in the declared action tendency vocabulary. If both the <emotionml> and the <emotion> element has an "action-tendency-set" attribute, then the <emotion> element\'s attribute defines the declared action tendency vocabulary.'))
	#this should fail
	def test_243(self):
		eml=EmotionML()
		eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
		emo=Emotion()
		rep=Representation('rejecting', 'action-tendency')			
		emo.action_tendencies.append(rep)
		rep=Representation(name='rejecting', representation='action-tendency', value=.4)			
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		print emxml
	
	def test_244(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='nonattending', representation='action-tendency', value='.9')
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		AT= doc.getElementsByTagName('action-tendency')
		self.assertTrue(AT[0].getAttribute('value'), printOutcome("244", 'fail', 'A <action-tendency> can not contain a "value" attribute.'))
		print printOutcome("244", 'pass', 'A <action-tendency> MAY contain a "value" attribute.')
	
	def test_245(self):
		eml=EmotionML()
		emo=Emotion()
		trace=Trace('90Hz', [.6, .4, .8])
		rep=Representation('power', 'action-tendency', trace)
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.getElementsByTagName('trace'), printOutcome("245", 'fail', 'A <action-tendency> can not contain a <trace> element.'))
		print printOutcome("245", 'pass', 'A <action-tendencyl> MAY contain a <trace> element.')

	def test_246(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			trace=Trace('50Hz', [.8, .4, .2])
			rep=Representation(name='approach',representation= 'action-tendency', trace=trace, value= .5 )
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("246", 'pass', 'A <action-tendency> cannot contain both a "value" attribute and a <trace> element.')
			return
		fail(printOutcome("246", 'fail', 'A <action-tendency> can contain both a "value" attribute and a <trace> element.'))
			

	def test_237(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='agonistic',representation= 'action-tendency', value= .7 , confidence= .2 )
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		AT= doc.getElementsByTagName('action-tendency')
		self.assertTrue(AT[0].hasAttribute('confidence'), printOutcome("247", 'fail', 'A <action-tendency> element cannot contain a "confidence" attribute.'))
		print printOutcome("247", 'pass', 'A <action-tendency> element MAY contain a "confidence" attribute.')
	
	def test_300(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation(name='bored', representation='category', value=.8 , confidence=5)
			emo.categories.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("300", "pass", "The value of the 'confidence' attribute must be in the closed interval [0, 1].")
			return
		fail( printOutcome("500", "fail", "The value of the 'confidence' attribute MUST be a floating point number in the closed interval [0, 1]."))
			
	#TODO
	'''def test_301(self):
	def test_302(self):
	def test_303(self):
	def test_304(self):'''

	def test_305(self):
		eml=EmotionML()
		info= Info('information')
		eml.info=info
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		node=doc.getElementsByTagName('info')
		self.assertTrue(node[0].getAttribute('id'), printOutcome('305', 'fail', 'The <info> element MAY contain an attribute "id".'))
		print printOutcome("305","pass","The <info> element MAY contain an attribute 'id'.")

	def test_410(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			ref=Reference()
			emo.references.append(ref)
			rep=Representation('power', 'action-tendency')
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except TypeError:
			print printOutcome("410","pass","The <reference> element requires a 'uri' attribute.")
			return
		fail (printOutcome("410","fail","The <reference> element doesn't contain a 'uri' attribute."))

	def test_413(self):
		eml=EmotionML()
		emo=Emotion()
		ref=Reference("http://some-uri", 'triggeredBy')
		emo.references.append(ref)
		rep=Representation('power', 'action-tendency')
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		refs=doc.getElementsByTagName('reference')
		self.assertTrue(refs[0].hasAttribute('role'), printOutcome("413", 'fail', 'The <reference> element MAY contain a "role" attribute.'))
		print printOutcome("413", 'pass', 'The <reference> element MAY contain a "role" attribute.')

	def test_414(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			ref=Reference("http://some-uri", 'fakeRole')
			emo.references.append(ref)
			rep=Representation('power', 'action-tendency')
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except TypeError:
			print printOutcome("414", 'pass', 'The value of the "role" attribute of the <reference> element, if present, MUST be one of "expressedBy", "experiencedBy", "triggeredBy", "targetedAt".')
			return
		fail(printOutcome("414", 'fail', 'The value of the "role" attribute of the <reference> element, if present, MUST be one of "expressedBy", "experiencedBy", "triggeredBy", "targetedAt".'))
			
	def test_415(self):
		eml=EmotionML()
		emo=Emotion()
		ref=Reference("http://some-uri", 'triggeredBy', 'voice')
		emo.references.append(ref)
		rep=Representation('power', 'action-tendency')
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		refs=doc.getElementsByTagName('reference')
		self.assertTrue(refs[0].hasAttribute('media-type'), printOutcome("415", 'fail', 'The <reference> element cannot contain a "media-type" attribute.'))
		print printOutcome("415", 'pass', 'The <reference> element MAY contain a "media-type" attribute.')
	#TODO
	'''def test_306(self):
	def test_411(self):
	def test_412(self):
	def test_416(self):
	def test_417(self):
	def test_420(self):
	def test_421(self):
	def test_422(self):
	def test_423(self):
	'''
	#need to specify type of exception
	def test_424(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation('deservingness', 'appraisal')
			emo.appraisals.append(rep)
			emo.time_ref_anchor_point= "middle"
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
			doc=parseString(emxml)
			emotions=doc.getElementsByTagName('emotion')
		except:
			print printOutcome('424', 'pass','The value of the "time-ref-anchor-point" attribute of <emotion> is either "start" or "end".')
			return
		fail(printOutcome('424', 'fail','The value of the "time-ref-anchor-point" attribute of <emotion> is not either "start" or "end".'))
			 	
	
	#TODO
	'''
	def test_425(self):
	'''

	def test_500(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation(name='bored', representation='category', value=10)
			emo.categories.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("500", "pass", 'The value of a "value" attribute, if present, MUST be a floating point value from the closed interval [0, 1].')
			return
		fail( printOutcome("500", "fail", "The value of a 'value' attribute, if present, MUST be a floating point value from the closed interval [0, 1]."))
			

	def test_501(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			trace=Trace(samples= [.6, .4, .8])
			rep=Representation('power', 'action-tendency', trace)
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except TypeError:		
			print printOutcome("501", 'fail', 'The <trace> element MUST have a "freq" attribute.')
			return
		fail( printOutcome("501", 'pass', 'The <trace> element MUST have a "freq" attribute.'))
	
	#will need to define the type of exception once created	
	def test_502(self):
 		try:
			eml=EmotionML()
			emo=Emotion()
			trace=Trace(20, [.6, .4, .8])
			rep=Representation('power', 'action-tendency', trace)
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except:
			print printOutcome("502", 'fail', 'The value of the "freq" attribute of <trace> MUST be a positive floating point number followed by optional whitespace followed by "Hz".')
			return
		fail( printOutcome("502", 'pass', 'The value of the "freq" attribute of <trace> MUST be a positive floating point number followed by optional whitespace followed by "Hz".'))
	
	def test_503(self):
		try:
			eml=EmotionML()
			emo=Emotion()
			trace=Trace(20)
			rep=Representation('power', 'action-tendency', trace)
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except TypeError:
			print printOutcome("503", 'fail', 'The <trace> element MUST have a "samples" attribute.')
			return
		fail( printOutcome("503", 'pass', 'The <trace> element MUST have a "samples" attribute.'))

#TODO
#need vocabulary implemented before can really do these
'''
	def test_504(self):
	def test_600(self):
	def test_601(self):
	def test_602(self):
	def test_603(self):
	def test_604(self):
	def test_605(self):
	def test_606(self):
	def test_607(self):
	def test_608(self):
	def test_700(self):'''
		






	


def printOutcome( ID, result, notes ):
	return "<assert id=\"%s\" res=\"%s\">%s</assert>" % (ID,result,notes)	

if __name__ == '__main__':
        unittest.main()
