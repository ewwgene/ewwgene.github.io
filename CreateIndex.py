import os, json

projectFile= '.project'
bodyFile= 'README.md'
urlHome= 'https://ewwgene.github.io/'

def getProjectInfo(path):
    filePath = os.path.join(path, projectFile)
    with open(filePath) as f:
        return json.load(f)

def makeProjectFile(path, data):
    fileMakePath= os.path.join(path, bodyFile)
    with open(fileMakePath, 'w') as f:
        f.write(data)
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

def imgTextCreate(imgPath, imgHeight):
    # print(imgPath)
    fullUrlHome=normPath(os.path.join(urlHome, os.path.dirname(imgPath)))
    # print(fullUrlHome)
    imgTextInsert = '<a href="' + fullUrlHome + '"><img src="/' + imgPath + '" height="' + imgHeight + '"></a> '
    return imgTextInsert

def imgTextCreateProject(imgPath, imgHeight):
    # print(imgPath)
    fullUrlHome=normPath(os.path.join(urlHome, imgPath))
    # print(fullUrlHome)
    imgTextInsert = '<a href="' + fullUrlHome + '"><img src="/' + imgPath + '" height="' + imgHeight + '"></a> '
    return imgTextInsert

def normPath(path):
    nPath = path.replace('\\', '/')
    return nPath

def imgText(pathProject, project):
    imgTextInsertAll=''
    imgNumInsertAll = []
    for file in os.listdir(pathProject):
        if os.path.isfile(os.path.join(pathProject, file)):
            name, ext= os.path.splitext(file)
            if ext=='.jpg':
                if name.startswith('0') or name.startswith('10'):
                    imgPath=os.path.join('projects', project, file)
                    imgHeight=''
                    # print(name)
                    if name=='000':
                        imgHeight = '200'
                        imgTextInsertAll = imgTextCreate(imgPath, imgHeight)
                    else:
                        if name!='100':
                            imgNumInsertAll.append(imgPath)
    for n in imgNumInsertAll:
        imgHeight = '100'
        imgTextInsertAll=imgTextInsertAll+imgTextCreate(n, imgHeight)

    imgTextInsertAll=normPath(imgTextInsertAll)

    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProject(path, project):
    imgTextInsertAll=''
    imgNumInsertAll = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext= os.path.splitext(file)
            if ext=='.jpg':
                if name.startswith('3'):
                    print(file)
                    imgPath=os.path.join('projects', project, file)
                    imgNumInsertAll.append(imgPath)
    for n in imgNumInsertAll:
        imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(n, '100')
    imgTextInsertAll=normPath(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProjectMaking(path, project, over):
    imgTextInsertAll=''
    imgNumInsertAll = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext= os.path.splitext(file)

            if ext=='.jpg':

                imgPath=os.path.join('projects', project, over, file)
                imgNumInsertAll.append(imgPath)
    for e, n in enumerate(imgNumInsertAll):
        imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(n, '100')
    imgTextInsertAll=normPath(imgTextInsertAll)
    print(imgTextInsertAll)
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
for project in os.listdir(os.path.join(os.path.dirname(__file__), 'projects')):
    pathProject=os.path.join(os.path.dirname(__file__), 'projects', project)
    if os.path.exists(os.path.join(pathProject, projectFile)):
        info= getProjectInfo(pathProject)
        fullUrlHome=normPath(os.path.join(urlHome, 'projects', project))
        ################################################################################################################
        textT = '''
### [%s.](%s) 
_%s._  
%s... [[more...]](%s)  
/
%s
/
%s

%s
''' % (
        project, fullUrlHome, info['date'], info['overview'][0:199], fullUrlHome, hardwareMaterial(info['hardware']),
        softwareMaterial(info['software']), imgText(pathProject, project))
        ################################################################################################################

        textProject = '''
## %s. _%s._  
![%s](/%s)%s  
**Overview**  
%s  
<br>
%s  
**Making**  
%s  
/
%s  
/
%s  
<br>
%s
''' % (
        project, info['date'], project, imgTextProjectIntro100(pathProject, project), imgTextProjectIntro(pathProject, project), info['overview'], imgTextProjectMaking(os.path.join(pathProject, 'Making'), project, 'Making'), info['making'], hardwareMaterial(info['hardware']),
        softwareMaterial(info['software']), imgTextProject(pathProject, project))
        ################################################################################################################
        # print(text)
        makeProjectFile(pathProject, textProject)
        text=text+textT
# print(text)
makeProjectFile(os.path.join(os.path.dirname(__file__)), text)
        # print(info['materials'][2])

#os.path.exists(os.path.join(os.path.dirname(__file__), 'projects',))
# print(os.listdir(os.path.join(os.path.dirname(__file__), 'projects')))


