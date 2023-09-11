'''
Created September 2023
This file is meant to test just the basic use of googletrans
@author: GerbenRienk
'''

from googletrans import Translator
import csv

def test_gtrans():
    translator = Translator()
    ''' 
    translation = translator.translate('bien sur, evidement')
    print(translation.text)
    ''' 
    # create a list for writing
    output_list = []
    
    #try to open a csv-file
    with open('./files/qsel_field_labels_nl.csv', newline='') as f:
    # with open('./files/input_example.csv', newline='') as f:
        reader = csv.reader(f, delimiter=';')
        for row in reader:
            print(row)
            # make this term a translation-object
            translation = translator.translate(row[1])
            # only do something with nl-texts
            if (translation.src == 'nl'):
                # print(row[0] + ' = ' + translation.src + ' ' + row[1])
                # print(row[1] + ' = ' + translation.text)
                one_new_row=[row[0], translation.text]
                output_list.append(one_new_row)
        
    # write the results to file
    with open('./files/output.csv', 'w', newline='') as f:
        writer = csv.writer(f, delimiter=';', quotechar='"')
        writer.writerows(output_list)
               
if __name__ == '__main__':
    test_gtrans()
