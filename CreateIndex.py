import os, json

projectFile= '.project'
README= 'README.md'
urlHome= 'https://ewwgene.github.io/'

def getProjectInfo(path):
    filePath = os.path.join(path, projectFile)
    with open(filePath) as f:
        return json.load(f)

def makeProjectFile(path, data):
    pathREADME= os.path.join(path, README)
    with open(pathREADME, 'w') as f:
        f.write(data)
        print('create ', pathREADME)
        f.close()
        # json.dump(data, f, indent=4)

def hardwareMaterial(data):
    datan=''
    for h in data:
        hn= '`'+h+'`'+' '
        datan=datan+hn
    return datan

def softwareMaterial(data):
    datan=''
    for h in data:
        hn= '_`'+h+'`_'+' '
        datan=datan+hn
    return datan

def imgCreateHTML(urlImg, imgHeight):
    # print(imgPath)
    # fullUrlHome=normPath(os.path.join(urlHome, os.path.dirname(imgPath)))
    # print(fullUrlHome)
    imgHTML = '<a href="' + urlImg + '"><img src="/' + urlImg + '" height="' + imgHeight + '"></a> '
    return imgHTML

def imgTextCreateProject(imgPath, imgHeight):
    # print(os.path.basename(imgPath)[4])
    hH, ext= os.path.splitext(os.path.basename(imgPath))
    if len(hH)>=6:
        imgHeight = hH[-3:]

    # if hhH == hhhH:
    #     print(os.path.basename(imgPath)[4])
    #     imgHeight=os.path.basename(imgPath)[5:7]
    #     print(imgHeight)

    fullUrlHome=normPath(os.path.join(urlHome, imgPath))
    # print(fullUrlHome)
    imgTextInsert = '<a href="' + fullUrlHome + '"><img src="/' + imgPath + '" height="' + imgHeight + '"></a> '
    return imgTextInsert

def normPath(path):
    nPath = path.replace('\\', '/')
    return nPath

def imgMain(projectFolder, urlProject, project):
    imgTextInsertAll=''
    imgLittle = []
    for file in os.listdir(projectFolder):
        if os.path.isfile(os.path.join(projectFolder, file)):
            name, ext= os.path.splitext(file)
            if ext=='.jpg':
                if name.startswith('0') or name.startswith('10'):
                    urlImg=os.path.join(urlProject, file)
                    imgHeight=''
                    # print(name)
                    if name=='000':
                        imgHeight = '200'
                        imgHTML = imgCreateHTML(urlImg, imgHeight)
                    else:
                        if name!='100':
                            imgLittle.append(urlImg)
    for img in imgLittle:
        imgHeight = '100'
        imgTextInsertAll=imgTextInsertAll+imgCreateHTML(img, imgHeight)

    imgTextInsertAll=normPath(imgTextInsertAll)

    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProject(path, project, nu):
    imgTextInsertAll=''
    imgNumInsertAll = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext= os.path.splitext(file)
            if ext=='.jpg':
                if name.startswith(nu):
                    # print(file)
                    imgPath=os.path.join('projects', project, file)
                    imgNumInsertAll.append(imgPath)
    for n in imgNumInsertAll:
        imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(n, '100')
    imgTextInsertAll=normPath(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProjectMaking(path, project, over):
    # print('making - ', project)
    imgTextInsertAll=''
    imgNumInsertAll = []
    imgIndex=[]
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext= os.path.splitext(file)
            if ext=='.jpg' or ext=='.gif':
                iInx=name[0]

                if not iInx in imgIndex:
                    imgIndex.append(iInx)
    # print(imgIndex)
    for i in imgIndex:
        for file in os.listdir(path):
            if os.path.isfile(os.path.join(path, file)):
                name, ext = os.path.splitext(file)
                if ext == '.jpg' or ext=='.gif':
                    if name.startswith(i):
                        imgPath = os.path.join('projects', project, over, file)
                        # print('projects', project, over, file)
                        # print(imgPath)
                        imgNumInsertAll.append(imgPath)
        for n in imgNumInsertAll:
            imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(n, '100')
        imgTextInsertAll = imgTextInsertAll + '<br>'
        imgNumInsertAll.clear()
    # print(imgNumInsertAll)
    # for e, n in enumerate(imgNumInsertAll):
    #     imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(n, '100')
    imgTextInsertAll=normPath(imgTextInsertAll)
    # print(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll


def imgTextProjectIntro(path, project):
    imgTextInsertAll = ''
    imgNumInsertAll = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext = os.path.splitext(file)
            if ext == '.jpg':
                if name.startswith('1') and name!='100':
                    # print(name)
                    imgPath = os.path.join('projects', project, file)
                    imgNumInsertAll.append(imgPath)
    for n in imgNumInsertAll:
        imgTextInsertAll=imgTextInsertAll+imgTextCreateProject(n, '100')

    imgTextInsertAll = normPath(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProjectIntro100(path, project):
    # imgTextInsertAll = ''
    # imgNumInsertAll = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext = os.path.splitext(file)
            if ext == '.jpg':
                if name=='100':
                    imgPath = os.path.join('projects', project, file)
                    imgPath=normPath(imgPath)
                    return imgPath
                    # imgNumInsertAll.append(imgPath)
                    # imgTextInsert = fullUrlHome + '"><img src="/' + imgPath + '" height="' + imgHeight + '"></a> '
    # for e, n in enumerate(imgNumInsertAll):
    #     if e < 5:
    #         imgTextInsertAll=imgTextInsertAll+imgTextCreateProject(n, '150')
    #
    # imgTextInsertAll = normPath(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'




# print(os.path.join(os.path.dirname(__file__), 'projects'))
text=''
textProject=''
dateIndex=[]
mainFolder=os.path.dirname(os.path.dirname(__file__))
for project in os.listdir(mainFolder):
    projectFolder=os.path.join(mainFolder, project)
    if os.path.exists(os.path.join(projectFolder, projectFile)):
        info= getProjectInfo(projectFolder)
        dateIndex.append(info['date'][1])

dateIndex.sort()
dateIndex.reverse()
for dI in dateIndex:
    for project in os.listdir(mainFolder):
        projectFolder=os.path.join(mainFolder, project)
        if os.path.exists(os.path.join(projectFolder, projectFile)):
            info= getProjectInfo(projectFolder)
            if info['date'][1] == dI:
                urlProject=normPath(os.path.join(urlHome, project))
                ################################################################################################################
                textMain = '''
### [%s.](%s)
_%s-%s._
%s... [[more...]](%s)
|
%s
/
%s

%s
''' % (
                project, urlProject, info['date'][0], info['date'][1], info['overview'][0:199], urlProject, hardwareMaterial(info['hardware']),
                softwareMaterial(info['software']), imgMain(projectFolder, urlProject, project))
                ################################################################################################################

#                 textProject = '''
# ## %s. _%s-%s._
# ![%s](/%s)%s
# <br>
# **Overview**
# %s
# <br><br>
# %s
# **Making**
# %s
# |
# %s
# /
# %s
# <br>
# %s
# <br>
# %s
# ''' % (
#                 project, info['date'][0], info['date'][1], project, imgTextProjectIntro100(pathProject, project), imgTextProjectIntro(pathProject, project), info['overview'], imgTextProjectMaking(os.path.join(pathProject, 'Making'), project, 'Making'), info['making'], hardwareMaterial(info['hardware']),
#                 softwareMaterial(info['software']), imgTextProject(pathProject, project, '3'), imgTextProject(pathProject, project, '4'))
#                 ################################################################################################################
#                 # print(text)
#                 makeProjectFile(pathProject, textProject)
                text=text+textMain
makeProjectFile(os.path.join(os.path.dirname(__file__)), text)




