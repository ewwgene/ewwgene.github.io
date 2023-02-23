import os, json

projectFile= '.project'
README= 'README.md'
Name= 'ewwgene.github.io'
urlHome= 'https://ewwgene.github.io/'
smallHeight= '66'

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
    imgHTML = '<a href="' + os.path.dirname(urlImg) + '"><img src="' + urlImg + '" height="' + imgHeight + '"></a> '
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
    fullUrlHome = normPath(imgPath)
    # print(fullUrlHome)
    imgTextInsert = '<a href="' + fullUrlHome + '"><img src="' + fullUrlHome + '" height="' + imgHeight + '"></a> '
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
                        imgTextInsertAll = imgCreateHTML(urlImg, imgHeight)
                    else:
                        if name!='100':
                            imgLittle.append(urlImg)
    for img in imgLittle:
        imgHeight = smallHeight
        imgTextInsertAll=imgTextInsertAll+imgCreateHTML(img, imgHeight)

    imgTextInsertAll=normPath(imgTextInsertAll)

    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProject(path, urlProject, nu):
    imgTextInsertAll=''
    imgNumInsertAll = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext= os.path.splitext(file)
            if ext=='.jpg':
                if name.startswith(nu):
                    # print(file)
                    urlImg=os.path.join(urlProject, file)
                    imgNumInsertAll.append(urlImg)
    for img in imgNumInsertAll:
        imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(img, smallHeight)
    imgTextInsertAll=normPath(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProjectMaking(path, urlProject, over):
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
                        urlImg = os.path.join(urlProject, over, file)
                        # print('projects', project, over, file)
                        # print(imgPath)
                        imgNumInsertAll.append(urlImg)
        for img in imgNumInsertAll:
            imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(img, smallHeight)
        imgTextInsertAll = imgTextInsertAll + '<br>'
        imgNumInsertAll.clear()
    # print(imgNumInsertAll)
    # for e, n in enumerate(imgNumInsertAll):
    #     imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(n, '100')
    imgTextInsertAll=normPath(imgTextInsertAll)
    # print(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProjectMaking2(path, urlProject, over):
    # print('making - ', project)
    imgTextInsertAll=''
    imgNumInsertAll = []
    imgIndex=[]
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext= os.path.splitext(file)
            if ext=='.jpg' or ext=='.gif':
                urlImg = os.path.join(urlProject, over, file)
                # print('projects', project, over, file)
                # print(imgPath)
                imgNumInsertAll.append(urlImg)

    for img in imgNumInsertAll:
        imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(img, smallHeight)

    imgTextInsertAll=normPath(imgTextInsertAll)
    return imgTextInsertAll


def imgProjectIntro(projectFolder, urlProject):
    imgTextInsertAll = ''
    imgNumInsertAll = []
    for file in os.listdir(projectFolder):
        if os.path.isfile(os.path.join(projectFolder, file)):
            name, ext = os.path.splitext(file)
            if ext == '.jpg':
                if name.startswith('1') and name!='100':
                    # print(name)
                    urlImg = os.path.join(urlProject, file)
                    imgNumInsertAll.append(urlImg)
    for img in imgNumInsertAll:
        imgTextInsertAll=imgTextInsertAll+imgTextCreateProject(img, smallHeight)

    imgTextInsertAll = normPath(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgProjectIntro100(path, project):
    # imgTextInsertAll = ''
    # imgNumInsertAll = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext = os.path.splitext(file)
            if ext == '.jpg':
                if name=='100':
                    imgPath = os.path.join(project, file)
                    imgPath = file
                    imgPath=normPath(imgPath)
                    # print(imgPath)
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

                textProject = '''
# [%s](%s)
## %s. _%s-%s._
![%s](/%s)%s
<br>
**Overview**
%s
<br><br>
%s
**Making**
%s
|
%s
/
%s
<br>

%s
<br>
%s
''' % (
                Name, urlHome, project, info['date'][0], info['date'][1], project, imgProjectIntro100(projectFolder, project), imgProjectIntro(projectFolder, urlProject), info['overview'], imgTextProjectMaking2(os.path.join(projectFolder, 'Making'), urlProject, 'Making'), info['making'], hardwareMaterial(info['hardware']),
                softwareMaterial(info['software']), imgTextProject(projectFolder, urlProject, '3'), imgTextProject(projectFolder, urlProject, '4'))
                ################################################################################################################
                # print(text)
                makeProjectFile(projectFolder, textProject)

                text=text+textMain
makeProjectFile(os.path.join(os.path.dirname(__file__)), text)




