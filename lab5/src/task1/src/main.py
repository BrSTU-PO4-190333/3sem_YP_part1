import os

def main():
    numberFiles = 0
    numberFolders = 0
    print('| %-8s | %-32s |' % ('Type', 'Name'))
    print('| %-8s | %-32s |' % ('--------', '--------------------------------'))
    for i in os.listdir("./"):
        
        if os.path.isfile(i):
            numberFiles += 1
            print('| %-8s |' % 'file', end = '')
        else:
            numberFolders += 1
            print('| %-8s |' % 'folder', end = '')
        print(' %-32s |' % i)

    print('number files: %d' % numberFiles)
    print('number folders: %d' % numberFolders)

main()