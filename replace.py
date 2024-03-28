initialSentence = "The!quick!brown!fox!jumps!over!the!lazy!dog."

sentence2 = initialSentence.replace("!", " ")

print(sentence2)

sentence3 = sentence2.upper()

print(sentence3)

sentence4 = reversed(sentence2)
sentence4 = ''.join(sentence4)
print(sentence4)
