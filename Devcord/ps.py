import psutil

def checkprocess(name):
    for proc in psutil.process_iter():
        print(proc.name.lower())
checkprocess('yahallo')