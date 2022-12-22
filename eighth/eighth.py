str = 'X-DSPAM-Confidence:0.8475'
find = str.find(":")
print(float(str[find+1:]))
