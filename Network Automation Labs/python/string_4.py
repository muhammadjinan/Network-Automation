txt='USERNAME cCISCO PASSWORD CCIE'
if 'PAss'.lower().upper() in txt:
    print('>>>> FOUND <<<<'.center(20))
print("> CommandFind <".center(20))
# If no match found ".find()" will return "-1"
print(txt.find("C"))
print(txt.lower().upper().find("C"))
print(txt.find("CI"))
print(txt.find("CIE"))
print("> CommandIndex <".center(20))
# If no match found ".index()" will return "error"
print(txt.index("C"))
print(txt.lower().upper().index("C"))
print(txt.index("CI"))
print(txt.index("CIE"))