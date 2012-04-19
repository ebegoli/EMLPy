#!/usr/bin/env python
''' A EmotionML document generator
'''

__author__ = 'Edmon Begoli'

import sys
import xml.dom.minidom

def make_category( doc, set, name, confidence=None ):

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
