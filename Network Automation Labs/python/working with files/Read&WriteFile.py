with open('Second.txt','a+') as F:
    F.write('\nhaaNew Line+2')
    # Write in new line
with open('Second.txt','r+') as R:
    text = R.read()
    print(text)
    # Read and print to console