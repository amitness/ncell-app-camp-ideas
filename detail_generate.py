from bs4 import BeautifulSoup
# import lxml
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

source = requests.get("http://ncellappcamp.com/ideas")
soup = BeautifulSoup(source.content, "lxml")
category=soup.find_all('div',{'class':'idea-name'})
problemlist=[]
idealist=[]
i=0
for item in category:
    idealist.append(str(item.text).replace('"','').replace(' ','').replace("/",''))
    src = item.find('a')
    link=src.get('href')
    source = requests.get("http://ncellappcamp.com"+link)
    soup=BeautifulSoup(source.content,'lxml')
    content = soup.find('div',{'class':'panel-pane pane-views-panes pane-idea-detail-page-panel-pane-idea-content'})
    teamcontent=str(content.text).replace("Team's idea in one sentence","\nIdea:\n")
    function_content=teamcontent.replace(" Main functions and elements of the application","Functions:\n")
    targeted_content=function_content.replace(" Targeted audience of the application","Targeted audience:\n")
    platform_content=targeted_content.replace(" Platforms in which application will be developed in","Platform:")
    submit_content=platform_content.replace(' Submitted on: ','Submitted on: ')
    problem_content=submit_content.replace(' Problem solved by the application ','Problem Solved:\n')
    benefit_content=problem_content.replace(' Main benefits of the application ','Main Benefits:\n')
    space_content=benefit_content.replace('\n\n\n\n  ','')
    problemlist.append(space_content)
    print "Completed:",i/7.27
    i+=1
    # if i==5:
        # break
print "Total", len(problemlist)
for i in range(727):
    with open(str(i+1)+'.'+idealist[i]+'.txt',"w") as newfile:
        newfile.write(idealist[i]+'\n'+problemlist[i])
