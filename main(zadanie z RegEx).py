import re

f = open("D:\Oleh Radchenko 2-P\pythonProject4\Lib\zakon.txt", "r", encoding='UTF-8')
text = f.read()
f.close()
x = re.findall("rycerz|zakon", text)
print(x,"\n")
y = re.findall("b|c|ć|cz|d|dz|dź|dż|f|g|ch|j|k|l|ł|m|n|ń|p|r|s|ś|sz|t|w|z|ź|ż|rz", text)
print(y,"\n")