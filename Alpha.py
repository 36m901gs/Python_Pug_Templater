#!/usr/bin/python
# -*- coding: utf-8 -*-
import re

##test = open('exproc.txt',"r")
##test_block = test.readlines()
##test.close()

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


def replacement_step(text_block, array_pairs, wild_card):
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


# this will ultimately be template builder function

with open('EasyCase', 'r') as bl:
    first_line.append(bl.readline())
    next(bl)
    for line in bl:
        if '\n' in line and len(line) > 1:
            wildcard = '^|'
            array_set = wildcard_prep(line,wildcard)
            print(replacement_step(line, array_set, wildcard))

            # print("p.\n\t"+line)


			
