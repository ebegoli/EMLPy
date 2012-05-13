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

import sys
import xml.dom.minidom

class Trace:      
   """Representation for the trace - frequency and samples"""
   #NOTE: this is implemented
   freq = None
   samples = []

   def __init__(self, freq, samples):
      """ Intializes with both frequency of collection and samples """
      self.freq = freq
      self.samples = samples

   def __str__(self):
      """ Utility string function """
      return "freq: " + str(self.freq) + " samples: " + str(self.samples)

   def to_xml(self, doc):
      """ Produces an EmotionML element """
      trace = doc.createElement('trace')
      trace.setAttribute('freq',str(self.freq))
      trace.setAttribute('samples',','.join(map(str,self.samples)))
      return trace

class Root:
   """ Representation for root Emotion element in EmotionML"""
   emotions = []
   vocabularies = []
   info = None

def toxml(self):
   #TODO: add namespace http://www.w3.org/2009/10/emotionml
      pass

class Info:
   """ Info element, structure is flexible and it should be text """
   #TODO: this is implemented
   id=None
   def __init__(self,id=None):
      if id:
         self.id = id

class Emotion: 
   """
   Required:
   
   Optional: emotion_id, start, end, duration, time-ref-uri, 
   time-ref-anchor-point, offset-to-start
   
   Notes: start, end, duration, time-ref-uri, 
   time-ref-anchor-point, offset-to-start are all in absolute time units
   """

   #TODO: figure out how to store sets
   categories = []
   dimensions = []
   appraisals = []
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

   def __init__(self):
      pass

   def to_xml(self, doc ):
      """ Creates EmotionML compliant Emotion element """
      emo = doc.createElement('emotion')

      if not (self.categories or self.dimensions 
         or self.appraisals or self.action_tendencies):
         raise ValueError('At least one of the category or dimension or appraisal or action-tendency must be provided')

      if emotion_id:
         emo.setAttribute('id', str(emotion_id))
      if start:
         emo.setAttribute('start', str(start))
      if end:
         emo.setAttribute('end', str(end))
      if duration:
         emo.setAttribute('duration', str(duration))
      if time_ref_uri:
         emo.setAttribute('time-ref-uri', str(time_ref_uri))
      if time_ref_anchor_point:
         emo.setAttribute('time-ref-anchor-point', str(time_ref_anchor_point))
      if offset_to_start:
         emo.setAttribute('offset-to-start', str(offset_to_start))
      if info:
         emo.appendChild(info.to_xml())

      doc.appendChild(emo)     
      return doc


class Representation:
   """ Class represents dimension, category, appraisal or action-tendency """
   #TODO: write unit tests
   representations = ('dimension', 'category', 
      'appraisal', 'action-tendency')
   representation = None
   category_ns = None
   value = None
   trace = None
   name = None
   confidence = None

   def __init__(self,repr):
      assert repr is not None and len(repr) > 0 , 'name of representation is empty'
      assert repr in self.representations, 'name of representation is not \
      in the list of representations ' + str(self.representations)
      self.representation = repr

   def get_category(self):
      #TODO: this has to be transformed into name, namespace tuple
      """ Returns the name of the representation that can be used in 
      set of categories """
      return self.representation

   def __str__(self):
      """ TODO: """
      pass
     
   def to_xml(self, doc):
      """ Creates EmotionML compliant representation """
      repr = doc.createElement(str(self.representation))
      repr.setAttribute('name',str(self.name))

      if self.trace and self.value:
         raise ValueError('Only one of traces or value can be provided for ' +
            self.representation) 
      if not self.trace and not self.value:   
         raise ValueError('No trace nor value are provided for ' +
            self.representation) 

      if self.trace:
            repr.appendChild(self.trace.to_xml(doc))
      else:
         repr.setAttribute('value',str(self.value))

      if self.confidence:
         repr.setAttribute('confidence',str(self.confidence))   

      doc.appendChild(repr)     
      return doc

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
   print "in main ... to be implemented ..."
