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

class EmotionML:
   """ Representation for root Emotion element in EmotionML"""
   emotions = []
   vocabularies = []
   info = None

   def __init__(self):
      pass

   def to_xml(self):
      doc = xml.dom.minidom.Document()
      em = doc.createElement('emotionml')
      for emotion in self.emotions:
         em.appendChild(emotion)
      #TODO: add namespace http://www.w3.org/2009/10/emotionml
      doc.appendChild(em)
      return doc

class Info:
   """ Info element <info>, structure is flexible and we represent its content 
   as text """
   #TODO: to be tested
   content=None
   id=None
   def __init__(self,id=None):
      if id:
         self.id = id

   def to_xml(self,doc):
      """  Constructs <info> element with id attribute and text content """
      info = doc.createElement('info')
      info.setAttribute('id',self.id)
      if self.content is not None and len(str(self.content).strip()) > 0:
         info_text = doc.createTextNode(str(self.content))
         info.appendChild(info_text)
      return info

class Reference:      
   """Representation for the <reference> - attributes: uri required 
   and optional: role and media-type. Role must be one of: 
   expressedBy" (default), "experiencedBy", "triggeredBy", "targetedAt" """
   uri=None
   role='expressedBy'
   media_type=None
   roles = ('expressedBy', 'experiencedBy', 'triggeredBy', 'targetedAt')


   def __init__(self, uri,role="expressedBy",media_type=None):
      """ Intializes with uri and optionally role and media_type """
      self.uri = uri
      if role is not None:
         self.role = role
      if media_type is not None:
         self.media_type = media_type

   def __str__(self):
      """ Utility string function """
      return "uri: %s role: %s media-type: %s" % str(self.uri) % str(self.role) % str(self.media_type)

   def to_xml(self, doc):
      """ Produces a <reference> element """
      ref = doc.createElement('reference')
      ref.setAttribute('uri',str(self.uri))
      if self.media_type:
         ref.setAttribute('media-type',str(self.media_type))
      if self.role in (self.roles): 
         ref.setAttribute('role',self.role)
      else:
         raise TypeError( "role ("+self.role+") must be one of " + self.roles )
      return ref

class Emotion: 
   """ This element represents a single emotion annotation.
   Children:
   It has at least one of the following children used to describe an emotion: 
   (<category>|<dimension>|<appraisal>|<action-tendency>)+
   <reference>*
   <info>?
   Attributes:
   version indicates the version of the specification to be used for the <emotion> 
   and its descendants. Documents using this specification MUST use 1.0 for the value. 
   The value of the version attribute defaults to "1.0".
   
   id, a unique identifier for the emotion, of type xsd:ID.
   
   category-set declares a local category vocabulary (see also <category>) 
   for the current <emotion> element. The attribute MUST be of type xsd:anyURI 
   and MUST refer to the ID of a <vocabulary> element defining an emotion 
   vocabulary with type="category", as specified in Defining vocabularies 
   for representing emotions.
   
   dimension-set declares a local dimension vocabulary (see also <dimension>) 
   for the current <emotion> element. The attribute MUST be of type xsd:anyURI 
   and MUST refer to the ID of a <vocabulary> element defining an emotion 
   vocabulary with type="dimension", as specified in Defining vocabularies 
   for representing emotions.
   
   appraisal-set declares a local appraisal vocabulary (see also <appraisal>) 
   for the current <emotion> element. The attribute MUST be of type xsd:anyURI 
   and MUST refer to the ID of a <vocabulary> element defining an emotion 
   vocabulary with type="appraisal", as specified in Defining vocabularies 
   for representing emotions.
   
   action-tendency-set declares a local action tendency vocabulary 
   (see also <action-tendency>) for the current <emotion> element. 
   The attribute MUST be of type xsd:anyURI and MUST refer to the ID of a 
   <vocabulary> element defining an emotion vocabulary with type="action-tendency", 
   as specified in Defining vocabularies for representing emotions.
   
   start, end, duration, time-ref-uri, time-ref-anchor-point and offset-to-start 
   provide information about the times at which an emotion happened, 
   as defined in Timestamps.
   
   expressed-through, the modality, or list of modalities, 
   through which the emotion is expressed.   

   See: http://www.w3.org/TR/emotionml/#s2.1.2
   """

   #TODO: figure out how to store sets
   # this cannot be list, but rather one per emotion
   category_set = None
   dimension_set = None
   appraisal_set = None
   action_tendency_set = None
   
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

   def add_category(self,category):
      self.categories.append( category )

   def add_dimension(self,dimension):
      self.dimensions.append( category )

   def add_apprasial(self,appraisal):
      self.appraisals.append( appraisal )

   def add_action_tendency(self,tendency):
      self.action_tendencies.append( tendency )

   @staticmethod
   def get_set( representations ):
      representation_set = []
      if representations:
         representation_set = [set([representation.get_category() 
            for representation in representations])]
      return representations_set

   def to_xml(self, doc ):
      """ Creates EmotionML compliant Emotion element """

      emo = doc.createElement('emotion')

      if not (self.categories or self.dimensions 
         or self.appraisals or self.action_tendencies):
         raise ValueError('At least one of the category or dimension or appraisal or action-tendency must be provided')



      for child in (self.categories,self.dimensions,self.appraisals,
         self.action_tendencies):
         for item in child:
            emo.appendChild(item.to_xml(emo))
      
      if emotion_id:
         emo.setAttribute('id', str(self.emotion_id))
      if start:
         emo.setAttribute('start', str(self.start))
      if end:
         emo.setAttribute('end', str(self.end))
      if duration:
         emo.setAttribute('duration', str(self.duration))
      if time_ref_uri:
         emo.setAttribute('time-ref-uri', str(self.time_ref_uri))
      if time_ref_anchor_point:
         emo.setAttribute('time-ref-anchor-point', str(self.time_ref_anchor_point))
      if offset_to_start:
         emo.setAttribute('offset-to-start', str(self.offset_to_start))
      if info:
         emo.appendChild(info.to_xml(emo))

      return emo


class Representation:
   """ Class represents dimension, category, appraisal or action-tendency """
   #TODO: write unit tests
   representations = ('dimension', 'category', 
      'appraisal', 'action-tendency')
   representation = None
   category_ns = None
   value = None
   trace = None
   repr_name = None
   confidence = None

   def __init__(self,name,representation, trace=None, value=None, confidence=None):
      assert representation, 'name of representation is empty'
      assert representation in self.representations, 'name of representation:%s is not in\
       the list of representations' % str(self.representations)
      self.representation = representation
      self.repr_name = name
      self.trace = trace
      self.value = value
      self.confidence = confidence 

   def get_category(self):
      #TODO: this has to be transformed into name, namespace tuple
      """ Returns the name of the representation that can be used in 
      set of categories """
      return self.representation

   def __str__(self):
      """ TODO: """
      return "representation:%s name:%s trace:%s value:%s confidence:%s" % \
      (self.representation, self.repr_name, self.trace, self.value, self.confidence)
     
   def to_xml(self, doc):
      """ Creates EmotionML compliant representation """
      repr = doc.createElement(str(self.representation))
      repr.setAttribute('name',str(self.repr_name))

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

      return repr

def make_xml(emotions, vocabularies, attributes, info=None):
   ''' Makes an EmotionML compliant XML document
   '''
   emotionml = EmotionML()
   print emotionml.to_xml().toprettyxml()

   rep = Representation(name='test',representation='action-tendency',
      value='0.5',confidence='1')

   print "Test representation:%s " % rep
   print rep.to_xml(emotionml.to_xml()).toprettyxml()

   trace = Trace( "2", ('1.5','1.5','1.6')) 
   print trace.to_xml(emotionml.to_xml()).toprettyxml()

   info = Info("some-id")
   print info.to_xml(emotionml.to_xml()).toprettyxml()

   reference = Reference(uri="http://some-uri",role="triggeredBy",media_type="jpeg")
   print reference.to_xml(emotionml.to_xml()).toprettyxml()


   #doc = xml.dom.minidom.Document()
   #emotionml = doc.createElement('emotionml')
   #doc.appendChild(emotionml)

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
   print make_xml(None,None,None)
