##########################################################
#             Version 1: Context period divider
#         prerequisites: english punctuation/ blank after period
#
#                          Made by: Veritas
##########################################################
import csv 
import re
import numpy as np
from itertools import repeat
import pprint
import fileinput
# import jieba

def main():
    path = 'lianchi.md'
    file = open(path, "r", encoding='utf-8') #Chinese Characters
    file = file.read()
    file = re.split(r'(?<=\?|\!|\.) (?!(?:[^(|"]*\([^)|"]*\))*[^()]*\))', file) #positive look behind-> matches group before the main expression without including it
    # file = re.split(r'(?<=\?|\!|\.) (?!(?:[^(|"]*\([^)|"]*\))*[^()]*\))', file) #positive look behind-> matches group before the main expression without including it
    
    
    #export data
    with open('new_parse.txt', 'w', encoding='utf-8') as output:
        #file = [x for item in file for x in repeat(item, 5)]
        output.write("\n\n".join(file))

main()



############################################# CARCASSESS ########################################################################################

  # #replace period to have a space behind
    # checkWords=(".")
    # repWords=(". ") doesnt work for chinese
    
    # for line in file:
    #     for check, rep in zip(checkWords, repWords):
    #         file = line.replace(check, rep)
    
    # print(file)

# import csv 
# import re
# import numpy as np
# from itertools import repeat
# import pprint
# # import jieba

# def main():
#     path = 'fengyuan.txt'
#     file = open(path, "r", encoding='utf-8')
#     file = file.read()
#     file = re.split(r'(?<=\?|\!|\.)', file) #positive look behind-> matches group before the main expression without including it
#     #file = re.split(r'(?<=\?|\!|\.) (?!(?:[^(]*\([^)]*\))*[^()]*\))', file) #positive look behind-> matches group before the main expression without including it
#     # print(file)
    
#     #export data
#     with open('new_parse.txt', 'w', encoding='utf-8') as output:
#         # output.write("\n".join(file))
#         # pp = pprint.PrettyPrinter(indent=4)
#         file = [x for item in file for x in repeat(item, 5)]
#         # pp = pprint.PrettyPrinter(indent=file, stream=output)
#         output.write("\n".join(file))
#         # output.write("\n".join(file))

# main()

# import csv 
# import re
# # import jieba

# def main():
#     path = 'zhuge.txt'
#     file = open(path, "r", encoding='utf-8')
#     file = file.read()
#     file = re.split(r'(?<=\?|\!|\.) (?!(?:[^(]*\([^)]*\))*[^()]*\))', file) #positive look behind-> matches group before the main expression without including it
#     #file = file.read().split('.') 
    
#     #export data
#     with open('new_parse.txt', 'w', encoding='utf-8') as output:
#         #output.write(str(file))
#         output.write("\n".join(file))
    
# main()

# import csv 
# import re
# import jieba

# def main():
#     path = 'Taiwan.txt'
#     file = open(path, "r", encoding='utf-8')
#     file = file.read()
#     file = re.split(r'(?<=\.)', file) #positive look behind-> matches group before the main expression without including it
#     #file = file.read().split('.') 
    
#     #export data
#     with open('new_parse.txt', 'w', encoding='utf-8') as output:
#         #output.write(str(file))
#         output.write("\n".join(file))
    
# main()




# with open(path,newline='') as csv_file:
# #with open(path ,newline='',encoding="utf-8") as csv_file:
#     reader = csv.reader(csv_file, lineterminator='\n') # create new reader
#     next(reader) #skip first row
#     sentence = [row[0].split("。")[0] for row in reader]

# with open('new_parse.csv', 'w') as new_file:
#     csv_writer = csv.writer(new_file, lineterminator='\n')
    
#     for line in sentence:
#         csvwriter.writerow(line)
    
    
    
    
#     csv_reader = csv.reader(csv_file)
#     csv_file= csv_file.read().replace("\n", "")
#     csv_file= re.compile(r'["~！@#￥%……&*（）——+《》：“{}|？，。、；‘【】、=-]')
#     csv_file = re.split(r'(?<=\。) ', csv_file)
#     # csv_file= re.sub(r'', csv_file)

    
# with open('new_parse.csv', 'w') as new_file:
#     csv_writer = csv.writer(new_file, delimeter='-')
    
#     for line in csv_reader:
#         print(line)
    