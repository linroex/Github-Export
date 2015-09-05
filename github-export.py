import sys, os
from git.repo.base import Repo

path = os.path.dirname(os.path.realpath(__file__))

def main():
    if sys.argv[1] == 'export':
        cloneAll()

def cloneAll():
    urls = getAllGithubUrl()

    for url in urls:
        info = getRepoInfo(url)
        repo = Repo.clone_from(info['url'], path + "/repo_temp/" + info['name'])
        print(repo)

def getAllGithubUrl():
    with open("url.txt") as f:
        return f.read().split("\n")

def getRepoInfo(origin_url):
    return {
        'url': origin_url + ".git",
        'name': origin_url.split("/")[-1]
    }

if __name__ == '__main__':
    main()