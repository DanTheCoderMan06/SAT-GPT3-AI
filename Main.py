!pip install transformers
!pip install sentence_transformers 
!pip install openai
import json
import pandas as pd
import sys
import os
sys.path.append('/files')
from functions import *
import math
import random
import numpy as np
import matplotlib as plt
import scipy
import openai
import statistics
from fractions import Fraction
from sentence_transformers import SentenceTransformer as st
import logging
import threading
import time
#Importing All of the functions
model = st("bert-base-nli-mean-tokens")
openai.api_key = "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"
keys = ["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","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"]
from functions import *
sample_size = 1
keys = ["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","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"]
names = []
#The Variables for the Program, make sure you have a folder named files under the parent of this .py file.
df = pd.read_csv('/files/Indian-Male-Names.csv')['name']
dflist = list(df)
for name in dflist:
  try:
    names.append(name.split(' ')[0])
  except:
    pass
df = pd.read_csv('/files/Indian-Female-Names.csv')['name']
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
#Now for the actual code
running = True
def constant_updates():
  while running:
    distances = create_one_step_list(1) + create_two_step_list(1) 
    random.shuffle(distances)
    newdistances = pd.DataFrame(distances)
    olddistances = pd.read_csv('/files/distances2.csv')
    distanceframe = pd.concat([newdistances,olddistances],ignore_index=True)
    print(len(distanceframe))
    distanceframe.to_csv('/files/distances2.csv')
while True:
  running = True
  loop = threading.Thread(target = constant_updates,args = ())
  loop.start()
  stop = input('Respond to this message once you have created a data-set!')
  running = False
  stop = input('Are you ready to Quit? (y = yes, anything else is no)')
  if stop == 'y':
    break
distances = pd.read_csv('/content/drive/MyDrive/distances2.csv')
distanceframe = pd.DataFrame(distances)
distanceframe.to_csv('/content/drive/MyDrive/distances2.csv')
distanceframe.groupby('type',as_index = False).mean().plot.bar('type','distance')
print(len(distanceframe))
from scipy.stats import ttest_ind
marr = distanceframe[distanceframe['type'] == 'addition'].distance.values
sarr = distanceframe[distanceframe['type'] == 'subtraction'].distance.values
ttest_ind(marr,sarr)
