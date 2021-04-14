alph="abcdefghijklmnopqrstuvwxyz"
punc=" .,!'?"
def vignere_decoder(message,key):
#Define the keyword phrase
    keyword_phrase=""
    keyword_counter=0
    for i in range(0,len(message)):
        if not message[i] in punc:
            if keyword_counter>len(key)-1:
                keyword_counter=0
            keyword_phrase+=key[keyword_counter]
            keyword_counter+=1
        else:
            keyword_phrase+=message[i]
    decoded=""
#Decode the message
    key_counter=0
    for letter in message:
        if letter in punc:
            decoded+=letter
        else:
            position_ms=alph.find(letter)
            position_key=alph.find(keyword_phrase[key_counter])
            decoded_position=position_ms-position_key
            if decoded_position<0:
                decoded_position=decoded_position+26
            decoded+=alph[decoded_position]
        key_counter+=1
    return decoded

def vignere_coder(message,key):
#Define the keyword phrase
    keyword_phrase=""
    keyword_counter=0
    for i in range(0,len(message)):
        if not message[i] in punc:
            if keyword_counter>len(key)-1:
                keyword_counter=0
            keyword_phrase+=key[keyword_counter]
            keyword_counter+=1
        else:
            keyword_phrase+=message[i]
    coded=""
#Code the message
    key_counter=0
    for letter in message:
        if letter in punc:
            coded+=letter
        else:
            position_ms=alph.find(letter)
            position_key=alph.find(keyword_phrase[key_counter])
            coded_position=position_ms+position_key
            if coded_position>25:
                coded_position=coded_position-26
            coded+=alph[coded_position]
        key_counter+=1
    return coded
