'''
Write a program that takes anonymous letter  and text from magazine 
and checks if the anaonymous letter can be produced from the magazine text

For the Anonymoius letter to be written from the magazine ,
 the ,magazine must contanin all the chaaracters of the letter and the number of times 
 of each chars must match

Default approach : Create a Has table for both the magazine text Anonymous text and check the cont of 
the each characyers for the Anonymous letter  is present in the Magazine.
---
Better Approach :
create :Hash table for the Anonymous letter

 Loop through the Magazine text and check if its in the hast able and the count matches

 For each caharacter in HAsh table that matches in the magazine text,reduce the count 
 if the Hash table becomes empty , then we are sure all the text in Anonymous is present in Magazine

'''
import collections

def is_letter_constructible_from_magazine(letter_Text:str,magazine_text:str)->bool:
    char_frequency_letter = collections.Counter(letter_Text)
    for text in magazine_text:
        if text in char_frequency_letter:
            char_frequency_letter[text] -=1
            if  char_frequency_letter[text] == 0:
                del char_frequency_letter[text]
            if not char_frequency_letter:
                #All the chars are accounted for , just return True
                return True
    return not char_frequency_letter

# Driver 

letter = "abcdefghij" 
mag = "abcd"
print(is_letter_constructible_from_magazine(letter,mag))
# letter = 'abcdefg',mag = 'abcdefghijk' ; return True
# letter = 'abcdefghij',mag = 'abcd' ; return False      
