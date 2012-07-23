#!/usr/bin/env python
"""
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
"""
"""
This is a demonstrator module for generation of EmotionML compliant 
documents.
"""
__author__ = 'Edmon Begoli'

from emldoc import *


if __name__ == "__main__":
        emotionml = EmotionML()
        emotionml.dimension_set="http://someurl/dim-set"
        emotionml.appraisal_set="http://somedef"
        emotion = Emotion()

        emotion.emotion_id = "test id"
        emotion.expressed_through = "voice"
        emotion.action_tendency_set="http://someurl/action-tendency-set"
        emotion.end = "3"
        emotion.start = "12"
        emotion.duration = "5"
        emotion.time_ref_anchor_point = "start"
        emotion.expressed_through = "12345"
        emotion.offset_to_start = "-62"
        emotion.dimension_set ="http://someurl/action-tendency-set"

        rep = Representation(name='test',representation='action-tendency',
        value='0.5',confidence='1')
       # rep2 = Representation(name='test',representation='category',
        #value='0.5',confidence='1')

        trace = Trace( "2", ('1.5','1.5','1.6')) 

        info = Info("some-id")

        reference = Reference(uri="http://some-uri",role="triggeredBy",media_type="jpeg")

        emotion.action_tendencies.append(rep)
        #emotion.categories.append(rep2)
        emotion.info = info
        emotion.references.append(reference)
        print emotion.get_undefined_sets()

        #just for control purposes
        #print emotion.to_xml(emotionml.to_xml()).toprettyxml()
        
        emotionml.emotions.append(emotion)


        emxml = emotionml.to_xml().toprettyxml()
        print emxml


