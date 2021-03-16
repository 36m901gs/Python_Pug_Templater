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


def replacement_step(text_block,resources, array_pairs,wild_card):
    
    url = '   www.test.com   '
    stored=text_block
    txtblock_index = 0
    resource_index=0

    while txtblock_index <= len(txt_block):
        #need to loop it here, through the array pairs associated with that text block, you're getting the phrase by substringig
        # via index, and replacing it with the end value, which will pull from resources
        new_string = text_block[txtblock_index].replace(text_block[array_pairs[0][init_index]:array_pairs[1][init_index]+ len(wild_card)], resources[resources_index])


    return stored
    

    

    





    #old
##    jar = text_block
##    while init_index < len(array_pairs[0]):
##        new_string =  jar.replace(text_block[array_pairs[0][init_index]:array_pairs[1][init_index]+ len(wild_card)], url)
##        init_index += 1
##        jar=new_string
##        stored.append(new_string)
##    return jar

def process_switch(line,resource_switch,wildcard):
    
    switch=resource_switch
    if '%%%' in line:
        switch=1
    
   # if switch==0:
    #    if '\n' in line and len(line) > 10:
     #       array_set = wildcard_prep(line,wildcard)
      #      print(replacement_step(line,array_set,wildcard))
        
    if switch==1:
        print("Resource_stuff")
                  


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
            wild_card_index.append(wildcard_prep(line,wildcard))
        if resource_switch==1 and len(line)>4 and '%%%' not in line:
            resources.append(line)
            replacement_index+=1
            #put line in current indices found in wild_card_index, then increment it

            #!!!!!!!!!!! Issue to fix - need to change how i wrote replacement step method. It's built for
            # static resources. Need to modify it to accept the new line and insert it into the original block.

            #right now i have those text blocks put in txt_blocks. so (1) it needs to accept that. Instead of storing resources sequentially,
            # maybe i should have a resources block too? We can make it elegant later, let's just make it work for now

    #process phase here        
    print(txt_blocks)        
    print(resources)    
    print(str(wild_card_index[0][0][0]) + '     ' + str(wild_card_index[0][1][0]))

    #for block in txt_blocks:
        
        
       
##        if '\n' in line and len(line) > 1:
##            wildcard = '^|'
##            array_set = wildcard_prep(line,wildcard)
##            print(replacement_step(line, array_set,wildcard))

            # print("p.\n\t"+line)
