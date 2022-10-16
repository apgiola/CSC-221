import re
user_text = input()

while True:
    string = user_text 
    string.rstrip()
    count = len(re.findall("[a-zA-Z_?]", string))
    print (count)
    break