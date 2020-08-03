import random
  #iterate through list to get the wrda and definitio we have createdimport random

def get_def_and_pop(word_list,word_dic):
    random_index = random.randrange(len(word_list)) #random number fro 0 to word length
    word = word_list.pop(random_index)
    definition = word_dict.get(word) # can access the defintion by using it key
    return word , definition

def get_word_and_definition(rawstring): # to separate the word from definition
    word, definition = rawstring.split(',' , 1)  # to split the rawsting by comma
    return word, definition # tuple return 


fh = open("Vocabulary_list.csv","r")
wd_list = fh.readlines()  #reading the file
# print(wd_list)  #printing the liss

wd_list.pop(0) # this will remove the first entry
wd_set = set(wd_list) #remove the duplicate words
fh = open("Vocabulary_set.csv","w") #open the file without duplicate
fh.writelines(wd_set)

word_dict = dict() # make a dictionary
for rawstring in wd_set : #iterate through list to get the word and definition from list we have created
    word ,definition = get_word_and_definition(rawstring) # give us word and definition
    word_dict[word] = definition # adding into the dictionary with word as key and definition as value
    #print(word)
 
while True:
 wd_list = list(word_dict) # give us list of kesy from the dictionary which is list of not not definit

 choice_list = [] 
 for x in range(4): 
      word ,definition = get_def_and_pop(wd_list , word_dict)
      choice_list.append(definition)
     

 random.shuffle(choice_list)

 print(word)
 print("----------------")
 for idx,choice in enumerate(choice_list):
      print(idx+1 , choice) 
 choice = int(input("enter 1 ,2 ,3 ,or 4 : 0 to exit"))
 if choice_list[choice-1] == definition:
      print("correct\n")
 elif choice ==0:
      exit(0)
 else:
      print("incorrect")

