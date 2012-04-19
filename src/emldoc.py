#!/usr/bin/env python
''' A EmotionML document generator
    TODO: study how to use this approach: http://code.activestate.com/recipes/415983/
'''

__author__ = 'Edmon Begoli'

import sys
import xml.dom.minidom

def make_dimension( doc, set, confidence=None ):
   ''' Makes an emotion sub-element dimensions. confidence 
   is optional'''

   category = doc.createElement('category')
   category.setAttribute('set', set)
   category.setAttribute('name', name)
   if confidence is not None:
      category.setAttribute('confidence',confidence)
   return category   

def make_category( doc, set, name, confidence=None ):
   ''' Makes an emotion sub-element category. confidence 
   is optional'''

   category = doc.createElement('category')
   category.setAttribute('set', set)
   category.setAttribute('name', name)
   if confidence is not None:
      category.setAttribute('confidence',confidence)
   return category   

def make_xml():
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
