#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec 15 13:11:32 2019

@author: vv
"""
import numpy as np
import requests
import os
import tweepy
#from our keys module (keys.py), import the keys dictionary
from keys import keys
import json
from cnvrg import Endpoint
from transformers import pipeline

nlp = pipeline("question-answering")

data=""
try:
    with open('/data/bert/info.txt', 'r') as file:
        data = file.read().replace('\n', '')
except:
    print('create a dataset ')
context = r"""
Extractive Question Answering is the task of extracting an answer from a text given a question. An example of a
question answering dataset is the SQuAD dataset, which is entirely based on that task. If you would like to fine-tune
a model on a SQuAD task, you may leverage the examples/question-answering/run_squad.py script. A cnvrg workspace is an interactive environment for developing and running code.
You can run any kind of interactive development environment, Python scripts and much more.
The environment is pre-configured (meaning all your dependencies are preinstalled). All the files and data in your workspace will be preserved for you, across restarts. Your workspace has automatic version control and scalable compute available, so that you can use unlimited compute resources to do your data science research.
cnvrg.io has built-in support for JupyterLab, JupterLab on Spark, R Studio and Visual Studio Code to run on remote computes.
cnvrg.io is a machine learning platform built by data scientists, for data scientists.
cnvrg.io helps teams to manage, build and automate machine learning from research to production.
Have additional questions? Email us at support@cnvrg.io
Manage, build and automate ML
Manage Deploy more models with drag and drop machine learning pipelines. cnvrg.io offers enterprises with a dynamic automated machine learning and meta learning technology that helps data scientists, software engineers or even business analysts apply state-of-the-art algorithms on their datasets in a few clicks.
Build Run and track experiments in hyperspeed with the freedom to use any compute environment, framework, programming language or tool - no configuration required.
Automate Build more models and automate your machine learning from research to production using reusable components and drag-n-drop interface. Add continual and active learning to your models with one click.
"""+data


def respo(question):
    resp = nlp(question=question, context=context)
    return resp['answer']



CONSUMER_KEY = keys['consumer_key']
CONSUMER_SECRET = keys['consumer_secret']
ACCESS_TOKEN = keys['access_token']
ACCESS_TOKEN_SECRET = keys['access_token_secret']

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

def reply(msg):
    rep = ""

    tweet = msg
    print('tweet_input', tweet)
    sn = tweet['screen_name']
    ids = tweet['id']
    text = tweet['text']
    peeps = ['cnvrg_io', 'Maya_Maxine', 'YanivGoldenberg', 'yochze', 'VVagias']
    rep = respo(text)
    if sn in peeps:
        try:
            api.update_status(rep, ids)
            #print('bot would reply in production')
        except:
            print('caught error')
                

    print(rep)
    return(rep)