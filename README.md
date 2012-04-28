EmotionMLPy
-----------

Reference implementation for EmotionML markup language vocabularies in Python

Structure of a EmotionML document:

emotionml - root  
attributes: 
namespace, version  
   elements:
   emotion+ 
   attributes: 
   category-set, dimension-set, appraisal-set, action-tendency-set
   version
   id? start? end? duration? time-ref-uri? time-ref-anchor-point? offset-to-start? expressed-through?
      elements:
      at least one of each: category, dimension, appraisal, action-tendency  
      info (occurs only once)
