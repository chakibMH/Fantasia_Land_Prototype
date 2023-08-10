# -*- coding: utf-8 -*-
"""
Created on Tue Oct 25 11:12:28 2022

@author: chaki
"""

import openai
import codecs
import pandas as pd

openai.api_key = "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"

def request(t):
    res = openai.Completion.create(
      model="text-davinci-002",
      prompt = t,
      temperature=0.7,
      max_tokens=256,
      top_p=1,
      frequency_penalty=0.0,
      presence_penalty=0.0,
      #stop=[]
    )  
    
    msg = res['choices'][0]['text']
    
    return msg

def read_exemple(ex_file):
    
        with codecs.open('..\\data\\clean\\exemples\\'+ex_file, encoding='utf-8') as f:
            ex = f.read()
        
        return ex
    
    
# {type, location, duration, Price_min, Price_max, description}

def data_extraction(context, question, ex_file):
    
    # read exemple file
    
    ex = read_exemple(ex_file)
    
    # generate the prompt
    
    t = ex + context + question 
    
    res = request(t)
    
    return res

def event_type(context, q_start, ex_file = "package_or_independant_1.txt"):
    
    
    q = "\n"+q_start+", is the type of program more of package tour or an independant activity?\n"\
    +"\nA:"
        
     
    res = data_extraction(context, q, ex_file)
    
    
    if 'independent activity' in res:
        activity_type = 'independent activity'
    elif 'package tour' in res:
        activity_type = 'package tour'
    
    return activity_type
    


def get_prices_info(context, q_start, ex_file = "price_2.txt"):
    

    
    q = "\n"+q_start+", what is the minimum and maximum cost (minimum/maximum)?"\
        +"\nA:"
        
    res = data_extraction(context, q, ex_file)
    
    p_min,p_max = [float(e) for e in res.split("/")]
    
    return p_min,p_max

def get_main_location(context, q_start, ex_file = 'main_location_1.txt'):
    
        q = "\n"+q_start+", where the main event is planned  to be?"\
        +"\nA:"
        
        res = data_extraction(context, q, ex_file)
        
        # trim spaces
        location = res.strip()
        
        return location
    
def get_total_duration(context, q_start, ex_file = 'duration_1.txt'):
    
        q = "\n"+q_start+", what is the duration of the whole program?"\
        +"\nA:"
        
        res = data_extraction(context, q, ex_file)
        
        dur = res.strip()
        
        return dur


def data_extraction_independent(prog, org_name):
    pass

def data_extraction_package(prog, org_name):
    pass

def structure_data(prog, q_start = "Q: according to the program 707, ", org_name = 'non_ext_my_org'):
    
    
    context = "\nprogram 707 : "+prog
    
    # extract event type
    t = event_type(context, q_start)
    
    
    min_p, max_p = get_prices_info(context,  q_start)
    
    location = get_main_location(context,  q_start)
    
    
    dur = get_total_duration(context,  q_start)
    
    return {"event_type":[t], 'min_price':[min_p], 'max_price':[ max_p], 'location': [location], 'duration':[dur]}
    
    # extract date
    
    # extract the location
