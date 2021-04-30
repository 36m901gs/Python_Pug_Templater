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


def pug_templify(resource,caption,wild_card):
    

    #if line is a URL wildcard, ok STRIP THE LINE FORMATTING OFF OF THIS!!!
    if wild_card == '^|':
        temp_wrap = "\n a(href='{}') {} \n | ".format(resource,caption)
        
    return temp_wrap

def wildcard_location(block,wildcard):

    beg = block.find(wildcard, 0)
    end = block.find(wildcard[::-1], 0)
    end+=len(wildcard)

    coordinates = [beg,end]

    return coordinates


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


def replacement_step(text_block,resources,wild_card):

    #formatting actually needs to be handled here
    
    url = '   www.test.com   '
    stored=text_block
    txtblock_index=0
    resource_index=0
    while txtblock_index < len(stored):
        curr_text = stored[txtblock_index]
        while wild_card in curr_text:
            locations_wc = wildcard_location(curr_text, wild_card)
            #need to strip the string formatting off the resources
            test_repl=pug_templify(resources[resource_index].strip('\n'),curr_text[locations_wc[0]+len(wild_card):locations_wc[1]-len(wild_card)], wild_card)
            curr_text=curr_text.replace(curr_text[locations_wc[0]:locations_wc[1]], test_repl)
            resource_index+=1

          
        stored[txtblock_index]='p \n |' + curr_text
        txtblock_index+=1
        resource_index=0
        
    return stored
    


def process_switch(line,resource_switch,wildcard):
    
    switch=resource_switch
    if '%%%' in line:
        switch=1
    

    return switch
        


with open('EasyCase', 'r') as bl:
    txt_blocks=[]
    resources = []
    wild_card_index = []
    replacement_index = 0
    resource_switch = 0
    first_line.append(bl.readline())
    next(bl)
    wildcard = '^|'
    for line in bl: #collection phase
        resource_switch=process_switch(line,resource_switch,wildcard)
        if resource_switch==0 and len(line)>10:
            txt_blocks.append(line)
        if resource_switch==1 and len(line)>4 and '%%%' not in line:
            resources.append(line)
            replacement_index+=1

    #process phase here        
    #print(resources)
    testbl=replacement_step(txt_blocks,resources,wildcard)
    for l in testbl:
        print(l)

#finish here - write it out to a file
final_lines = ""
with open('Header', 'r') as css:
    final_lines+=css.read()
    
final_pug_file = open('Pugified.pug','w')
for l in testbl:
    final_lines+=l
final_pug_file.write(final_lines)
final_pug_file.close()
print("COMPLETE")
  
