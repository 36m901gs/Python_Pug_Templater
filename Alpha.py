#!/usr/bin/python
# -*- coding: utf-8 -*-
import re



templates = ['a(href=) caption']
special_characters = [
    '*',
    '!',
    '~',
    '^',
    '^^',
    '%%%',
    ]
first_line = []
line_capture = []
resource_characters = ['^', '^^']
special_character_locations = []

def resource_pull(text_file):
    print('test')
    # scan entire doc, cut from the %%% and store resources. return the block without those
    # run this before you run anything else
    # remember, when you look at a big block of text the pc just sees one line
    # probably should use a while so that we can just keep on keeping on?
##    for line in text_file:
##        if '%%%' in line and len(line) < 5:
            

def wildcard_prep(block, wildcard):
    
        
    array_pairs = [[], []]
    start_ind = 0
    array_ind = 0
    while block.find(wildcard, start_ind) != -1:
        array_pairs[0].append(block.find(wildcard, start_ind))
        start_ind = array_pairs[0][array_ind] + 1
        array_pairs[1].append(block.find(wildcard[::-1], start_ind))
        start_ind = array_pairs[1][array_ind] + 1
        array_ind += 1
    return array_pairs


def replacement_step(text_block, array_pairs,wild_card):
    
    url = '   www.test.com   '
    stored=[]
    init_index = 0
    jar = text_block
    while init_index < len(array_pairs[0]):
        new_string =  jar.replace(text_block[array_pairs[0][init_index]:array_pairs[1][init_index]+ len(wild_card)], url)
        init_index += 1
        jar=new_string
        stored.append(new_string)
    return jar

def process_switch(line,resource_switch,wildcard):
    switch=resource_switch
    if '%%%' in line:
        switch=1
    
    if switch==0:
        if '\n' in line and len(line) > 1:
            array_set = wildcard_prep(line,wildcard)
            print(replacement_step(line,array_set,wildcard))
        
    if switch==1:
        print("Resource_stuff")
                  


    return switch
        

# this will ultimately be template builder function

#so tbh, really should be loading resources at the end? the wildcard phase should probs be the same as
# the resources phase
#resourcepull either goes here or one below. ok so change this to respond to switches instead, if its
# a block switch, use one set of methods/procedures, else use resource methods/procedures
with open('EasyCase', 'r') as bl:
    resource_switch = 0
    first_line.append(bl.readline())
    next(bl)
    wildcard = '^|'
    for line in bl:
        resource_switch=process_switch(line,resource_switch,wildcard)
        print(resource_switch)
       
##        if '\n' in line and len(line) > 1:
##            wildcard = '^|'
##            array_set = wildcard_prep(line,wildcard)
##            print(replacement_step(line, array_set,wildcard))

            # print("p.\n\t"+line)
