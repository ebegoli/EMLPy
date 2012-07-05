import unittest
from xml.dom.minidom import Document, parseString
from emldoc import *
import time

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


def printOutcome( ID, result, notes ):
	return "<assert id=\"%s\" res=\"%s\">%s</assert>" % (ID,result,notes)	

if __name__ == '__main__':
        unittest.main()
