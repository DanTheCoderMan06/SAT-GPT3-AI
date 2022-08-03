!pip install transformers
!pip install sentence_transformers 
!pip install openai
import json
import pandas as pd
import time
import sys
import os
sys.path.append('/content/drive/MyDrive')
from functions import *
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
openai.api_key = "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"
keys = ["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","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"]
sys.path.append('/')
print('Test')
