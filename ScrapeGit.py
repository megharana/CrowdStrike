from bs4 import BeautifulSoup
import urllib.request as urllib2
from lxml import html
import subprocess, os
from ForkRepo import forking
from FileToPush import generate_file
import time
import shutil

#scraping the repository details
url = "https://s3-ap-southeast-1.amazonaws.com/he-public-data/crowdstriked6215ff.html"

content = urllib2.urlopen(url)
#using beautiful soup for picking web elements easily
soup = BeautifulSoup(content)

table_rows = soup.find_all("tr")
repo_list = []  # to maintain repoList
data_list = []  # to maintain each repo details and later append it in repoList
i = -1
for row in table_rows:
    table_datas = row.find_all("td")

    for data in table_datas:  #reading all td of table
        if (i == 2):
            #for grouping up individual row item(i.e one repo detail)
            repo_list.append(data_list)
            data_list = []
        data_list.append(data.text)
        i += 1

repo_list.append(data_list)

for repo in repo_list:
    repo_url = str(repo[1])
    repo_name = str(repo[0])
    repo_branch = str(repo[2])
    forking(str(repo_url))
    repo_to_operate = "https://bitbucket.org/megharana95/" + repo_name + "/src/master/"
    cmd = "git clone " + repo_to_operate  #cloning the forked repo from zeeshan
    p_clone = os.popen(cmd)
    time.sleep(10)
    current_path = os.getcwd()
    path = current_path + "/master/"
    os.chdir(path)  #change directory to master folder

    p_init = os.popen("git init")
    #connecting remotely
    p_add_remote = os.popen("git remote add " + repo_name + " " +
                            repo_to_operate)
    #file to push is generated with the content provided
    generate_file()

    p_new_branch = os.popen("git checkout -b " + repo_branch)
    print(os.popen("git status"))
    p_add_new_file = os.popen("git add fileToPush.js")
    p_commit_message = os.popen("git commit -m 'Added new File'")
    time.sleep(5)
    p_push = os.popen("git push --set-upstream " + repo_name)

    time.sleep(5)

    os.chdir(current_path)
    shutil.rmtree(
        "master")  #remove master folder to clone again the second repo
