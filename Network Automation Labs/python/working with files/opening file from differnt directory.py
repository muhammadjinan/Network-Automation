file = open('C:\\User\\admin\\Documents\\python\\test.txt','r')  # OR #
file = open(r'C:\User\admin\Documents\python\test.txt','r')      # Both commands give same result (use only one)
# This is not a real directory, Change the directory of the real file so that you can open it
print(file.read())