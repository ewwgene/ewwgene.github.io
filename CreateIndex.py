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



# print(os.path.join(os.path.dirname(__file__), 'projects'))
for project in os.listdir(os.path.join(os.path.dirname(__file__), 'projects')):
    if os.path.exists(os.path.join(os.path.dirname(__file__), 'projects', project, projectFile)):
        info= getProjectInfo(os.path.join(os.path.dirname(__file__), 'projects', project))
        # print(info)
        # print(info['dimensions'])
        text = ''' ### %s.         
_%s._  
%s. _%s._ [(...)](https://www.google.com)  
/
%s
/
%s
''' % (info['name'], info['date'], info['comment'], info['dimensions'], hardwareMaterial(info['hardware']), softwareMaterial(info['software']))

        print(text)

        makeProjectFile(os.path.join(os.path.dirname(__file__), 'projects', project), text)
        # print(info['materials'][2])

#os.path.exists(os.path.join(os.path.dirname(__file__), 'projects',))
# print(os.listdir(os.path.join(os.path.dirname(__file__), 'projects')))
