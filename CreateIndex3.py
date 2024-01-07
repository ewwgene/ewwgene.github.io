import os, json, random
from PIL import Image, ExifTags

mainFolder=os.path.dirname(os.path.dirname(__file__))
fatherFolders= ['CAD', 'Programming']
introWWW= 'https://ewwgene.github.io/'
projectFile= '.project2'
indexFile= 'index.html'
projectFolders=[]
imgFolders=[]
imgs = []


def makeIndexFile(path, data):
    if os.path.basename(path) in fatherFolders:
        path = os.path.join(os.path.dirname(__file__), os.path.basename(path))
        if not os.path.exists(path):
            os.mkdir(path)
    pathIndexFile = os.path.join(path, indexFile)
    with open(pathIndexFile, 'w', encoding='utf-8-sig', errors='ignore') as file:
        file.write(data)
        print('Make ', pathIndexFile)
        file.close()
def htmlData(path):
    print('---->', path)
    projectName = os.path.basename(path)
    checkForTitle, htmlTable = makeHtmlTable(path, projectName)
    if os.path.basename(path) in fatherFolders:
        introWWW = '../'
    else:
        introWWW = ''
    if checkForTitle:
        htmlTitle = makeHtmlTitle(projectName)
    else:
        htmlTitle=''

    return '''
    <!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01//EN">
    <html>
    <head>
    <title>My first styled page</title>
    <style type="text/css">
    p { text-indent: 30px; 
    margin: 0px 0;
    padding: 5px;
    }
    body {}
    </style>
    </head>
    <body>
    %s
    %s
    </body>
    </html>
    ''' % (htmlTitle, htmlTable)

def makeHtmlTitle(projectName):
    print('makeHtmlTitle ', projectName)
    return '''
    <table width="292" cellpadding="7.5">
        <td align="left" valign="center">
            <big><big>%s</big></big>
        </td>
    </table>
    ''' % (projectName)

def makeHtmlTable(path, projectName):
    checkForTitle, htmlTr = makeHtmlTr(path, projectName)
    htmlTable= '''
    <table>
        <tr >
    %s
        </tr>
    </table>
    ''' % (htmlTr)
    return checkForTitle, htmlTable

def makeHtmlTr(path, projectName):
    htmlTr = ''
    checkForTitle = ''
    subProjectNames = []
    imgFolders.clear()
    findImgFolders(path)

    for imgFolder in imgFolders:
        imgs.clear()
        findImgs(imgFolder)
        subProjectName = splitName(os.path.basename(imgFolder.removesuffix('\\IMG')))
        subProjectNames.append(subProjectName)
        # print(subProjectName)

        if not len(imgs) == 0:
            htmlTd = makeHtmlTd(imgs, subProjectName, imgFolder)
            htmlTr = htmlTr + htmlTd

    if projectName in subProjectNames:
        checkForTitle = False
    else:
        checkForTitle = True

    return checkForTitle, htmlTr


def splitName(subProjectName):
    try:
        subProjectName=subProjectName.split('_')[1]
    except:
        pass
    return subProjectName
    # try:
    #     return os.path.relpath(path, f).split('\\')[0].split('_')[1]
    # except:
    #     return os.path.relpath(path, f)

def makeHtmlTd(imgs, subProjectNames, imgFolder):
    print('subProjectNames ', subProjectNames)
    return '''
                <td valign="top">
    		        <table width="292" height="400" cellpadding="20">
    		            <td align="center" valign="center">
                            <big><big><big>%s</big></big></big>
                            <br><br><br>
                            <big>%s</big>
    		        </table>
    	        </td>
        %s	        
        ''' % (subProjectNames, makeInfoText(imgFolder.removesuffix('\\IMG')), htmlImg(imgs))


def htmlImg(paths):
    htmlImgText = ''
    for father in fatherFolders:
        if father in folder:
            introWWW = '../'
        else:
            introWWW = ''
    for path in paths:
        # print(path)
        htmlImgText = htmlImgText + '''
                    <td valign="top"><img src="%s" height="606" border="1">
            <p>%s
                    </td>
            ''' % (os.path.normpath(os.path.join(introWWW, os.path.relpath(path, folder))), comment(path))
    return htmlImgText


def comment(path):
    img = Image.open(path)
    output = ''
    tags = ExifTags.TAGS
    x = 'кодирует в строку байтов'
    b = x.encode('utf-8')
    exif = img.getexif()
    # val_utf=[]
    for key, val in exif.items():
        if tags.get(key, key) == 'XPComment':
            output = str(val, 'UTF-16')[:-1]

    if not output:
        output = ''
    return output


def makeInfoText(path):
    infoText=''
    if "info.txt" in os.listdir(path):
        # print("info.txt")
        pathInfo=os.path.join(path,"info.txt")
        with open(pathInfo, 'r', encoding='utf-8-sig', errors='ignore') as f:
            infoText=f.read()
            f.close()
    return infoText

def findImgFolders(path):
    if 'IMG' in os.listdir(path):
        ImgFolderPath = os.path.join(path, 'IMG')
        imgFolders.append(ImgFolderPath)
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            findImgFolders(os.path.join(path, folder))

def findImgs(imgFolder):
    for f in os.listdir(imgFolder):
        fpath= os.path.join(imgFolder, f)
        if os.path.isfile(fpath):
            ff, ext= os.path.splitext(os.path.basename(fpath))
            if ext== '.jpg' or ext== '.gif':
                if ff.isdigit():
                    # print(f)
                    imgs.append(fpath)
        else:
            findImgs(fpath)





for project in os.listdir(mainFolder):
    projectFolder=os.path.join(mainFolder, project)
    if os.path.exists(os.path.join(projectFolder, projectFile)):
        projectFolders.append(projectFolder)

for folder in projectFolders:
    makeIndexFile(folder, htmlData(folder))

