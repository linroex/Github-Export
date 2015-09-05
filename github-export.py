import sys
import git

def main():
    
    if sys.argv[1] == 'export':
        print(getAllGithubUrl())

def cloneAll():
    pass

def getAllGithubUrl():
    with open("url.txt") as f:
        return f.read().split("\n")

def convertGithubUrl(origin_url):
    return origin_url + ".git"

if __name__ == '__main__':
    main()