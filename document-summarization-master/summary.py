# -*- coding: utf-8 -*-
"""
Created on Fri Feb 14 02:12:36 2020

@author: GAURANG
"""

from sumy.parsers.plaintext import PlaintextParser #We're choosing a plaintext parser here, other parsers available for HTML etc.
from sumy.nlp.tokenizers import Tokenizer 
from sumy.summarizers.lsa import LsaSummarizer #We're choosing Luhn, other algorithms are also built in

file = "source.txt" #name of the plain-text file
parser = PlaintextParser.from_file(file, Tokenizer("english"))
summarizer_lsa = LsaSummarizer()

summary_2 =summarizer_lsa(parser.document,15) #Summarize the document with 5 sentences

for sentence in summary_2:
    print(sentence)