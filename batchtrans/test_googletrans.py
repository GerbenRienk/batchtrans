'''
Created September 2023
This file is meant to test just the basic use of googletrans
@author: GerbenRienk
'''

from googletrans import Translator


def test_gtrans():

    translator = Translator(service_urls=['translate.google.nl'])
    translation = translator.translate('bien sur, naturellement')
    print(translation.text)
               
if __name__ == '__main__':
    test_gtrans()
