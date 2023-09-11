# batchtrans
Using a python library to translate a file of words and sentences

## why this repository?
The origin of creating this repository lies in the fairification of data, see [go-fair.org](https://www.go-fair.org/fair-principles/fairification-process/). This may seem a long shot, but in this case I was given the assignment to provide metadata of a study with more than 4500 variables. That is a lot, but the nature of the software that was used to collect the data creates for every variable a unique name, even if the question is repeated at various time points. This still leaves about 800 variables and because the study was conducted in the Netherlands, all questions were in Dutch. Anyway ...

## purpose of this repository
The purpose is to be able to use as input a file with variable-identifiers plus variable-labels and then add the English translation to that.

## googletrans
Starting point was [googletrans](https://pypi.org/project/googletrans/)
Install it using pip with:  
pip install googletrans==4.0.0-rc1  
and don't forget the version number
