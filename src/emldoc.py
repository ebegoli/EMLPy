#!/usr/bin/env python
''' An EmotionML document generator
    TODO: study how to use this approach: http://code.activestate.com/recipes/415983/
'''

__author__ = 'Edmon Begoli'

import sys
import xml.dom.minidom

#TODO: make sure that dimensions passed are list of instances of documents
def make_dimensions( doc, emotion_dimensions, trace=None, value=None, confidence=None ):
   ''' Makes an emotion sub-element dimensions. confidence 
   is optional'''

   dimensions = doc.createElement('dimensions')
   for dimension in emotion_dimensions:
      dimensions.appendChild( dimension )

   if trace is not None:
      dimensions.appendChild( trace )
      
   if value is not None:
      dimensions.setAttribute('value',value)
   if confidence is not None:
      dimension.setAttribute('confidence',confidence)
   
   return category   

def make_category( doc, value, category=None ):
   ''' Makes an emotion sub-element category. confidence 
   is optional'''

   category = doc.createElement('category')
   category.setAttribute('set', set)
   category.setAttribute('name', name)
   if confidence is not None:
      category.setAttribute('confidence',confidence)
   return category   

def make_emotion(category, dimension, appraisal, action_tendency, reference, info ):   


def make_xml():
   ''' Makes an EmotionML compliant XML document
   '''
   doc = xml.dom.minidom.Document()
   emotionml = doc.createElement('emotionml')
   doc.appendChild(emotionml)

   emotion = doc.createElement('emotion')
   emotionml.appendChild(emotion)

   category = make_category( doc, 'everydayEmotions','satisfaction')
   emotion.appendChild(category)

   #el = doc.createElementNS('http://example.net/ns', 'el')
   #el.setAttribute("xmlns", "http://example.net/ns")
   #doc.appendChild(el)
   #retrun doc.toprettyxml()
   return doc


if __name__ == '__main__':
   print make_xml().toprettyxml()
