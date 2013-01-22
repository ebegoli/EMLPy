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
An EmotionML document generator
"""
__author__ = 'Edmon Begoli'

import re
import xml.dom.minidom

representations = ('dimension', 'category', 'appraisal', 'action-tendency')
anyuri_regex = re.compile(r"^(([a-zA-Z][0-9a-zA-Z+\-\.]*:)?/{0,2}[0-9a-zA-Z;/?:@&=+" +
                          r"$\.\-_!~*'()%]+)?(#[0-9a-zA-Z;/?:@&=+$\.\-_!~*'()%]+)?$")


class EmotionML:
    """ Representation for root Emotion element in EmotionML """

    def __init__(self):
        self.emotions = []
        self.info = None
        self.version = "1.0"
        self.category_set = None
        self.dimension_set = None
        self.appraisal_set = None
        self.action_tendency_set = None
        self.vocabularies = []
        self.content = ""

    def to_xml(self):
        """ Generates representation for the whole document with validations """
        doc = xml.dom.minidom.Document()
        em = doc.createElement('emotionml')
        em.setAttribute("xmlns", "http://www.w3.org/2009/10/emotionml")
        if (self.version is None) or ("1.0" != self.version.strip()):
            raise ValueError('Version on emotionml has to be 1.0. Value %s for version is not valid.' % self.version)
        else:
            em.setAttribute("version", self.version)

        em_sets = (('category-set', self.category_set), ('dimension-set', self.dimension_set),
                   ('appraisal-set', self.appraisal_set), ('action-tendency-set', self.action_tendency_set))

        for em_set in em_sets:
            em = store_repr_set(em_set, em)

        if self.content:
            em_text = doc.createTextNode(str(self.content))
            em.appendChild(em_text)

        if self.info:
            em.appendChild(self.info.to_xml(doc))
        for vocabulary in self.vocabularies:
            em.appendChild(vocabulary.to_xml(doc))
        for emotion in self.emotions:
            # see if there are any undefined sets and if so, if defined at this level
            #undef_sets = emotion.get_undefined_sets()
            #self.check_if_defined(undef_sets, emotion)
            # 1. find references with no local vocabulary
            # 2. iterate over this and see if they map to global vocabularies
            # 3. if no global voc. found - raise exception
            #if emotion.has_missing_vocabulary_items():
            #   if emotion.has_missing_global_vocabulary_items( self.vocabularies ):
            #      raise TypeError( "emotion %s is missing vocabulary definitions for %s. " %
            #         (emotion.emotion_id, str(emotion.global_missing) ))
            em.appendChild(emotion.to_xml(doc))
        doc.appendChild(em)
        return doc

    def check_if_defined(self, undefined_sets, emotion):
        """ Checks that sets undefined at the emotion level are defined on this,
        emotionml level. If they are not, function will raise value error."""
        if undefined_sets["dimension-set"] and not self.dimension_set:
            raise ValueError("dimension-set not defined for " + str(emotion.emotion_id))
        if undefined_sets["category-set"] and not self.category_set:
            raise ValueError("category-set not defined for " + str(emotion.emotion_id))
        if undefined_sets["action-tendency-set"] and not self.action_tendency_set:
            raise ValueError("action-tendency-set not defined for " + str(emotion.emotion_id))
        if undefined_sets["appraisal-set"] and not self.appraisal_set:
            raise ValueError("appraisal-set not defined for " + str(emotion.emotion_id))


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

    def __init__(self):
        """ Constructor """

        self.category_set = None
        self.dimension_set = None
        self.appraisal_set = None
        self.action_tendency_set = None
        self.content = None

        self.vocabularies = []
        self.missing = []

        self.categories = []
        self.dimensions = []
        self.appraisals = []
        self.action_tendencies = []
        self.references = []
        self.info = None
        self.version = None
        self.emotion_id = None
        self.start = None
        self.end = None
        self.duration = None
        self.time_ref_uri = None
        self.time_ref_anchor_point = None
        self.offset_to_start = None
        self.expressed_through = None

    def get_undefined_sets(self):
        """ iterate through four representations and make sure
        the representation sets on emotion defined these
        if not - return representations that are not defined
        and dictionary of names ('representation':True/False) """
        unrepresented = {'dimension-set': False, 'category-set': False,
                         'appraisal-set': False, 'action-tendency-set': False}

        if self.categories and not self.category_set:
            unrepresented['category-set'] = True
        if self.action_tendencies and not self.action_tendency_set:
            unrepresented["action-tendency-set"] = True
        if self.dimensions and not self.dimension_set:
            unrepresented["dimension-set"] = True
        if self.appraisals and not self.appraisal_set:
            unrepresented["appraisal-set"] = True
        return unrepresented

    def to_xml(self, doc ):
        """ Creates EmotionML compliant Emotion element """

        emo = doc.createElement('emotion')

        """ my interpretation of http://www.w3.org/TR/emotionml/#s2.1.2
        However, the <emotion> element MUST contain at least one <category> or
        <dimension> or <appraisal> or <action-tendency> element. """
        if not (self.categories or self.dimensions
                or self.appraisals or self.action_tendencies):
            raise ValueError(
                'At least one of the category or dimension or appraisal or action-tendency must be provided')

        check_uniqueness(self.action_tendencies, "action-tendency")
        check_uniqueness(self.categories, "category")
        check_uniqueness(self.appraisals, "appraisal")
        check_uniqueness(self.dimensions, "dimension")

        if self.version:
            if "1.0" != self.version.strip():
                raise ValueError('Version on emotion has to be 1.0. Value %s for version is not valid.' % self.version)
            else:
                emo.setAttribute("version", self.version)

        for vocabulary in self.vocabularies:
            emo.appendChild(vocabulary.to_xml(doc))

        for repset in (("dimension-set", self.dimension_set), ("category-set", self.category_set),
                       ("action-tendency-set", self.action_tendency_set), ("appraisal-set", self.appraisal_set)):
            emo = store_repr_set(repset, emo)

        for reference in self.references:
            emo.appendChild(reference.to_xml(doc))

        for sets in (self.categories, self.dimensions, self.appraisals, self.action_tendencies):
            for item in sets:
                emo.appendChild(item.to_xml(doc))

        if self.emotion_id:
            if not is_ID(self.emotion_id):
                raise ValueError("id %s on emotion is not of type xsd:id." % str(self.emotion_id))
            emo.setAttribute('id', str(self.emotion_id))

        if self.start:
            if not is_positive_int(self.start):
                raise ValueError("start %s is not a positive integer." %
                                 str(self.start))
            emo.setAttribute('start', str(self.start))

        if self.end:
            if not is_positive_int(self.end):
                raise ValueError("end %s is not a positive integer." %
                                 str(self.end))
            emo.setAttribute('end', str(self.end))

        if self.duration:
            if not is_positive_int(self.duration):
                raise ValueError("duration %s is not a positive integer." %
                                 str(self.duration))
            emo.setAttribute('duration', str(self.duration))
        if self.time_ref_uri:
            emo.setAttribute('time-ref-uri', str(self.time_ref_uri))

        if self.time_ref_anchor_point:
            if ( (str(self.time_ref_anchor_point).strip() != "start"  ) and
                 ( str(self.time_ref_anchor_point).strip() != "end")):
                raise ValueError("time-ref-anchor-point %s is not either start nor end."
                                 % str(self.time_ref_anchor_point))
            emo.setAttribute('time-ref-anchor-point', str(self.time_ref_anchor_point))

        if self.offset_to_start:
            if not is_int(self.offset_to_start):
                raise ValueError("offset-to-start %s is not an integer." %
                                 str(self.offset_to_start))
            emo.setAttribute('offset-to-start', str(self.offset_to_start))

        if self.expressed_through:
            if str(self.expressed_through).find(" ") >= 0:
                raise ValueError("expressed-through %s is of not valid xsd:token type." %
                                 self.expressed_through)
            emo.setAttribute('expressed-through', str(self.expressed_through))
        if self.info:
            emo.appendChild(self.info.to_xml(doc))

        if self.content and len(str(self.content).strip()) > 0:
            emo_text = doc.createTextNode(str(self.content))
            emo.appendChild(emo_text)

        return emo

    def has_missing_global_vocabulary_items(self, global_vocabularies ):
        """ Query function looks into defined representations and related sets
        and looks up vocabularies to check if representations are defined """
        self.global_missing = []
        for rep in self.missing:
            if rep[1] and rep[0]:
                if not global_vocabularies:
                    self.global_missing.append(rep)
                else:
                    for repr in rep[1]:
                        if not self.is_defined_on_vocabulary(repr, rep[0], global_vocabularies):
                            self.global_missing.append(rep)
        return (self.global_missing)

    def has_missing_vocabulary_items(self):
        """ Query function looks into defined representations and related sets
        and looks up vocabularies to check if representations are defined """
        for rep in ((self.category_set, self.categories),
                    (self.dimension_set, self.dimensions),
                    (self.appraisal_set, self.appraisals),
                    (self.action_tendency_set, self.action_tendencies)):
            if rep[1] and rep[0]:
                if not self.vocabularies:
                    self.missing.append(rep)
                else:
                    for repr in rep[1]:
                        print "is uri " + self.is_uri(rep[0])
                        if not self.is_uri(rep[0]) and not self.is_defined_on_vocabulary(repr, rep[0],
                                                                                         self.vocabularies):
                            self.missing.append(rep)
        return (self.missing)

    def has_vocabulary_references(self, set_name, vocabularies):
        """ Checks if set name refers to an actual vocabulary """
        return find(lambda vocab: vocab.id in set_name, vocabularies)


    def is_defined_on_vocabulary(self, representation, set_name, vocabularies):
        """ looks into vocabulary with known set name for definitions of items
        as found on representations """
        vocabulary = find(lambda vocab: vocab.id == set_name, vocabularies)
        if not vocabulary:
            return False
        if find(lambda item: item.name == representation.name, vocabulary.items):
            return True
        else:
            return False


class Vocabulary:
    ''' Contains the definition of an emotion vocabulary - <vocabulary>  '''

    def __init__(self, type, id, items, info=None):
        self.type = type
        self.id = id
        self.items = items
        self.info = info

    def __str__(self):
        """ Returns string representation of the vocabulary """
        return "type:%s id:%s info:%s" % (self.type, self.id, map(str, self.items))

    def to_xml(self, doc):
        """ Produces a <vocabulary> element """
        voc = doc.createElement('vocabulary')
        if not self.id:
            raise ValueError('id attribute has to be set on a vocabulary')
        if not self.type:
            raise ValueError('type attribute has to be set on a vocabulary %s' % self.id)
        if self.type not in representations:
            raise TypeError('type %s attribute on vocabulary %s has to be one of the representations %s' %
                            ( self.type, self.id, map(str, representations)))

        if not is_ID(self.id):
            raise TypeError('id %s on vocabulary %s is not valid xsd:id.' % (self.id, self.type))

        voc.setAttribute('id', str(self.id))
        voc.setAttribute('type', str(self.type))

        if not self.items:
            raise TypeError('There should be at least on item on vocabulary %s'
                            % self.id)

        if self.info:
            voc.appendChild(self.info.to_xml(doc))

        if self.items:
            check_uniqueness(self.items, "vocabulary " + self.id)

        for item in self.items:
            voc.appendChild(item.to_xml(doc))
        return voc


class Item:
    """ Representation for <item> which represents the definition of one vocabulary item,
    associated with a value which can be used in the "name" attribute of <category>,
    <dimension>, <appraisal> or <action-tendency>
    (depending on the type of vocabulary being defined). """

    def __init__(self, name, info=None):
        """ Constructor - name is mandatory"""
        self.name = name
        self.info = info

    def __str__(self):
        """ string representation for item """
        return "name:%s info:%s " % (self.name, str(self.info))

    def to_xml(self, doc):
        """ Produces an <item> element """
        item = doc.createElement('item')

        if not self.name:
            raise ValueError('name attribute is required on item element')
        item.setAttribute('name', str(self.name))

        if self.info:
            item.appendChild(self.info.to_xml(doc))
        return item


class Representation:
    """ This class is an abstract representation (i.e. there is no such element
       as <representation> in EmotionML) of an emotion expressed through one of
       the four ways how emotion can be represented in EmotionML -
       dimension, category, appraisal or action-tendency.
       To represent emotion using one of the four categories author of the document
       will create an instance of the Representation class providing the 'representation'
       value in the constructor. This value has to be one of the four categories.

       The structure of the Representation and therefore dimension, category, appraisal
       or action-tendency is:
       Children <trace>: A representation MAY contain either a value
           attribute or a <trace> element.
       Attributes
         Required:
          name, the name of the representation, which MUST be contained in the declared
          category vocabulary (see below).
        Optional:
          value: A representation MAY contain either a value attribute
          or a <trace> element.
          confidence, the annotator's confidence that the annotation
          given for this representation is correct.
        """

    def __init__(self, name, representation, trace=None, value=None, confidence=None):
        '''name is a given name for this representation and representation has to be
        one of 'dimension', 'category', 'appraisal', 'action-tendency' '''
        assert representation, 'name of representation is empty'
        assert representation in representations, 'name of representation:%s is not in\
       the list of representations' % str(representations)
        self.representation = representation # canonical names specified by standard, so far four
        self.name = name # user specified name for this representation
        self.trace = trace
        self.value = value
        self.confidence = confidence

    def __str__(self):
        """ string representation of what it carries
        dimension, category, appraisal, action-tendency """
        return "representation:%s name:%s trace:%s value:%s confidence:%s" %\
               (self.representation, self.name, self.trace, self.value, self.confidence)

    def to_xml(self, doc):
        """ Creates EmotionML compliant representation """
        repr = doc.createElement(str(self.representation))

        if not self.name:
            raise ValueError('Name has to be provided for %s %s' %
                             (str(self.representation), str(self.name)))
        repr.setAttribute('name', str(self.name))

        if self.representation == 'dimension':
            if not self.value and not self.trace:
                raise ValueError('Either trace or value has to be provided for dimension ' + self.name)

        if self.value and self.trace:
            raise ValueError('Trace and value cannot be both provided for ' + self.name)

        if self.trace:
            repr.appendChild(self.trace.to_xml(doc))
        elif self.value:
            if float(str(self.value)) > 1.0 or float(str(self.value)) < 0.0:
                raise ValueError('Value has to be within closed [0,1] interval instead of ' + str(self.value))
            else:
                repr.setAttribute('value', str(self.value))

        if self.confidence:
            if float(str(self.confidence)) > 1.0 or float(str(self.confidence)) < 0.0:
                raise ValueError('Confidence has to be within closed [0,1] interval instead of ' + str(self.confidence))
            else:
                repr.setAttribute('confidence', str(self.confidence))
        return repr


class Info:
    """ Info element <info>, structure is flexible and we represent its content
    as text """

    def __init__(self, id=None):
        """ Constructor - nothing is required """
        self.content = None
        self.id = None
        if id:
            self.id = id

    def to_xml(self, doc):
        """  Constructs <info> element with id attribute and text content """
        info = doc.createElement('info')
        if self.id:
            if not is_ID(self.id):
                raise ValueError('Id %s on <info> element is not of xsd:id type ' % str(self.id))
            info.setAttribute('id', self.id)
        if self.content and len(str(self.content).strip()) > 0:
            info_text = doc.createTextNode(str(self.content))
            info.appendChild(info_text)
        return info


class Trace:
    """Representation for the <trace> which captures the
    time evolution of a dynamic scale value represented through frequency and samples"""

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
        if not self.freq:
            raise ValueError('Trace element requires freq attribute. It was not set.')
        else:
            #Perform checks for units
            parts = str(self.freq).split('Hz')
            try:
                fl = float(parts[0])
            except ValueError:
                raise ValueError('Frequency attribute on trace element was not float: ' + str(self.freq))
            if fl <= float(0):
                raise ValueError('Frequency attribute on trace element was negative float: ' + str(self.freq))
            if not str(self.freq).strip().endswith('Hz'):
                raise ValueError('Frequency attribute on trace element does not have valid (Hz) unit: ' +
                                 str(self.freq))
            trace.setAttribute('freq', str(self.freq))
        if not self.samples:
            raise ValueError('Trace element requires samples attribute. It was not set.')
        else:
            for sample in self.samples:
                if not is_float(sample):
                    raise ValueError('Sample %d on a trace is not a valid floating point number.' % sample)
                if not is_within_interval(float(sample)):
                    raise ValueError('Sample %d on a trace is not within [0,1] interval.' % sample)
            trace.setAttribute('samples', ' '.join(map(str, self.samples)))
        return trace


class Reference:
    """Representation for the <reference> - attributes: uri required
    and optional: role and media-type. Role must be one of:
    expressedBy" (default), "experiencedBy", "triggeredBy", "targetedAt" """
    roles = ('expressedBy', 'experiencedBy', 'triggeredBy', 'targetedAt')


    def __init__(self, uri, role="expressedBy", media_type=None):
        """ Intializes with uri and optionally role and media_type """
        self.uri = uri
        if role is not None:
            self.role = role
        self.media_type = media_type

    def __str__(self):
        """ Utility string function """
        return "uri: %s role: %s media-type: %s" % str(self.uri) % str(self.role) % str(self.media_type)

    def to_xml(self, doc):
        """ Produces a <reference> element """
        ref = doc.createElement('reference')
        ref.setAttribute('uri', str(self.uri))
        if self.media_type:
            if not has_media_type(self.media_type):
                raise TypeError("media type (" + self.media_type + ") is not recognized.")
            ref.setAttribute('media-type', str(self.media_type))
            #if role is set, make sure it is one of accepted values
        if self.role:
            if self.role in (self.roles):
                ref.setAttribute('role', self.role)
            else:
                raise TypeError("role (" + self.role + ") must be one of " + map(str, self.roles))
        return ref

#module level functions
def is_int(s):
    """ Simple int check """
    try:
        int(s)
        return True
    except ValueError:
        return False


def is_positive_int(s):
    """ Simple positive int check """
    try:
        val = int(s)
        return (val >= 0)
    except ValueError:
        return False


def is_float( val ):
    """ Simple float check """
    try:
        float(val)
        return True
    except ValueError:
        return False


def is_within_interval( val, start=0.0, end=1.0):
    """ checks if the value is within an interval pass"""
    return (start < val < end)


def validate_dimension(dim):
    """ Checks that dimension value is provided"""
    if not (dim.value):
        raise ValueError('No trace nor value are provided for ' + dim.representation)


def check_uniqueness( elements, context ):
    """ Validates the elements of the list for name uniqueness
    and throws validation exception is names are not unique """
    if has_same_name(elements):
        raise ValueError('Not all names of %s are unique: %s' %
                         (  context, map(str, elements) ))


def find(f, seq):
    """Return first item in sequence where f(item) == True."""
    for item in seq:
        if f(item):
            return item


def is_ID( val ):
    """ Checks if the value is valid xsd:id """
    reg = re.compile(r'^[a-zA-Z_][\w.-]*$')
    return reg.match(val)


def is_uri( something ):
    ''' Checks if the string complies with xsd:anyURI '''
    return (something is not None) and (anyuri_regex.match(str(something)) is not None)


def has_same_name( elements ):
    """ Checks if the names of the elements are same
    """
    name = [element.name for element in elements]
    return len(set(name)) < len(name)


def has_media_type( media_type):
    ''' Checks media type such as 'application/atom+xml' against iana.org.
    It queries the web site  http://www.iana.org/assignments/media-types/application
    and searches for atom+xml on the web page. '''
    import urllib2

    if media_type.find('/'):
        media_parts = media_type.split('/')
    else:
        raise ValueError('media type %s does not have a proper type-subtype structure.' % media_type)

    search_url = "http://www.iana.org/assignments/media-types/" + media_parts[0]
    results = None
    try:
        results = urllib2.urlopen(search_url)
    except urllib2.HTTPError as he:
        raise ValueError("In has_media_type got %s for %s." % (he, search_url))

    found = False
    for l in results.readlines():
        try:
            if l.count(media_parts[1]) > 0:
                found = True
                break
        except UnicodeDecodeError:
            print "Ignoring UnicodeDecodeError in has_media_type"
    results.close()
    return found


def store_repr_set( repset, doc ):
    """ Checks on the format of set (if it is anyURI) and adds it to the emotion document """
    if repset[1]:
        if not is_uri(repset[1]):
            raise ValueError('%s for %s is not a valid URI' % (repset[1], repset[0]))
        doc.setAttribute(repset[0], repset[1])
    return doc