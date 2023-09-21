'''
Created September 2023
This file is meant to test just the basic use of googletrans
@author: GerbenRienk
'''

from googletrans import Translator
import csv
import time
from utils.reporter import Reporter

def test_gtrans():

    translator = Translator()
    input_rows=[]
    counter = 0
    tot = 0
    #try to open a csv-file
    # with open('./files/qsel_field_labels_nl.csv', newline='') as f:
    with open('./files/qsel_options_nl.csv', newline='') as f:
    # with open('./files/input_example.csv', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            input_rows.append(row)
    
    
    for row in input_rows:
        print(row)
        translation = translator.translate(row[1])
        output_file = Reporter()
        # only do something with nl-texts
        if (translation.src == 'nl'):
            # print(row[0] + ';' + translation.text) 
            output_file.append_to_report(row[0] + ';' + translation.text)
        else:
            output_file.append_to_report(row[0] + ';')
        output_file.close_file()
        
        # take 5 if we're running too long
        counter = counter + 1
        tot = tot + 1
        # print(counter + ' ' + tot)
        if (counter > 99):
            counter = 0
            # translator = Translator()
            time.sleep(5)
               
if __name__ == '__main__':
    test_gtrans()
