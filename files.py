files= open("notes.txt","w")
files.write("This is a test file for wrting and reading purpose")
files.close()

files= open("notes.txt","r")
content = files.read()
print(content)
files.close()

#append mode.
files = open("notes.txt","a")
files.write("\nThis is an additional line.")
files.close()

files =open("notes.txt","r")
content = files.read()
print(content)
files.close()
