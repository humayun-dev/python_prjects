# Converting text/string to hand written style text
# for this purpose, pywhatkit is used which has some other functions such as sending whatsapp messages, play youtube 
# video, perform google search and get information on a particular topic

import pywhatkit as pw     # pip install pywhatkit for text to handwritten text

text = "I am text that will be converted to the hand written style using functions of the pywhatkit"

pw.text_to_handwriting(text,"convertedtext.png",[10,10,10])
print(" END ")