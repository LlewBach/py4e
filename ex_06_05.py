text = "X-DSPAM-Confidence:     0.8475"

semiLoc = text.find(':')
print(semiLoc)

num = float(text[semiLoc + 1:].strip())
print(num)