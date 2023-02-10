import os, json

projectFile= '.project'
bodyFile= 'bodyFile.md'

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

def imgText(pathProject, project):
    imgTextInsertAll=''
    for file in os.listdir(pathProject):
        if os.path.isfile(os.path.join(pathProject, file)):
            name, ext= os.path.splitext(os.path.join(pathProject, file))
            if ext=='.jpg':
                imgPath=os.path.join('projects', project, file)
                imgHeight='200'
                imgAlign = 'top'
                imgTextInsert='<img src="' + imgPath + '" height="'+ imgHeight +'" align="' + imgAlign + '"> '
                imgTextInsertAll=imgTextInsertAll+imgTextInsert
                imgTextInsertAll=imgTextInsertAll.replace('\\', '/')
    return imgTextInsertAll




# print(os.path.join(os.path.dirname(__file__), 'projects'))
for project in os.listdir(os.path.join(os.path.dirname(__file__), 'projects')):
    pathProject=os.path.join(os.path.dirname(__file__), 'projects', project)
    if os.path.exists(os.path.join(pathProject, projectFile)):
        info= getProjectInfo(pathProject)
        # print(project)
        # print(info['dimensions'])
        text = ''' ### %s.         
_%s._  
%s. _%s._ [(...)](https://www.google.com)  
/
%s
/
%s

%s
''' % (project, info['date'], info['comment'], info['dimensions'], hardwareMaterial(info['hardware']), softwareMaterial(info['software']), imgText(pathProject, project))

        # imgText(pathProject, project)
        print(text)
        makeProjectFile(os.path.join(os.path.dirname(__file__), 'projects', project), text)
        # print(info['materials'][2])

#os.path.exists(os.path.join(os.path.dirname(__file__), 'projects',))
# print(os.listdir(os.path.join(os.path.dirname(__file__), 'projects')))
