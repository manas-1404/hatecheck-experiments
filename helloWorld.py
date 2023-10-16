# Initialise relevant packages
import pandas as pd
import pickle


# Text cleaning
from html import unescape
import re
import string
import wordsegment as ws
import emoji
ws.load() # load vocab for word segmentation