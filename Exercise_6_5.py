str = 'X-DSPAM-Confidence: 0.08475'
point = str.find(":")
result = float(str[point+1: ])
print(result)