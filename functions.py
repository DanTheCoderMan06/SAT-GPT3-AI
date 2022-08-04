#Imports
import json
import pandas as pd
import time
import math
import time
import random
import numpy as np
import matplotlib as plt
import scipy
import openai
import statistics
from fractions import Fraction
from sentence_transformers import SentenceTransformer as st
model = st("bert-base-nli-mean-tokens")
currentkey = 0
sample_size = 1
keys = ["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","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"]
names = []
df = pd.read_csv('/problems/Indian-Male-Names.csv')['name']
dflist = list(df)
for name in dflist:
  try:
    names.append(name.split(' ')[0])
  except:
    pass
df = pd.read_csv('/problems/Indian-Female-Names.csv')['name']
dflist = list(df)
for name in dflist:
  try:
    names.append(name.split(' ')[0])
  except:
    pass
objectsinquestion = ['Apples','Pencils','Bananas','Pears','Fruits','Phones','Cameras','Computers','Cans','Candles']
actions = [{
    'first' : 'has',
    'second' : 'gives',
    'third' : 'have left',
    'fourth' : 'has',
    'fifth' : 'left',
    'sixth' : 'have',
    'seventh' : 'recieves',
    'eighth' : 'would have'
    },
     ]
random.shuffle(names)
#Functions
def computeGCD(x, y):
   while(y):
       x, y = y, x % y
   return abs(x)
def distance(v1,v2):
  return scipy.spatial.distance.cosine(v1,v2)
def embed(text):
  return model.encode(text)
def predict(text):
  global currentkey
  time.sleep(.6)
  if currentkey > len(keys) - 1:
    currentkey = 0
  openai.api_key = keys[currentkey]  
  currentkey += 1
  success = False
  while not success:
    try:
      response = openai.Completion.create(model="text-davinci-002", prompt=text, temperature=0, max_tokens=20)
      return response['choices'][0]['text']
    except:
      time.sleep(.6)
      if currentkey > len(keys) - 1:
        currentkey = 0
      openai.api_key = keys[currentkey]  
      currentkey += 1
    
def gcd(n, m):
   d =  min (n,    m)
   while   n %  d  !=   0  or  m  %  d  !=   0:
      d =  d  -  1
   return  d
def reduce (num, den):
   if num == 0:
      return  (0,   1)
   g =  gcd(num,      den)
   return  (num    //  g,   den   //  g)
def subtraction(step,prevframe):
  name1 = names[random.randint(0,len(names) -1 )]
  name2 = names[random.randint(0,len(names) -1)]
  objectinquestion = objectsinquestion[random.randint(0,len(objectsinquestion) - 1)]
  action = actions[random.randint(0,len(actions) - 1)]
  firstnum = random.randint(1,10)
  secondnum = random.randint(1,firstnum)
  frame = {
  'question' : f"{name1} {action['first']} {firstnum} {objectinquestion} , {name1} then {action['second']} {name2} {secondnum} {objectinquestion}, how many {objectinquestion} does {name1} {action['third']} ?",
  'answer' : f"{name1} {action['fourth']} {firstnum - secondnum} {objectinquestion} {action['fifth']}. ",
  'type' : "subtraction",
  'step' : 1
  }
  if step == 1:
    frame = {
    'question' : f"{name1} {action['first']} {firstnum} {objectinquestion} , {name1} then {action['second']} {name2} {secondnum} {objectinquestion}, afterwords",
    'answer' : f"{name1} {action['fourth']} {firstnum - secondnum} {objectinquestion} {action['fifth']}. ",
    'numericalanswer' : firstnum-secondnum,
    'type' : "subtraction",
    'name1' : name1,
    'definedobject' : objectinquestion
    }
  elif step == 2:
    secondnum = random.randint(1,10)
    frame = {
    'question' : f"{prevframe['question']} {prevframe['name1']} {action['second']} {name2} {secondnum} {objectinquestion}.",
    'answer' : f"{prevframe['name1']} {action['fourth']} {prevframe['numericalanswer'] - secondnum} {prevframe['definedobject']} {action['fifth']}. ",
    'numericalanswer' : prevframe['numericalanswer'] - secondnum,
    'type' : prevframe['type'] + "subtraction",
    'step' : 2
    }
  return frame
def addition(step,prevframe):
  name1 = names[random.randint(0,len(names) -1 )]
  name2 = names[random.randint(0,len(names) -1)]
  objectinquestion = objectsinquestion[random.randint(0,len(objectsinquestion) - 1)]
  action = actions[random.randint(0,len(actions) - 1)]
  firstnum = random.randint(1,10)
  secondnum = random.randint(1,firstnum)
  frame = {
  'question' : f"{name1} {action['first']} {firstnum} {objectinquestion} , {name1} then {action['seventh']} {secondnum} {objectinquestion}, how many {objectinquestion} does {name1} {action['sixth']} ?",
  'answer' : f"{name1} {action['fourth']} {firstnum + secondnum} {objectinquestion} . ",
  'type' : "addition",
  'step' : 1
  }
  if step == 1:
    frame = {
    'question' : f"{name1} {action['first']} {firstnum} {objectinquestion} , {name2} then {action['second']} {name1} {secondnum} {objectinquestion}, afterwords",
    'answer' : f"{name1} {action['fourth']} {firstnum + secondnum} {objectinquestion} . ",
    'numericalanswer' : firstnum+secondnum,
    'type' : "addition",
    'name1' : name1,
    'definedobject' : objectinquestion
    }
  elif step == 2:
    secondnum = random.randint(1,100)
    frame = {
    'question' : f"{prevframe['question']} {name2} {action['second']} {prevframe['name1']} {secondnum} {objectinquestion}.",
    'answer' : f"{prevframe['name1']} {action['fourth']} {prevframe['numericalanswer'] + secondnum} {prevframe['definedobject']} . ",
    'numericalanswer' : prevframe['numericalanswer'] + secondnum,
    'type' : prevframe['type'] + "addition",
    'step' : 2
    }
  return frame
def multiplication(step,prevframe):
  name1 = names[random.randint(0,len(names) -1 )]
  name2 = names[random.randint(0,len(names) -1)]
  objectinquestion = objectsinquestion[random.randint(0,len(objectsinquestion) - 1)]
  action = actions[random.randint(0,len(actions) - 1)]
  firstnum = random.randint(1,10)
  secondnum = random.randint(1,10)
  frame = {
  'question' : f"{name1} {action['first']} {firstnum} {objectinquestion} , then {name1} multiplies the amount of {objectinquestion} {name1} {action['fourth']} by {secondnum}, how many {objectinquestion} does {name1} {action['sixth']}  ?",
  'answer' : f"{name1} {action['fourth']} {firstnum * secondnum} {objectinquestion} . ",
  'type' : "multiplication",
  'step' : 1
  }
  if step == 1:
    frame = {
    'question' : f"{name1} {action['first']} {firstnum} {objectinquestion} , then {name1} multiplies the amount of {objectinquestion} {name1} {action['fourth']} by {secondnum}, afterwords",
    'answer' : f"{name1} {action['fourth']} {firstnum * secondnum} {objectinquestion} . ",
    'numericalanswer' : firstnum * secondnum,
    'type' : "multiplication",
    'name1' : name1,
    'definedobject' : objectinquestion
    }
  elif step == 2:
    secondnum = random.randint(1,100)
    frame = {
    'question' : f"{prevframe['question']} {prevframe['name1']} multiplies the amount of {prevframe['definedobject']} {prevframe['name1']} {action['fourth']} by {secondnum},  how many {prevframe['definedobject']} does {prevframe['name1']} {action['sixth']}  ?",
    'answer' : f"{prevframe['name1']} {action['fourth']} {prevframe['numericalanswer'] * secondnum} {prevframe['definedobject']} . ",
    'numericalanswer' : prevframe['numericalanswer'] * secondnum,
    'type' : prevframe['type'] + "multiplication",
    'step' : 2
    }
  return frame
def divison(step,prevframe):
  name1 = names[random.randint(0,len(names) -1 )]
  name2 = names[random.randint(0,len(names) -1)]
  objectinquestion = objectsinquestion[random.randint(0,len(objectsinquestion) - 1)]
  action = actions[random.randint(0,len(actions) - 1)]
  firstnum = random.randint(1,100)
  secondnum = random.randint(1,firstnum)
  #while (firstnum/secondnum) - round(firstnum/secondnum) != 0:
    #secondnum = random.randint(1,firstnum)
  frame = {
  'question' : f"{name} {action['first']} {firstnum} {objectinquestion} , then {name} divides the amount of {objectinquestion} {name} {action['fourth']} by {secondnum}, how many {objectinquestion} does {name} {action['sixth']}  ?",
  'answer' : f"{name} {action['eighth']} {round(firstnum/secondnum,2)} {objectinquestion} left. ",
  'type' : "divison",
  'step' : 1
  }
  if step == 1:
    frame = {
    'question' : f"{name1} {action['first']} {firstnum} {objectinquestion} , then {name1} divides the amount of {objectinquestion} {name1} {action['fourth']} by {secondnum}, afterwords",
    'answer' : f"{name1} {action['fourth']} {round(firstnum / secondnum,2)} {objectinquestion} . ",
    'numericalanswer' : round(firstnum / secondnum,2),
    'type' : "divison",
    'name1' : name1,
    'definedobject' : objectinquestion
    }
  elif step == 2:
    secondnum = random.randint(1,100)
    frame = {
    'question' : f"{prevframe['question']} {prevframe['name1']} divides the amount of {prevframe['definedobject']} {prevframe['name1']} {action['fourth']} by {secondnum},  how many {prevframe['definedobject']} does {prevframe['name1']} {action['sixth']}  ?",
    'answer' : f"{prevframe['name1']} {action['fourth']} {round(prevframe['numericalanswer'] / secondnum,2)} {prevframe['definedobject']} . ",
    'numericalanswer' : round(prevframe['numericalanswer'] / secondnum,2),
    'type' : prevframe['type'] + "divison",
    'step' : 2
    }
  return frame
def create_two_step_list(sizeinput):
  listofquestions = []
  for topfunction in [multiplication,divison,subtraction,addition]:
    for botfunction in [multiplication,divison,subtraction,addition]:
       for i in range(0,sizeinput):
          test = topfunction(1,0)
          test = botfunction(2,test)
          test['predictedanswer'] = predict(test['question'])
          test['distance'] = distance(model.encode(test['answer']),model.encode(test['predictedanswer']))
          listofquestions.append(test)

  return listofquestions
def create_one_step_list(sizeinput):
  listofquestions = []
  for topfunction in [multiplication,divison,subtraction,addition]:
    for i in range(0,sizeinput):
      test = topfunction(0,0)
      test['predictedanswer'] = predict(test['question'])
      test['distance'] = distance(model.encode(test['answer']),model.encode(test['predictedanswer']))
      listofquestions.append(test)
  return listofquestions
