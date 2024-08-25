from os.path import exists
from os import remove
from termcolor import colored

def createFile(filePath : str) :
    with open(filePath, 'a') as f:
        f.close()

def createnv() :
    htmlFileName : str = input("Enter the html file name :\t")
    cssFileName : str = input("Enter the css file name :\t")
    jsFileName : str = input("Enter the javascript file name :\t")
    files : dict[str, str] = {htmlFileName : "html", cssFileName : "css", jsFileName : "js"}
    for file in files.keys():
        fileName : str = f"{file}.{files[file]}"
        filePath : str = fr"{path}{fileName}" if (path[-1] == "\"") else f"{path}\{fileName}"
        if not exists(filePath):
            createFile(filePath)
            print(colored(f"{fileName} has been created successfully!", "green"))
        else:
            print(colored(f"{fileName} is allready exists!", "blue"))
            choice : str = input(f"Do you want to renew the file {fileName}\n\t[Y]es\t[N]o\n>>>\t")
            if choice.lower() == "y":
                remove(filePath)
                createFile(filePath)

path : str = input("Enter the path :\t")
createnv()