#!/usr/bin/env python
''' An EmotionML document generator
    TODO: study how to use this approach: http://code.activestate.com/recipes/415983/
'''

__author__ = 'Edmon Begoli'

import sys
import xml.dom.minidom

trace = {'freq':2,'samples':[3,3]}

class EmotionRepresentation:
   emotions = []
   vocabularies = []
   info = None
   def toxml():
      pass
 
class Emotion: 
   categories = []
   dimensions = []
   apprisals = []
   action_tendencies = []
   references = []
   info = None
   version = None
   emotion_id = None
   start = None
   end = None
   duration = None
   time_ref_uri = None
   time_ref_anchor_point = None
   offset_to_start = None
   expressed_through = None

   def toxml(self, doc ):
      pass

class Representation:
   representations = ('dimension', 'category', 'dimension', 
      'appraisal', 'action-tendency')
   representation = None
   value = None
   traces = []
   name = None
   confidence = None

   def __init__(self,repr):
      assert repr is not None and len(repr) > 0 , 'name of representation is empty'
      assert repr in self.representations, 'name of representation is not \
      in the list of representations ' + str(self.representations)
      representation = repr
     
   def appendAsXML(self, doc):
      repr = doc.createElement(name)
      if traces:
         for trace in traces:
            traceElem = doc.createElement(trace)
            repr.appendChild(traceElem)
      doc.appendChild(repr)     

      
   #el = doc.createElementNS('http://example.net/ns', 'el')
   #el.setAttribute("xmlns", "http://example.net/ns")
   #doc.appendChild(el)




#TODO: make sure that dimensions passed are list of instances of documents
def make_dimensions( doc, emotion_dimensions, trace=None, value=None, confidence=None ):
   ''' Makes an emotion sub-element dimensions. confidence 
   is optional'''

   # dimensions = doc.createElement('dimensions')
   # for dimension in emotion_dimensions:
   #    dimensions.appendChild( dimension )

   # if trace is not None:
   #    dimensions.appendChild( trace )
      
   # if value is not None:
   #    dimensions.setAttribute('value',value)
   # if confidence is not None:
   #    dimension.setAttribute('confidence',confidence)
   
   # return category   

def make_category( doc, value, category=None ):
   ''' Makes an emotion sub-element category. confidence 
   is optional'''

   # category = doc.createElement('category')
   # category.setAttribute('set', set)
   # category.setAttribute('name', name)
   # if confidence is not None:
   #    category.setAttribute('confidence',confidence)
   # return category   

def make_emotion(doc, children, attributes, info=None ):   
   ''' pass children tuples, list of attributes and optional info
       iterate through list of children tuples and attributes 
       and append them to the doc 
       Function enforces EmotionML constraints (has_emotion_children()) 
   '''
   pass

def make_xml(emotions, vocabularies, attributes, info=None):
   ''' Makes an EmotionML compliant XML document
   '''
   doc = xml.dom.minidom.Document()
   emotionml = doc.createElement('emotionml')
   doc.appendChild(emotionml)

   #for emotion in emotions:
   #   emotionml.appendChild( make_emotion( doc, emotion )

   #for vocabulary in vocabularies:
   #   emotionml.appendChild( make_vocabulary( doc, emotion ) 

   #el = doc.createElementNS('http://example.net/ns', 'el')
   #el.setAttribute("xmlns", "http://example.net/ns")
   #doc.appendChild(el)
   #retrun doc.toprettyxml()
   #return doc


if __name__ == '__main__':
   #print make_xml().toprettyxml()
   em1 = EmotionRepresentation()
   em2 = EmotionRepresentation()
   rep = Representation('dimension')
   #rep = Representation('dxmension')
   em1.info = "test"
   print em1.info

