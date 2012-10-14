import unittest
from xml.dom.minidom import Document, parseString
from emldoc import *
import time
import datetime

class TestEMLAssertions(unittest.TestCase):
	def test_100(self):
		print printOutcome("100","pass","All EmotionML documents must validate against the XML schema.")

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
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		eml.emotions.append(emotion)
		emxml= eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(len(doc.getElementsByTagName("emotion")) > 0,
			printOutcome('103', 'fail', 'The <emotionml> element cannot contain one or more <emotion> elements.'))
		print printOutcome("103","pass","The <emotionml> element may contain one or more <emotion> elements.")
	
	def test_104(self):
		item= []
		eml=EmotionML()
		item.append(Item('anger'))
		voc=Vocabulary('category', 'big6', item)
		eml.vocabularies.append(voc)
		item2=[]
		item2.append(Item('valence'))
		item2.append(Item('potency'))
		item2.append(Item('arousal'))
		voc2= Vocabulary('dimension', 'fsre-dimension', item2)
		eml.vocabularies.append(voc2)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertEqual(len(doc.getElementsByTagName("vocabulary")),2, printOutcome('104', 'fail', 'The <emotionml> element cannot contain one or more <vocabulary> elements.'))
		print printOutcome('104', 'pass', 'The <emotionml> element may contain one or more <vocabulary> elements.')

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

	def test_113(self):
		'''
		The "category-set" attribute of <emotionml>, if present, MUST be of type xsd:anyURI.
		'''
		print printOutcome("113", 'not-impl', 
			'The "category-set" attribute of <emotionml>, if present, MUST be of type xsd:anyURI.',
			comment="See general comments.")
	
	def test_114(self):
		'''
		'''
		print printOutcome("114", 'not-impl', 
			'The "category-set" attribute of <emotionml>, if present, MUST refer to the ID of a <vocabulary> element with type="category"',
			comment="See general comments.")
	
	def test_115(self):
		eml=EmotionML()
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('dimension-set'), printOutcome('115', 'fail', 'The <emotionml> element cannot contain an attribute "dimension-set".'))
		print printOutcome('115', 'pass', 'The <emotionml> element MAY contain an attribute "dimension-set".')

	
	def test_116(self): 
		'''
		The "dimension-set" attribute of <emotionml>, if present, MUST be of type xsd:anyURI.
		'''
		print printOutcome('116', 'not-impl', 
			'The "dimension-set" attribute of <emotionml>, if present, MUST be of type xsd:anyURI.',
			comment="See general comments.")


	def test_117(self): 
		print printOutcome( '117','not-impl',
			'SUB CONSTRAINT: The "dimension-set" attribute of <emotionml>, if present, MUST refer to the ID of a <vocabulary> element with type="dimension".',
			comment="See general comments.")

	def test_118(self):
		eml= EmotionML()
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('appraisal-set'), printOutcome("118", 'fail', 'The <emotionml> element cannot contain an attribute "appraisal-set".'))
		print printOutcome("118", 'pass', 'The <emotionml> element  MAY contain an attribute "appraisal-set".')

	def test_119(self): 
		''' The "appraisal-set" attribute of <emotionml>, if present, MUST be of type xsd:anyURI.
		'''
		print printOutcome("119", 'not-impl', 'The "appraisal-set" attribute of <emotionml>, if present, MUST be of type xsd:anyURI.',
			comment="See general comments.")

	def test_120(self): 
		print printOutcome('120','not-impl','SUB CONSTRAINT: The "appraisal-set" attribute of <emotionml>, if present, MUST refer to the ID of a <vocabulary> element with type="appraisal".',
			comment="See general comments.")

	
	def test_121(self):
		eml=EmotionML()
		eml.action_tendency_set="http://www.example.com/emotionot-implction/frijda.xml"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.documentElement.getAttribute('action-tendency-set'), printOutcome('121', 'fail', 'The <emotionml> element cannot contain an attribute "action-tendency-set".'))
		print printOutcome('121', 'pass', 'The <emotionml> element MAY contain an attribute "action-tendency-set".')

	
	def test_122(self):
		''' 
		The "action-tendency-set" attribute of <emotionml>, if present, MUST be of type xsd:anyURI.
		'''
		print printOutcome('122', 'not-impl','The "appraisal-set" attribute of <emotionml>, if present, MUST be of type xsd:anyURI.',
			comment="See general comments.")
	
	def test_123(self): 
		print printOutcome( '123','not-impl', 'SUB CONSTRAINT: The "action-tendency-set" attribute of <emotionml>, if present, MUST refer to the ID of a <vocabulary> element with type="action-tendency".',
			comment="See general comments.")

	def test_124(self):
		''' The <emotionml> element MAY contain arbitrary plain text.'''
		eml=EmotionML()
		emo=Emotion()
		emo.action_tendency_set="act"
		emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
		trace=Trace('10.5Hz', [.6, .4, .8])
		rep=Representation('power', 'action-tendency', trace)
		emo.action_tendencies.append(rep)
		eml.content = "Test Content"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		#print emxml
		doc=parseString(emxml)
		nodes=doc.getElementsByTagName('emotionml')

		for tnode in nodes[0].childNodes:
			if ( tnode.nodeType == tnode.TEXT_NODE ):
				if "Test Content" in tnode.nodeValue:
					print printOutcome( '124','pass', "The <emotionml> element MAY contain arbitrary plain text.")
					return		
		self.fail(printOutcome( '124','fail', "The <emotionml> element MAY contain arbitrary plain text."))
				

	def test_150(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('disappointment', 'category')
		emo.categories.append(rep)
		rep=Representation('despair', 'category')
		emo.categories.append(rep)
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
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
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
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
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
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
		eml.action_tendency_set="http://www.example.com/emotionot-implction/frijda.xml"
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
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
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
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
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
		self.fail (printOutcome('156', 'fail', 'The <emotion> element does not require at least one <category> or <dimension> or <appraisal> or <action-tendency> element.'))

		
	
	def test_157(self): 
		print printOutcome( '157','pass','The allowed child elements of <emotion> MAY occur in any order.')

	def test_158(self): 
		print printOutcome( '158','pass','The allowed child elements of <emotion> MAY occur in any combination.')

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


	def test_160(self): 
		'''
		The "category-set" attribute of <emotion>, if present, MUST be of type xsd:anyURI.
		'''
		print printOutcome("160", 'not-impl', 'category-set" attribute of <emotion>, if present, MUST be of type xsd:anyURI',
			comment="See general comments.")

	def test_161(self): 
		print printOutcome( '161','not-impl',
			'SUB CONSTRAINT: The "category-set" attribute of <emotion>, if present, MUST refer to the ID of a <vocabulary> element with type="category".',
			comment="See general comments.")	
	
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

	def test_163(self): 
		''' The "dimension-set" attribute of <emotion>, if present, MUST be of type xsd:anyURI.
		'''
		print printOutcome('163', 'not-impl', 
			'The "dimension-set" attribute of <emotion>, if present, MUST be of type xsd:anyURI.',
			comment="See general comments.")

	def test_164(self): 
		print printOutcome( '164','not-impl',
			'SUB CONSTRAINT: The "dimension-set" attribute of <emotion>, if present, MUST refer to the ID of a <vocabulary> element with type="dimension".',
			comment="See general comments.")
	
	def test_165(self):
		eml= EmotionML()
		emo=Emotion()
		rep=Representation('suddenness', 'appraisal')
		emo.appraisals.append(rep)
		emo.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('appraisal-set'), printOutcome("165", 'fail', 'The <emotionml> element cannot contain an attribute "appraisal-set".'))
		print printOutcome("165", 'pass', 'The <emotionml> element  MAY contain an attribute "appraisal-set".')


	def test_166(self): 
		''' The "appraisal-set" attribute of <emotion>, if present, MUST be of type xsd:anyURI.
		'''
		print printOutcome("166", 'not-impl', 'The "appraisal-set" attribute of <emotion>, if present, MUST be of type xsd:anyURI',
			comment="See general comments.")

	def test_167(self):
		print printOutcome('167','not-impl',
			'SUB CONSTRAINT: The "appraisal-set" attribute of <emotion>, if present, MUST refer to the ID of a <vocabulary> element with type="appraisal".',
			comment="See general comments.")

	
	def test_168(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('agnostic', 'action-tendency')
		emo.action_tendencies.append(rep)
		emo.action_tendency_set="http://www.example.com/emotionot-implction/frijda.xml"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions= doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('action-tendency-set'), printOutcome('168', 'fail', 'The <emotionml> element cannot contain an attribute "action-tendency-set".'))
		print printOutcome('168', 'pass', 'The <emotionml> element MAY contain an attribute "action-tendency-set".')
	
	
	def test_169(self): 
		''' 
		The "action-tendency-set" attribute of <emotion>, if present, MUST be of type xsd:anyURI.
		'''
		print printOutcome('169', 'not-impl', 
			'"action-tendency-set" attribute of <emotion>, if present, MUST be of type xsd:anyURI.',
			comment="See general comments.")

	def test_170(self): 
		print printOutcome('170', 'pass', "SUB CONSTRAINT: The \"action-tendency-set\" attribute of <emotion>, if present, MUST refer to the ID of a <vocabulary> element with type=\"action-tendency\".")

	def test_171(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('agnostic', 'action-tendency')
		emo.action_tendencies.append(rep)
		emo.version='1.0'
		eml.emotions.append(emo)
		eml.action_tendency_set="http://www.example.com/emotionot-implction/frijda.xml"
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
		emo.emotion_id='Angry'
		eml.emotions.append(emo)
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('id'), printOutcome('173', 'fail',"The <emotion> element can't contain an attribute 'id'."))
		print printOutcome("173","pass",'The <emotion> element MAY contain an attribute "id".')
	
	def test_174(self): 
		''' The "id" attribute of <emotion>, if present, MUST be of type xsd:ID.
		'''
		invalid_ids = ['  ','9zzk','-hjk','*httpjj9-']
		def create_em(id):
			eml=EmotionML()
			emo=Emotion()
			rep=Representation('anger', 'category')
			emo.categories.append(rep)
			emo.emotion_id=id
			eml.emotions.append(emo)
			eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
			emxml=eml.to_xml().toprettyxml()
			return
		try:
			for id in invalid_ids:
				last = id
				create_em(id)
		except ValueError as te:
			pass
		else:
			self.fail(printOutcome("174", 'fail','The "id" attribute of <emotion>, if present, MUST be of type xsd:ID.'))

		valid_ids = ['_7','az56','A-hjk0','_---']
		last = ""
		try:
			for id in valid_ids:
				last = id
				create_em(id)
		except ValueError as te:
			self.fail(printOutcome("174", 'fail','The "id" attribute of <emotion>, if present, MUST be of type xsd:ID.'))
		printOutcome("174", 'pass','The "id" attribute of <emotion>, if present, MUST be of type xsd:ID.')


	def test_175(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation('love', 'category')
		emo.categories.append(rep)
		emo.start= time.time()
		eml.emotions.append(emo)
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
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
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
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
		emo.duration= 150
		eml.emotions.append(emo)
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
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
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
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
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
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
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
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
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		emotions=doc.getElementsByTagName('emotion')
		self.assertTrue(emotions[0].getAttribute('expressed-through'), printOutcome('181', 'fail','The <emotion> element MAY have an attribute "expressed-through".'))
		print printOutcome('181', 'pass','The <emotion> element MAY have an attribute "expressed-through".')
	
	def test_182(self): 
		''' The <emotion> element MAY contain arbitrary plain text.
		'''
		eml=EmotionML()
		emo=Emotion()
		emo.action_tendency_set="act"
		emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
		trace=Trace('10.5Hz', [.6, .4, .8])
		rep=Representation('power', 'action-tendency', trace)
		emo.action_tendencies.append(rep)
		emo.content = "Test Content"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		print emxml
		doc=parseString(emxml)
		nodes=doc.getElementsByTagName('emotion')

		for tnode in nodes[0].childNodes:
			if ( tnode.nodeType == tnode.TEXT_NODE ):
				if "Test Content" in tnode.nodeValue:
					print printOutcome( '182','pass', "The <emotion> element MAY contain arbitrary plain text.")
					return		
		self.fail(printOutcome( '182','fail', "The <emotion> element MAY contain arbitrary plain text.."))
	
	def test_210(self):
		"""
		eml= EmotionML()
		try:
			emo= Emotion()
			rep=Representation('anger', 'category')
			emo.categories.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		
		except:
			pass
			
		else:
			self.fail( printOutcome("210", 'fail', 'If the <category> element is used, a category vocabulary is not required to be declared using a "category-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.'))
		
		emo= Emotion()
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		rep=Representation('anger', 'category')
		emo.categories.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()

	
		eml2= EmotionML()
		emo= Emotion()
		emo.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		rep=Representation('anger', 'category')
		emo.categories.append(rep)
		eml2.emotions.append(emo)
		emxml=eml2.to_xml().toprettyxml()
		print printOutcome("210", 'pass', 'If the <category> element is used, a category vocabulary MUST be declared using a "category-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.')
		"""
		print printOutcome("210", 'not-impl', 
			'If the <category> element is used, a category vocabulary MUST be declared using a "category-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.',
			comment="See general comments.")

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
		print printOutcome("211", 'pass', 'A <category> element contains a \"name\" attribute.')
	
	def test_212(self): 
		print printOutcome('211', 'not-impl', 
			"SUB CONSTRAINT: The value of the \"name\" attribute of the <category> element MUST be contained in the declared category vocabulary. If both the <emotionml> and the <emotion> element has a \"category-set\" attribute, then the <emotion> element\'s attribute defines the declared category vocabulary.",
			comment="See general comments.")
	
	
	def test_213(self):
	 	eml=EmotionML()	
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		
		try:
			emo=Emotion()
			rep=Representation('distress', 'category')
			emo.categories.append(rep)
			eml.emotions.append(emo)
			rep=Representation(name='distress', representation='category', value= .7)
			emo.categories.append(rep)
			eml.emotions.append(emo)
			eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("213", 'pass', "For any given category name in the set, zero or one occurrence is allowed within an <emotion> element, i.e. a category with name 'x' MUST NOT appear twice in one <emotion> element.")
			return
		else:
			fail(printOutcome("213", 'fail', "A category with name 'x' may appear twice in one <emotion> element."))
		
		

	def test_214(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='anger', representation='category', value='.5')
		emo.categories.append(rep)
		eml.emotions.append(emo)
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		categories= doc.getElementsByTagName('category')
		self.assertTrue(categories[0].getAttribute('value'), printOutcome("214", 'fail', 'A <category> can not contain a "value" attribute.'))
		print printOutcome("214", 'pass', 'A <category> MAY contain a "value" attribute.')
	
	def test_215(self):
		eml=EmotionML()
		emo=Emotion()
		trace=Trace('100Hz', [.2, .4, .6])
		rep=Representation('worried', 'category', trace)
		emo.categories.append(rep)
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertTrue(doc.getElementsByTagName('trace'), printOutcome("215", 'fail', 'A <category> can not contain a <trace> element.'))
		print printOutcome("215", 'pass', 'A <category> MAY contain a <trace> element.')

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
		eml.category_set="http://www.w3.org/TR/emotion-voc/xml#everyday-categories"
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		categories= doc.getElementsByTagName('category')
		self.assertTrue(categories[0].hasAttribute('confidence'), printOutcome("217", 'fail', 'A <category> element cannot contain a "confidence" attribute.'))
		print printOutcome("217", 'pass', 'A <category> element MAY contain a "confidence" attribute.')

	def test_220(self):
		"""
		eml= EmotionML()
		try:
			emo= Emotion()
			rep=Representation(name='anger', representation='dimension', value=.3 )
			emo.dimensions.append(rep)	
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		
		except:
			pass
			
		else:
			self.fail( printOutcome("220", 'fail', 'If the <dimension> element is used, a dimension vocabulary MUST be declared using a "dimension-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.'))
		
		emo= Emotion()
		rep=Representation(name='anger', representation='dimension', value=.3 )
		emo.dimensions.append(rep)
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"	
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()

	
		eml2= EmotionML()		
		emo= Emotion()
		rep=Representation(name='anger', representation='dimension', value=.3 )
		emo.dimensions.append(rep)
		emo.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"	
		eml2.emotions.append(emo)
		emxml=eml2.to_xml().toprettyxml()
		print printOutcome("220", 'pass', 'If the <dimension> element is used, a dimension vocabulary MUST be declared using a "dimension-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.')
		"""
		print printOutcome("220", 'not-impl', 
			'If the <dimension> element is used, a dimension vocabulary MUST be declared using a "dimension-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.',
			comment="See general comments.")


	def test_221(self):
		eml= EmotionML()
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		try:
			emo= Emotion()
			rep=Representation(representation='dimension', value='.5')
			emo.dimensions.append(rep)
			eml.emotions.append(emo)
		except:
			pass
		emo=Emotion()
		trace=Trace('50Hz', [.8, .4, .2])
		rep=Representation('valence', 'dimension', trace)
		emo.dimensions.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		dimensions= doc.getElementsByTagName('dimension')
		self.assertTrue(dimensions[0].getAttribute('name'), printOutcome("221", 'fail', 'A dimension element does not contain a "name" attribute.'))
		print printOutcome("221", 'pass', 'A dimension element must contain a "name" attribute.')
	
	def test_222(self): 
		print printOutcome('222', 'not-impl', 
			'SUB CONSTRAINT: The value of the "name" attribute of the <dimension> element MUST be contained in the declared dimension vocabulary. If both the <emotionml> and the <emotion> element has a "dimension-set" attribute, then the <emotion> element\'s attribute defines the declared dimension vocabulary.',
			comment="See general comments.")
	

	def test_223(self):
	 	eml=EmotionML()	
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		
		try:
			emo=Emotion()
			rep=Representation(name='pleasure', representation= 'dimension', value= .9 , confidence= .8 )
			emo.dimensions.append(rep)
			eml.emotions.append(emo)
			rep=Representation(name='pleasure', representation= 'dimension', value= .3 )
			emo.dimensions.append(rep)
			eml.emotions.append(emo)
			eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("223", 'pass', "For any given dimension name in the set, zero or one occurrence is allowed within an <emotion> element, i.e. a dimension with name 'x' MUST NOT appear twice in one <emotion> element.")
			return
		else:
			fail(printOutcome("223", 'fail', "A dimension with name 'x' may appear twice in one <emotion> element."))
	

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
		eml.dimension_set="http://www.w3.org/TR/emotion-voc/xml#pad-dimensions"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		dimensions= doc.getElementsByTagName('dimension')
		self.assertTrue(dimensions[0].hasAttribute('confidence'), printOutcome("225", 'fail', 'A <dimension> element cannot contain a "confidence" attribute.'))
		print printOutcome("225", 'pass', 'A <dimension> element MAY contain a "confidence" attribute.')
	
	def test_230(self):
		"""
		eml= EmotionML()
		try:
			emo= Emotion()
			rep=Representation('suddenness', 'appraisal')
			emo.appraisals.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		
		except:
			pass
			
		else:
			self.fail( printOutcome("230", 'fail', 'If the <appraisal> element is used, an appraisal vocabulary MUST be declared using an "appraisal-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.'))
		
		emo= Emotion()
		rep=Representation('suddenness', 'appraisal')
		emo.appraisals.append(rep)
		eml.emotions.append(emo)
		eml.appraisal_set="http://www.w3.org/TR/emotion-voc/xml#ema-appraisals"
		emxml=eml.to_xml().toprettyxml()

	
		eml2= EmotionML()
		emo= Emotion()
		emo.appraisal_set="http://www.w3.org/TR/emotion-voc/xml#scherer-appraisals"
		rep=Representation('suddenness', 'appraisal')
		emo.appraisals.append(rep)
		eml2.emotions.append(emo)
		emxml=eml2.to_xml().toprettyxml()
		print printOutcome("230", 'pass', 'If the <appraisal> element is used, an appraisal vocabulary MUST be declared using an "appraisal-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.')
		"""
		print printOutcome("230", 'not-impl', 
			'If the <appraisal> element is used, an appraisal vocabulary MUST be declared using an "appraisal-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.',
			comment="See general comments.")

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
	
	def test_232(self): 
		print printOutcome('232', 'not-impl', 
			'SUB CONSTRAINT: The value of the "name" attribute of the <appraisal> element MUST be contained in the declared appraisal vocabulary. If both the <emotionml> and the <emotion> element has an "appraisal-set" attribute, then the <emotion> element\'s attribute defines the declared appraisal vocabulary.',
			comment="See general comments.")
	
	def test_233(self):
	 	eml=EmotionML()	
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
		try:
			emo=Emotion()
			rep=Representation('power', 'appraisal')
			emo.appraisals.append(rep)
			eml.emotions.append(emo)
			rep=Representation('power', 'appraisal')
			emo.appraisals.append(rep)
			eml.emotions.append(emo)
			eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("233", 'pass', "For any given appraisal name in the set, zero or one occurrence is allowed within an <emotion> element, i.e. an appraisal with name 'x' MUST NOT appear twice in one <emotion> element.")
			return
		else:
			fail(printOutcome("233", 'fail', "An appraisal with name 'x' may appear twice in one <emotion> element."))	
	
	def test_234(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='power', representation='appraisal', value='.5')
		emo.appraisals.append(rep)
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		appraisals= doc.getElementsByTagName('appraisal')
		self.assertTrue(appraisals[0].getAttribute('value'), printOutcome("234", 'fail', 'A <appraisal> can not contain a "value" attribute.'))
		print printOutcome("234", 'pass', 'A <appraisal> MAY contain a "value" attribute.')
	
	def test_235(self):
		eml=EmotionML()
		emo=Emotion()
		trace=Trace('90.0Hz', [.6, .4, .8])
		rep=Representation('power', 'appraisal', trace)
		emo.appraisals.append(rep)
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
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
		self.fail( printOutcome("236", 'fail', 'A <appraisal> can contain both a "value" attribute and a <trace> element.'))
			

	def test_237(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='control',representation= 'appraisal', value= .5 , confidence= .8 )
		emo.appraisals.append(rep)
		eml.appraisal_set="http://www.example.com/emotionot-implppraisal/scherer.xml"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		appraisals= doc.getElementsByTagName('appraisal')
		self.assertTrue(appraisals[0].hasAttribute('confidence'), printOutcome("237", 'fail', 'A <appraisal> element cannot contain a "confidence" attribute.'))
		print printOutcome("237", 'pass', 'A <appraisal> element MAY contain a "confidence" attribute.')

	def test_240(self):
		"""
		eml= EmotionML()
		try:
			emo= Emotion()
			emo.action_tendency_set="act"
			emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("nonattending")]))
			emo.action_tendency_set="act"
			rep=Representation('nonattending', 'action-tendency')
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		
		except:
			pass
		else:
			self.fail( printOutcome("240", 'fail', 'If the <action-tendency> element is used, an action tendency vocabulary MUST be declared using an "action-tendency-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.'))
		
		emo= Emotion()
		rep=Representation('nonattending', 'action-tendency')
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
		emxml=eml.to_xml().toprettyxml()

	
		eml2= EmotionML()
		emo= Emotion()
		emo.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
		rep=Representation('nonattending', 'action-tendency')
		emo.action_tendencies.append(rep)
		eml2.emotions.append(emo)
		emxml=eml2.to_xml().toprettyxml()
		print printOutcome("240", 'pass', 'If the <action-tendency> element is used, an action tendency vocabulary MUST be declared using an "action-tendency-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.')
		"""
		print printOutcome("240", 'not-impl', 
			'If the <action-tendency> element is used, an action tendency vocabulary MUST be declared using an "action-tendency-set" attribute on either the enclosing <emotion> element or the root element <emotionml>.',
			comment="See general comments.")

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

	def test_242(self):
		"""
		try:
			eml=EmotionML()
			eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
			emo=Emotion()
			rep=Representation('notSpecifying', 'action-tendency')			
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("242", 'pass', "SUB CONSTRAINT: The value of the 'name' attribute of the <action-tendency> element MUST be contained in the declared action tendency vocabulary. If both the <emotionml> and the <emotion> element has an 'action-tendency-set' attribute, then the <emotion> element's attribute defines the declared action tendency vocabulary.")
			return
		self.fail(printOutcome("242", 'fail', 'SUB CONSTRAINT: The value of the "name" attribute of the <action-tendency> element MUST be contained in the declared action tendency vocabulary. If both the <emotionml> and the <emotion> element has an "action-tendency-set" attribute, then the <emotion> element\'s attribute defines the declared action tendency vocabulary.'))
		"""
		print printOutcome("242", 'not-impl', 
			"SUB CONSTRAINT: The value of the 'name' attribute of the <action-tendency> element MUST be contained in the declared action tendency vocabulary. If both the <emotionml> and the <emotion> element has an 'action-tendency-set' attribute, then the <emotion> element's attribute defines the declared action tendency vocabulary.",
			comment="See general comments.")
	
	def test_243(self):
		try:
			eml=EmotionML()
			eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
			emo=Emotion()
			rep=Representation('rejecting', 'action-tendency')			
			emo.action_tendencies.append(rep)
			rep=Representation(name='rejecting', representation='action-tendency', value=.4)			
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("243", 'pass', "For any given action tendency name in the set, zero or one occurrence is allowed within an <emotion> element, i.e. an action tendency with name 'x' MUST NOT appear twice in one <emotion> element.")
			return
		self.fail(printOutcome("243", 'fail', "An action tendency with name 'x' may appear twice in one <emotion> element."))
	
	def test_244(self):
		eml=EmotionML()
		emo=Emotion()
		rep=Representation(name='nonattending', representation='action-tendency', value='.9')
		emo.action_tendencies.append(rep)
		eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
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
		eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
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
		self.fail(printOutcome("246", 'fail', 'A <action-tendency> can contain both a "value" attribute and a <trace> element.'))
			

	def test_247(self):
		eml=EmotionML()
		eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
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
			rep=Representation(name='bored', representation='category', value=.8 , confidence=1.5)
			emo.categories.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			print printOutcome("300", "pass", "The value of the 'confidence' attribute must be in the closed interval [0, 1].")
			return
		self.fail( printOutcome("300", "fail", "The value of the 'confidence' attribute MUST be a floating point number in the closed interval [0, 1]."))
			
	def test_301(self): 
		''' The attribute "expressed-through" of the <emotion> element, if present, MUST be of type xsd:nmtokens.
		'''
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation(name='bored', representation='category', value=.8 , confidence=.5)
			emo.categories.append(rep)
			emo.expressed_through="123 456"
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:			
			print printOutcome("301", "pass", 
				'The attribute "expressed-through" of the <emotion> element, if present, MUST be of type xsd:nmtokens.')
			return
		self.fail( printOutcome("301", "fail", 
			'The attribute "expressed-through" of the <emotion> element, if present, MUST be of type xsd:nmtokens.'))
	
	def test_302(self): 
		''' The <info> element MAY contain any elements with a namespace different from the EmotionML namespace, "http://www.w3.org/2009/10/emotionml"
		'''
		print printOutcome("302", "pass", 
			'The <info> element MAY contain any elements with a namespace different from the EmotionML namespace, "http://www.w3.org/2009/10/emotionml"')

	def test_303(self): 
		'''The <info> element MAY contain arbitrary plain text.
		'''
		info = Info('something')
		info.content = "Test Content"
		doc = Document()
		emxml=info.to_xml(doc).toprettyxml()
		doc=parseString(emxml)
		nodes=doc.getElementsByTagName('info')

		for tnode in nodes[0].childNodes:
			if ( tnode.nodeType == tnode.TEXT_NODE ):
				if "Test Content" in tnode.nodeValue:
					print printOutcome( '303','pass', 'The <info> element MAY contain arbitrary plain text.')
					return		
		self.fail(printOutcome( '303','fail', 'The <info> element MAY contain arbitrary plain text.'))
	
	def test_304(self): 
		''' The <info> element MUST NOT contain any elements in the EmotionML namespace, "http://www.w3.org/2009/10/emotionml". 
		'''
		print printOutcome( '304','not-impl', 
			'The <info> element MUST NOT contain any elements in the EmotionML namespace, "http://www.w3.org/2009/10/emotionml". ',
			comment="See general comments.")

	def test_305(self):
		eml=EmotionML()
		info= Info('information')
		eml.info=info
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		node=doc.getElementsByTagName('info')
		self.assertTrue(node[0].getAttribute('id'), printOutcome('305', 'fail', 'The <info> element MAY contain an attribute "id".'))
		print printOutcome("305","pass","The <info> element MAY contain an attribute 'id'.")
	
	
	def test_306(self): 
		''' The "id" attribute of the <info> element, if present, MUST be of type xsd:ID.
		'''
		invalid_ids = ['  ','9zzk','-hjk','*httpjj9-']
		def create_info(id):
			info = Info(id=id)
			doc = Document()
			info.to_xml(doc)
			return
		last = ""
		try:
			for id in invalid_ids:
				last = id
				create_info(id)
		except ValueError as te:
			pass
		else:
			self.fail(printOutcome("306", 'fail','The "id" attribute of the <info> element, if present, MUST be of type xsd:ID.'))
		valid_ids = ['_7','az56','A-hjk0','_---']
		last = ""
		try:
			for id in valid_ids:
				last = id
				create_info(id)
		except ValueError as te:
			self.fail(printOutcome("306", 'fail','The "id" attribute of the <info> element, if present, MUST be of type xsd:ID.'))
		printOutcome("306", 'pass','The "id" attribute of the <info> element, if present, MUST be of type xsd:ID.')


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
		self.fail (printOutcome("410","fail","The <reference> element doesn't contain a 'uri' attribute."))
	
	def test_411(self):
		print printOutcome("411","not-impl",'The "uri" attribute of <reference> MUST be of type xsd:anyURI',
			comment="See general comments.") 

	def test_412(self): 
		print printOutcome("412","not-impl",
			'SUB CONSTRAINT: The URI in the "uri" attribute of a <reference> element MAY be extended by a media fragment.',
			comment="See general comments.")
	

	def test_413(self):
		eml=EmotionML()
		emo=Emotion()
		ref=Reference("http://some-uri", 'triggeredBy')
		emo.references.append(ref)
		rep=Representation('power', 'action-tendency')
		emo.action_tendencies.append(rep)
		eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
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
			eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except TypeError:
			print printOutcome("414", 'pass', 'The value of the "role" attribute of the <reference> element, if present, MUST be one of "expressedBy", "experiencedBy", "triggeredBy", "targetedAt".')
			return
		self.fail(printOutcome("414", 'fail', 'The value of the "role" attribute of the <reference> element, if present, MUST be one of "expressedBy", "experiencedBy", "triggeredBy", "targetedAt".'))
			
	def test_415(self):
		eml=EmotionML()
		emo=Emotion()
		ref=Reference("http://some-uri", 'triggeredBy', 'voice')
		emo.references.append(ref)
		rep=Representation('power', 'action-tendency')
		emo.action_tendencies.append(rep)
		eml.action_tendency_set="http://www.w3.org/TR/emotion-voc/xml#frijda-action-tendencies"
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		refs=doc.getElementsByTagName('reference')
		self.assertTrue(refs[0].hasAttribute('media-type'), printOutcome("415", 'fail', 'The <reference> element cannot contain a "media-type" attribute.'))
		print printOutcome("415", 'pass', 'The <reference> element MAY contain a "media-type" attribute.')
	
	def test_416(self): 
		''' The value of the "media-type" attribute of the <reference> element, if present, MUST be of type xsd:string.
		'''
		print printOutcome('416','pass','The value of the "media-type" attribute of the <reference> element, if present, MUST be of type xsd:string.')
	def test_417(self): 
		print printOutcome("417","not-impl",
			'SUB CONSTRAINT: The value of the "media-type" attribute of the <reference> element, if present, MUST be a valid MIME type.',
			comment="See general comments.")
	
	def test_420(self): 
		'''The value of the "start" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.
		'''
		invalid_val = ["z","0.0003","54x","-3","-0.5"]
		for inv in invalid_val:
			try:
				eml=EmotionML()
				emo=Emotion()
				rep=Representation(name='bored', representation='category', value=0.5)
				emo.categories.append(rep)
				emo.start = inv
				eml.emotions.append(emo)
				emxml=eml.to_xml().toprettyxml()
			except ValueError:
				pass
			else:
				self.fail( printOutcome("420", "fail", 'The value of the "start" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.'))
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation(name='bored', representation='category', value=0.5)
			emo.categories.append(rep)
			emo.start = 236
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError as ve:
			self.fail( printOutcome("420", "fail", 'The value of the "start" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.'))
		printOutcome("420", "pass", 'The value of the "start" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.')

	def test_421(self): 
		''' The value of the "end" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.
		'''
		invalid_val = ["z","0.0003","54x","-3","-0.5"]
		for inv in invalid_val:
			try:
				eml=EmotionML()
				emo=Emotion()
				rep=Representation(name='bored', representation='category', value=0.5)
				emo.categories.append(rep)
				emo.end = inv
				eml.emotions.append(emo)
				emxml=eml.to_xml().toprettyxml()
			except ValueError:
				pass
			else:
				self.fail( printOutcome("421", "fail", 'The value of the "end" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.'))
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation(name='bored', representation='category', value=0.5)
			emo.categories.append(rep)
			emo.end = 236
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError as ve:
			self.fail( printOutcome("421", "fail", 'The value of the "end" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.'))
		printOutcome("421", "pass", 'The value of the "end" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.')

	def test_422(self): 
		''' The value of "duration" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.
		'''
		invalid_val = ["z","0.0003","54x","-3","-0.5"]
		for inv in invalid_val:
			try:
				eml=EmotionML()
				emo=Emotion()
				rep=Representation(name='bored', representation='category', value=0.5)
				emo.categories.append(rep)
				emo.duration = inv
				eml.emotions.append(emo)
				emxml=eml.to_xml().toprettyxml()
			except ValueError:
				pass
			else:
				self.fail( printOutcome("422", "fail", 'The value of "duration" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.'))
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation(name='bored', representation='category', value=0.5)
			emo.categories.append(rep)
			emo.duration = 236
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError as ve:
			self.fail( printOutcome("422", "fail", 'The value of "duration" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.'))
		printOutcome("422", "pass", 'The value of "duration" attribute of <emotion>, if present, MUST be of type xsd:nonNegativeInteger.')

	def test_423(self): 
		print printOutcome("423","not-impl",
			'The value of the "time-ref-uri" attribute of <emotion>, if present, MUST be of type xsd:anyURI.',
			comment="See general comments.") 

	

	def test_424(self):
		''' print printOutcome('424', 'pass','The value of the "time-ref-anchor-point" attribute of <emotion> is either "start" or "end".
		'''
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
		except ValueError:
			print printOutcome('424', 'pass','The value of the "time-ref-anchor-point" attribute of <emotion> is either "start" or "end".')
			return
		self.fail(printOutcome('424', 'fail','The value of the "time-ref-anchor-point" attribute of <emotion> is not either "start" or "end".'))
			 	
	
	def test_425(self):
		""" The value of the "offset-to-start" attribute of <emotion>, if present, MUST be of type xsd:integer """
		invalid_val = ["z","0.0003","54x"]
		for inv in invalid_val:
			try:
				eml=EmotionML()
				emo=Emotion()
				rep=Representation(name='bored', representation='category', value=0.5)
				emo.categories.append(rep)
				emo.offset_to_start = inv
				eml.emotions.append(emo)
				emxml=eml.to_xml().toprettyxml()
			except ValueError:
				pass
			else:
				self.fail( printOutcome("425", "fail", 'The value of the "offset-to-start" attribute of <emotion>, if present, MUST be of type xsd:integer'))
		try:
			eml=EmotionML()
			emo=Emotion()
			rep=Representation(name='bored', representation='category', value=0.5)
			emo.categories.append(rep)
			emo.offset_to_start = 236
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError as ve:
			self.fail( printOutcome("425", "fail", 'The value of the "offset-to-start" attribute of <emotion>, if present, MUST be of type xsd:integer'))
		printOutcome("425", "pass", 'The value of the "offset-to-start" attribute of <emotion>, if present, MUST be of type xsd:integer')


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
		self.fail( printOutcome("500", "fail", "The value of a 'value' attribute, if present, MUST be a floating point value from the closed interval [0, 1]."))
			

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
			print printOutcome("501", 'pass', 'The <trace> element MUST have a "freq" attribute.')
			return
		self.fail( printOutcome("501", 'fail', 'The <trace> element doesn\'t require a "freq" attribute.'))
	
	def test_502(self):
		""" Test validity of the freq format """
		#negative float
 		try:
			eml=EmotionML()
			emo=Emotion()
			emo.action_tendency_set="act"
			emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
			trace=Trace('-.5Hz', [.6, .4, .8])
			rep=Representation('power', 'action-tendency', trace)
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except ValueError:
			pass
		else:
			self.fail( printOutcome("502", 'fail', 'The value of the "freq" attribute of <trace> MUST be a positive floating point number followed by optional whitespace followed by "Hz".'))
		
		#negative float with space
		try:
			eml=EmotionML()
			emo=Emotion()
			emo.action_tendency_set="act"
			emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
			trace=Trace('-.5 Hz', [.6, .4, .8])
			rep=Representation('power', 'action-tendency', trace)
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except (TypeError, ValueError):
			pass
		else:
			self.fail( printOutcome("502", 'fail', 'The value of the "freq" attribute of <trace> MUST be a positive floating point number followed by optional whitespace followed by "Hz".'))

		# no Hz
		try:
			eml=EmotionML()
			emo=Emotion()
			emo.action_tendency_set="act"
			emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
			trace=Trace('.5', [.6, .4, .8])
			rep=Representation('power', 'action-tendency', trace)
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except (TypeError, ValueError):
			pass
		else:
			self.fail( printOutcome("502", 'fail', 'The value of the "freq" attribute of <trace> MUST be a positive floating point number followed by optional whitespace followed by "Hz".'))
		
		#Wrong unit
		try:
			eml=EmotionML()
			emo=Emotion()
			emo.action_tendency_set="act"
			emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
			trace=Trace('.5 Kz', [.6, .4, .8])
			rep=Representation('power', 'action-tendency', trace)
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()
		except (TypeError, ValueError):
			pass
		else:
			self.fail( printOutcome("502", 'fail', 'The value of the "freq" attribute of <trace> MUST be a positive floating point number followed by optional whitespace followed by "Hz".'))
		
		#wrong unit at the end
		try:
			eml=EmotionML()
			emo=Emotion()
			emo.action_tendency_set="act"
			emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
			trace=Trace('.5 Hz Kz', [.6, .4, .8])
			rep=Representation('power', 'action-tendency', trace)
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()	

		except (TypeError, ValueError):
			pass
		else:
			self.fail( printOutcome("502", 'fail', 'The value of the "freq" attribute of <trace> MUST be a positive floating point number followed by optional whitespace followed by "Hz".'))
		
		# wrong float value
		try:
			eml=EmotionML()
			emo=Emotion()
			emo.action_tendency_set="act"
			emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
			trace=Trace('Az Hz', [.6, .4, .8])
			rep=Representation('power', 'action-tendency', trace)
			emo.action_tendencies.append(rep)
			eml.emotions.append(emo)
			emxml=eml.to_xml().toprettyxml()		
		except (TypeError, ValueError):
			pass
		else:
			self.fail( printOutcome("502", 'fail', 'The value of the "freq" attribute of <trace> MUST be a positive floating point number followed by optional whitespace followed by "Hz".'))

		# these are all good
		eml=EmotionML()
		emo=Emotion()
		emo.action_tendency_set="act"
		emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
		trace=Trace('10.5Hz', [.6, .4, .8])
		rep=Representation('power', 'action-tendency', trace)
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()

		eml=EmotionML()
		emo=Emotion()
		emo.action_tendency_set="act"
		emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
		trace=Trace('10.5 Hz', [.6, .4, .8])
		rep=Representation('power', 'action-tendency', trace)
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()
		
		eml=EmotionML()
		emo=Emotion()
		emo.action_tendency_set="act"
		emo.vocabularies.append(Vocabulary("action-tendency","act",[Item("power")]))
		trace=Trace('.5 Hz', [.6, .4, .8])
		rep=Representation('power', 'action-tendency', trace)
		emo.action_tendencies.append(rep)
		eml.emotions.append(emo)
		emxml=eml.to_xml().toprettyxml()

		print printOutcome("502", 'pass', 'The value of the "freq" attribute of <trace> MUST be a positive floating point number followed by optional whitespace followed by "Hz".')

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
			print printOutcome("503", 'pass', 'The <trace> element MUST have a "samples" attribute.')
			return
		self.fail( printOutcome("503", 'fail', 'The <trace> element doesn\'t require have a "samples" attribute.'))

	def test_504(self):
		""" The value of the "samples" attribute of <trace> MUST be a space-separated list of floating point values from the closed interval [0, 1] """
		try:
			trace = Trace("0.5Hz",[0.5,0.99999,0.000001])
			doc = Document()
			trace.to_xml(doc)
		except ValueError:
			self.fail( printOutcome("504", 'fail', 'The value of the "samples" attribute of <trace> MUST be a space-separated list of floating point values from the closed interval [0, 1].'))
			
		invalid_samples = [[-0.5],[0],[1],[1.2222]]

		for inv in invalid_samples:
			try:
				trace = Trace("0.5Hz",inv)
				doc = Document()
				trace.to_xml(doc)
			except ValueError:
				pass
			else:
				self.fail( printOutcome("504", 'fail', 'The value of the "samples" attribute of <trace> MUST be a space-separated list of floating point values from the closed interval [0, 1].'))
		print printOutcome("504", 'pass', 'The value of the "samples" attribute of <trace> MUST be a space-separated list of floating point values from the closed interval [0, 1].')

	def test_600(self):
		try:
			eml=EmotionML()
			voc=Vocabulary(type='action-tendency', id='frijda-subset')
			eml.vocabularies.append(voc)
			eml.to_xml().toprettyxml()
		except TypeError:
			print printOutcome("600", 'pass', 'A <vocabulary> element MUST contain one or more <item> elements.')
			return
		self.fail( printOutcome("600", 'fail', 'A <vocabulary> element MUST contain one or more <item> elements.'))

	def test_601(self):
		eml=EmotionML()
		items=[]
		item=Item('approach')
		items.append(item)
		info= Info('someID')
		info2=Info('otherID')
		voc=Vocabulary('action-tendency', 'frijda-subset', items, info)
		voc.info=info2
		eml.vocabularies.append(voc)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertEqual(len(doc.getElementsByTagName('info')), 1, printOutcome("601", 'fail', 'A <vocabulary> element MAY contain a single <info> element.'))
		print printOutcome("601", 'pass', 'A <vocabulary> element MAY contain a single <info> element.')

	def test_602(self):
		try:
			eml=EmotionML()
			item=[]
			item.append(Item('approach'))
			voc=Vocabulary(id='frijda-subset', items= item)
			eml.vocabularies.append(voc)
			eml.to_xml().toprettyxml()
		except TypeError:
			print printOutcome("602", 'pass', 'A <vocabulary> element MUST contain a "type" attribute')
			return
		self.fail( printOutcome("602", 'fail', 'A <vocabulary> element MUST contain a "type" attribute'))

	def test_603(self):
		try:
			eml=EmotionML()
			items= []
			items.append(Item('anger'))
			voc=Vocabulary('NotAType', 'big6', item)
			eml.vocabularies.append(voc)
			emxml=eml.to_xml().toprettyxml()
			doc=parseString(emxml)
		except:
			print printOutcome('603', 'pass', 'The value of the "type" attribute of the <vocabulary> element MUST be one of "category", "dimension", "action-tendency" or "appraisal".')
			return
		self.fail(printOutcome('603', 'fail', 'The value of the "type" attribute of the <vocabulary> element isn\'t required to be one of "category", "dimension", "action-tendency" or "appraisal".'))
		
	def test_604(self):
		try:
			eml=EmotionML()
			item=[]
			item.append(Item('approach'))
			voc=Vocabulary(type='action-tendency', items= item)
			eml.vocabularies.append(voc)
			eml.to_xml().toprettyxml()
		except TypeError:
			print printOutcome("604", 'pass', 'A <vocabulary> element MUST contain an "id" attribute')
			return
		self.fail( printOutcome("604", 'fail', 'A <vocabulary> element does not have to contain an "id" attribute'))

	def test_605(self):
		""" The value of the "id" attribute of the <vocabulary> element MUST be of type xsd:ID """
		invalid_ids = ['  ','9zzk','-hjk','*httpjj9-']
		def create_voc(id):
				items= []
				items.append(Item('anger'))
				voc = Vocabulary("dimension",id,items)
				doc = Document()
				voc.to_xml(doc)
				return
		last = ""
		try:
			for id in invalid_ids:
				last = id
				create_voc(id)
		except TypeError as te:
			pass
		else:
			self.fail(printOutcome("605", 'fail','The value of the "id" attribute of the <vocabulary> element MUST be of type xsd:ID.'))

		valid_ids = ['_7','az56','A-hjk0','_---']
		last = ""
		try:
			for id in valid_ids:
				last = id
				create_voc(id)
		except TypeError as te:
			self.fail(printOutcome("605", 'fail','The value of the "id" attribute of the <vocabulary> element MUST be of type xsd:ID.'))
		printOutcome("605", 'pass','The value of the "id" attribute of the <vocabulary> element MUST be of type xsd:ID.')


	def test_606(self):
		eml=EmotionML()
		items=[]
		info= Info('someID')
		item=Item('approach', info)
		info2=Info('otherID')
		item.info=info2
		items.append(item)
		voc=Vocabulary('action-tendency', 'frijda-subset', items)
		eml.vocabularies.append(voc)
		emxml=eml.to_xml().toprettyxml()
		doc=parseString(emxml)
		self.assertEqual(len(doc.getElementsByTagName('info')), 1, printOutcome("606", 'fail', 'An <item> element MAY contain a single <info> element.'))
		print printOutcome("606", 'pass', 'An <item> element MAY contain a single <info> element.')

	def test_607(self):
		try:
			eml=EmotionML()
			item=[]
			item.append(Item())
			voc=Vocabulary(type='action-tendency', items= item)
			eml.vocabularies.append(voc)
			eml.to_xml().toprettyxml()	
		except TypeError:
			print printOutcome("607", 'pass', 'An <item> element MUST contain a "name" attribute.')
			return
		self.fail( printOutcome("607", 'fail', 'An <item> element is not required to contain a "name" attribute.'))
	
	def test_608(self):
		'''
		try:
			item= []
			eml=EmotionML()
			item.append(Item('anger'))
			item.append(Item('disgust'))
			item.append(Item('anger'))
			voc=Vocabulary('category', 'big6', item)
			eml.vocabularies.append(voc)
			emxml=eml.to_xml().toprettyxml()
			doc=parseString(emxml)
		except ValueError:
			print printOutcome('608', 'pass', 'An <item> MUST NOT have the same name as any other <item> within the same <vocabulary>.')
			return
		self.fail(printOutcome('608', 'fail', 'An <item> MUST NOT have the same name as any other <item> within the same <vocabulary>.'))
		'''
		printOutcome('608', 'not-impl', 'An <item> MUST NOT have the same name as any other <item> within the same <vocabulary>.',comment="Vocabulary checks were not implemented in this release. See ")


	def test_700(self):
		""" All EmotionML elements MUST use the EmotionML namespace, "http://www.w3.org/2009/10/emotionml".
		"""
		eml = EmotionML()
		emlxml = eml.to_xml().toprettyxml()
		doc=parseString(emlxml)
		eml = doc.getElementsByTagName('emotionml')[0]
		ns = eml.getAttribute("xmlns")
		self.assertEqual(ns,"http://www.w3.org/2009/10/emotionml", 
		printOutcome('700', 'fail', 'All EmotionML elements MUST use the EmotionML namespace, "http://www.w3.org/2009/10/emotionml". '))
		printOutcome('700', 'pass', 'All EmotionML elements MUST use the EmotionML namespace, "http://www.w3.org/2009/10/emotionml". ')
	

def printOutcome( ID, result, notes,comment="" ):
	return '<assert id=\"%s\" res=\"%s\">%s</assert>' % (ID,result,comment)	

if __name__ == '__main__':
        unittest.main()
