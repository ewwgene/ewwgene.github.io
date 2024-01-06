import os, json, random
from PIL import Image, ExifTags
projectFile= '.project2'
indexFile= 'index.html'
README= 'README.md'
Name= 'ewwgene.github.io'
urlHome= 'https://ewwgene.github.io/'
smallHeight= '66'
about= '### [ABOUT /](https://ewwgene.github.io/ABOUT)\n'
inst= '### [@ewwgene__](https://instagram.com/ewwgene__?igshid=YmMyMTA2M2Y=)\n'
mailTo= '### [MAIL_TO:](mailto:r0cam@me.com)\n'
preFoot= '\n '
allSoft=[]
allHard=[]
allImage=[]
imgFolders=[]
imgs = []

allImageText=''
# headerMain=  '# [' + Name + ' /](' + urlHome + ')\n'
headerMain=  '# ' + Name + ' /\n'
navigMain= '## [_DESIGN_ /](https://ewwgene.github.io/DESIGN)<br>[_ART_ /](https://ewwgene.github.io/ART)<br>[_PROGRAMMING_ /](https://ewwgene.github.io/PROGRAMMING)\n'
headerDESIGN= '# [' + Name + ' /](' + urlHome + ') _DESIGN_ '
headerART= '# [' + Name + ' /](' + urlHome + ') _ART_ '
headerPROGRAMMING= '# [' + Name + ' /](' + urlHome + ') _PROGRAMMING_ '

footer = '<br> \n\n' + about + inst + mailTo

def htmlData(path):
    imgFolders.clear()
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
<table width="292" cellpadding="7.5">
    <td align="left" valign="center">
        <big><big>%s</big></big>
    </td>
</table>
%s
</body>
</html>
''' % (htmlName(path), htmlTable(path))
        #
        # for folder in os.listdir(path):
        # pathFolder=os.path.join(path, folder)
        # if os.path.isdir(pathFolder):
        #     print('check2', pathFolder)
def htmlName(path):
    htmlTr(path)
    if not os.path.basename(path)==os.path.relpath(imgs[0], f).split('\\')[0].split('_')[1]:
        return os.path.basename(path)
    else:
        return ''
def htmlTable(path):
    return '''
<table>
    <tr >
%s
    </tr>
</table>
''' % (htmlTr(path))

def htmlTr(path):
    htmlTrecursive(path)
    htmlTrText = ''
    # print(imgFolders)
    for imgFolder in imgFolders:
        imgs.clear()
        htmlTrecursive2IMG(imgFolder)
        # print(imgFolder)
        if not len(imgs) == 0:
            htmlTrText=htmlTrText+htmlTd(imgs)
            # print(os.path.relpath(img, f).split('\\')[0])
            # print(imgs)
            # print(mainFolder)
    return htmlTrText
    # for f in imgFolders:
    #     for file in os.listdir(folder):

def htmlTrecursive(path):
    if 'IMG' in os.listdir(path):
        folderPath = os.path.join(path, 'IMG')
        imgFolders.append(folderPath)
    for folder in os.listdir(path):
        if os.path.isdir(os.path.join(path, folder)):
            htmlTrecursive(os.path.join(path, folder))

def htmlTrecursive2IMG(path):
    for ff in os.listdir(path):
        fpath= os.path.join(path, ff)
        if os.path.isfile(fpath):
            f, ext= os.path.splitext(os.path.basename(fpath))
            if ext== '.jpg' or ext== '.gif':
                if f.isdigit():
                    # print(f)
                    imgs.append(fpath)
        else:
            htmlTrecursive2IMG(fpath)

def htmlTd(paths):

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
    ''' % (os.path.relpath(paths[0], f).split('\\')[0].split('_')[1], makeInfoText(paths[0], f), htmlImg(paths))


def htmlImg(paths):
    htmlImgText = ''
    for path in paths:
        # print(path)
        htmlImgText = htmlImgText + '''
                <td valign="top"><img src="%s" height="606" border="1">
        <p>%s
                </td>
        ''' % (os.path.relpath(path, f), comment(path))
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

#         <td valign="top">
# 		    <table width="292" height="506" cellpadding="25">
# 		        <td align="center" valign="center">
#                     <h1>%s</h1>
#                 </td>
# 		    </table>
# 	    </td>
# 	    <td valign="top">
# 	        <img src="AutoCAD/IMG/_tempDM/Untitled-1.jpg" height="606">
# 1. Duis te feugifacilisi. Duis autem dolor in hendrerit in vulputate velit esse molestie consequat
#         </td>
# 	    <td valign="top">
# 	        <img src="AutoCAD/IMG/_tempDM/Untitled-2.jpg" height="606">
# 	    </td>
# 	    <td valign="top">
# 	        <img src="AutoCAD/IMG/_tempDM/Untitled-1.jpg" height="606">
# 1. Duis te feugifacilisi. Duis autem dolor in hendrerit in vulputate velit esse molestie consequat
#         </td>
# 	    <td valign="top">
# 	        <img src="AutoCAD/IMG/_tempDM/Untitled-2.jpg" height="606">
# 	    </td>
# ''' % ('AUTOCAD')
def makeInfoText(path, f):
    infoText=''
    if "info.txt" in os.listdir(os.path.join(f, os.path.relpath(path, f).split('\\')[0])):
        print("info.txt")
        pathInfo=os.path.join(os.path.join(f, os.path.relpath(path, f).split('\\')[0]),"info.txt")
        with open(pathInfo, 'r', encoding='utf-8-sig', errors='ignore') as f:
            infoText=f.read()
            f.close()
    return infoText

def makeIndexFile(path, data):
    pathIndexFile= os.path.join(path, indexFile)
    with open(pathIndexFile, 'w', encoding='utf-8-sig', errors='ignore') as f:
        f.write(data)
        # print('create ', pathREADME)
        f.close()
        # json.dump(data, f, indent=4)
def getProjectInfo(path):
    filePath = os.path.join(path, projectFile)
    with open(filePath) as f:
        return json.load(f)

def makeProjectFile(path, data):
    pathREADME= os.path.join(path, README)
    with open(pathREADME, 'w', encoding='utf-8-sig', errors='ignore') as f:
        f.write(data)
        # print('create ', pathREADME)
        f.close()
        # json.dump(data, f, indent=4)

def imgCreateHTML(urlImg, imgHeight, project, m1=None):
    # print(imgPath)
    # fullUrlHome=normPath(os.path.join(urlHome, os.path.dirname(imgPath)))
    # print(fullUrlHome)
    dee, fee= os.path.splitext(os.path.basename(urlImg))
    if m1:
        pref= '/#' + project.lower() + '--' + m1.replace(' ', '-').lower()
    else:
        pref = '/#' + dee

    imgHTML = '<a href="' + os.path.dirname(urlImg) + pref + '"><img src="' + urlImg + '" height="' + imgHeight + '"></a> '
    return imgHTML

def imgTextCreateProject(imgPath, imgHeight, project, over=None):
    # print(os.path.basename(imgPath)[4])
    hH, ext= os.path.splitext(os.path.basename(imgPath))
    if over:
        hM=hH+'m'
    else:
        hM = hH
    if len(hH)>=6:
        imgHeight = hH[-3:]
    if project == 'ABOUT':
        imgHeight = '33'


    # if hhH == hhhH:
    #     print(os.path.basename(imgPath)[4])
    #     imgHeight=os.path.basename(imgPath)[5:7]
    #     print(imgHeight)
    # ind=str(allImage.index(imgPath))

    fullUrlHome=normPath(os.path.join(urlHome, imgPath))
    fullUrlHome = normPath(imgPath)

    fullUrlHomeCarousel = normPath(os.path.join(urlHome, project, 'Carousel', '#' + hM))

    # print(fullUrlHome)
    imgTextInsert = '<a id="' + hM + '" href="' + fullUrlHomeCarousel + '"><img src="' + fullUrlHome + '" height="' + imgHeight + '"></a> '
    # print(imgTextInsert)
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

def imgMain2(projectFolder, urlProject, project):
    imgTextInsertAll=''
    imgLittle = []
    for file in os.listdir(projectFolder):
        if os.path.isfile(os.path.join(projectFolder, file)):
            name, ext= os.path.splitext(file)
            if ext=='.jpg' or ext=='.gif':
                urlImg=os.path.join(urlProject, file)
                imgHeight=''
                # print(name)
                if name=='000':
                    imgHeight = '200'
                    imgTextInsertAll = imgCreateHTML(urlImg, imgHeight, project)
                else:
                    if name!='100':
                        imgLittle.append(urlImg)

    volRand= random.randint(1, 3)
    # print(volRand)
    random.shuffle(imgLittle)
    # print(imgLittle)
    # print(len(imgLittle))
    for i in range(volRand):
    #     if i!=0:
    #     print('range', i)
        imgHeight = smallHeight
        imgTextInsertAll=imgTextInsertAll+imgCreateHTML(imgLittle[i], imgHeight, project)

    imgTextInsertAll=normPath(imgTextInsertAll)

    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProject(path, urlProject, nu, project):
    imgTextInsertAll=''
    imgNumInsertAll = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext= os.path.splitext(file)
            if ext=='.jpg' or ext=='.gif':
                if name.startswith(nu) or name.startswith('4'):
                    # print(file)
                    urlImg=os.path.join(urlProject, file)
                    imgNumInsertAll.append(urlImg)
    for nImg, img in enumerate(imgNumInsertAll):
        # print( nImg, ' of ', len(imgNumInsertAll))
        allImage.append(img)
        imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(img, smallHeight, project)
    imgTextInsertAll=normPath(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProjectMaking(path, urlProject, over, project):
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
            imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(img, smallHeight, project)
        imgTextInsertAll = imgTextInsertAll + '<br>'
        imgNumInsertAll.clear()
    # print(imgNumInsertAll)
    # for e, n in enumerate(imgNumInsertAll):
    #     imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(n, '100')
    imgTextInsertAll=normPath(imgTextInsertAll)
    # print(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgTextProjectMaking2(path, urlProject, over, project):
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
        allImage.append(img)
        imgTextInsertAll = imgTextInsertAll + imgTextCreateProject(img, smallHeight, project, over)
    imgTextInsertAll = imgTextInsertAll
    imgTextInsertAll=normPath(imgTextInsertAll)
    return imgTextInsertAll


def imgProjectIntro(projectFolder, urlProject, project):
    imgTextInsertAll = ''
    imgNumInsertAll = []

    for file in os.listdir(projectFolder):
        if os.path.isfile(os.path.join(projectFolder, file)):
            name, ext = os.path.splitext(file)
            if ext == '.jpg':
                if name.startswith('1') or name.startswith('2'):
                    if name!='100':
                        # print(name)
                        urlImg = os.path.join(urlProject, file)
                        imgNumInsertAll.append(urlImg)
    for nImg, img in enumerate(imgNumInsertAll):
        allImage.append(img)
        # if nImg==len(imgNumInsertAll)-1:
        #     imgTextInsertAll = imgTextInsertAll + '<a id="text"></a>' + imgTextCreateProject(img, smallHeight, project)
        # else:
        imgTextInsertAll=imgTextInsertAll+imgTextCreateProject(img, smallHeight, project)

    imgTextInsertAll = normPath(imgTextInsertAll)
    # imgTextInsertAll='<a href="https://www.google.com">' + imgTextInsertAll + '</a>'
    return imgTextInsertAll

def imgProjectIntro100(path, project):
    # imgTextInsertAll = ''
    # imgNumInsertAll = []
    for file in os.listdir(path):
        if os.path.isfile(os.path.join(path, file)):
            name, ext = os.path.splitext(file)
            if ext == '.jpg' or ext == '.gif':
                if name=='100':
                    imgPath = os.path.join(project, file)
                    imgPath = file
                    imgPath=normPath(imgPath)
                    urlProject=os.path.join(urlHome, project)
                    urlImg = os.path.join(urlProject, file)
                    # print(urlProject, project)
                    allImage.append(urlImg)

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
def textImageInsert(projectFolder):
    pass


def mediumMain(medium):
    return medium.split('_')[0]

def mediumBubbles(mediums):
    bubbles = ''
    for medium in mediums:
        mediumPath= os.path.join(urlHome, mediumMain(medium))
        # bubble = '[_`' + medium + '`_]' + '(' + mediumPath + ') '
        bubble = '_`' + medium + '`_ '
        bubbles = bubbles + bubble
    # datan= datan+ '<br>'
    return bubbles

def materialBubbles(materials):
    bubbles=''
    for material in materials:
        bubble= '_`' + material + '`_ '
        bubbles= bubbles + bubble
    return bubbles

def hardwareBubbles(hardwares):
    bubbles=''
    for hardware in hardwares:
        bubble = '_**`' + hardware + '`**_ '
        bubbles = bubbles + bubble
    return bubbles

def softwareBubbles(softwares):
    bubbles = ''
    for software in softwares:
        bubble = '_`' + software + '`_ '
        bubbles = bubbles + bubble
    return bubbles

def embedVideo(projectFolder):
    s=''
    embed= os.path.join(projectFolder, '.embed')
    if os.path.exists(embed):
        f = open(embed, 'r')
        s= f.read()
        f.close()
        # print (s)
    return s

def aboutPage():
    aboutFolder=os.path.join(os.path.dirname(os.path.dirname(__file__)), Name, 'ABOUT')
    aboutPath=os.path.join(urlHome, 'ABOUT')
    CVFile= os.path.join(aboutFolder, '.CV')
    PEFile = os.path.join(aboutFolder, '.PE')
    allImageText=''
    allImage.clear()
    if os.path.exists(CVFile):
        f = open(CVFile, 'r')
        CV= f.read()
        f.close()
        # print (CV)
    if os.path.exists(PEFile):
        f = open(PEFile, 'r')
        PE= f.read()
        f.close()
        # print (PE)

    aboutText = '''
# [%s /](%s) %s
    
%s

%s

%s

%s

%s%s

%s

%s

[![%s](%s/%s)](%s)

    ''' % (
        Name, urlHome, 'ABOUT',
        CV,
        imgProjectIntro(aboutFolder, aboutPath, 'ABOUT').replace('> <', '><'),
        PE,
        imgTextProject(aboutFolder, aboutPath, '3', 'ABOUT'),
        softwareBubbles(allSoft), hardwareBubbles(allHard),
        inst,
        mailTo,
        'ABOUT', aboutPath, imgProjectIntro100(aboutFolder, 'ABOUT'), normPath(os.path.join(aboutPath, 'Carousel'))
        )
    # print (aboutText)
    makeProjectFile(aboutFolder, aboutText)
    for i in allImage:
        i = normPath(i)
        nnN, extN = os.path.splitext(os.path.basename(i))
        nnM = nnN
        iText = '<a id="' + nnM + '"></a> ![' + os.path.basename(i) + '](' + i + ')\n'
        allImageText = allImageText + iText

    textCarousel = '''
# [%s /](%s) [%s /](%s)

%s
    ''' % (
        Name, urlHome, 'ABOUT', aboutPath,
        allImageText)

    makeProjectFile(os.path.join(aboutFolder, 'Carousel'), textCarousel)
    print(textCarousel)
    ################################################################################################################






# print(os.path.join(os.path.dirname(__file__), 'projects'))
mediumCAD=[]
mediumDESIGN=[]
text=''
textProject=''
dateIndex=[]
dateIndexContinues=[]
dateALL=[]
textDESIGN=''
textART=''
textPROGRAMMING=''
mainFolder=os.path.dirname(os.path.dirname(__file__))
# print(mainFolder)
projectFolders=[]
for project in os.listdir(mainFolder):
    projectFolder=os.path.join(mainFolder, project)
    if os.path.exists(os.path.join(projectFolder, projectFile)):
        ProjectInfo= getProjectInfo(projectFolder)
        # print(ProjectInfo)
        # if not 'CONTINUES' in info['date'][1]:
        #     dateIndex.append(info['date'][1])
        # else:
        #     dateIndexContinues.append(info['date'][1])
        if ProjectInfo['medium'][0].startswith('DESIGN'):
            mediumDESIGN.append(projectFolder)
        if ProjectInfo['medium'][0].startswith('ART'):
            mediumDESIGN.append(projectFolder)
        if ProjectInfo['medium'][0].startswith('PROGRAMMING'):
            mediumCAD.append(projectFolder)
        if ProjectInfo['medium'][0].startswith('CAD'):
            mediumCAD.append(projectFolder)
        projectFolders.append(projectFolder)



for f in projectFolders:
    makeIndexFile(f, htmlData(f))
    print('Make Index File in ', f)
    print(os.path.basename(f))
# dateIndex.sort()
# dateIndexContinues.sort()
# dateIndex.reverse()
# dateIndexContinues.reverse()
# dateALL=dateIndexContinues+dateIndex
# print(dateALL)
# dateIndexDESIGN.sort()
# dateIndexDESIGN.reverse()




#     for f in projectFolders:
#         projectFolder = os.path.join(mainFolder, project)
#         for project in os.listdir(mainFolder):
#             projectFolder=os.path.join(mainFolder, project)
#             if os.path.exists(os.path.join(projectFolder, projectFile)):
#                 info= getProjectInfo(projectFolder)
#                 if info['date'][1] == dI:
#                     urlProject=normPath(os.path.join(urlHome, project))
#                     ################################################################################################################
#                     textMainDESIGN = '''
# ### [%s.](%s)
# _%s-%s._
# %s... [[more...]](%s/#text) <br>
# %s
#
# %s
#
# ''' % (
#                 project, urlProject, info['date'][0], info['date'][1], info['overview'][0:99], urlProject, mediumBubbles(info['medium']), imgMain2(projectFolder, urlProject, project))
                ################################################################################################################
# for dI in dateALL:
#     for project in os.listdir(mainFolder):
#         projectFolder=os.path.join(mainFolder, project)
#         if os.path.exists(os.path.join(projectFolder, projectFile)):
#             info= getProjectInfo(projectFolder)
#             if info['date'][1] == dI:
#                 # print(info['date'][1])
#                 urlProject=normPath(os.path.join(urlHome, project))
#                 ################################################################################################################
#                 textMain = '''
# ### [%s.](%s)
# _%s-%s._
# %s... [[more...]](%s/#text) <br>
# %s
#
# %s
#
# ''' % (
#                 project, urlProject,
#                 info['date'][0], info['date'][1],
#                 info['overview'][0:144], urlProject,
#                 mediumBubbles(info['medium']),
#                 imgMain2(projectFolder, urlProject, project))
#                 ################################################################################################################
#
#
#                 textProject = '''
# # [%s /](%s) [_%s_ /](%s) %s
#
# [![%s](/%s)](%s)<br> %s<a id="text">&#160;</a>
#
# %s
#
# %s
#
# ### Making — _%s-%s._
# %s
#
# %s %s
#
# %s
#
# %s
#
# %s
# %s
# ''' % (
#                 Name, urlHome, mediumMain(info['medium'][0]), os.path.join(urlHome, mediumMain(info['medium'][0])), project,
#                 project, imgProjectIntro100(projectFolder, project), normPath(os.path.join(urlProject, 'Carousel')), imgProjectIntro(projectFolder, urlProject, project),
#                 materialBubbles(info['material']),
#                 info['overview'],
#                 info['date'][0], info['date'][1],
#                 imgTextProjectMaking2(os.path.join(projectFolder, 'Making'), urlProject, 'Making', project),
#                 softwareBubbles(info['software']), hardwareBubbles(info['hardware']),
#                 info['making'],
#                 imgTextProject(projectFolder, urlProject, '3', project),
#                 mediumBubbles(info['medium']),
#                 embedVideo(projectFolder))
#                 ################################################################################################################
#                 # print(textProject)
#                 for s in info['software']:
#                     if not s in allSoft:
#                         allSoft.append(s)
#                 for h in info['hardware']:
#                     if not h in allHard:
#                         allHard.append(h)
#                 # print(text)
#                 textProject = textProject + footer
#
#                 makeProjectFile(projectFolder, textProject)
#                 # print('Mk', projectFolder)
#
#                 for i in allImage:
#                     i=normPath(i)
#
#
#                     nnN, extN= os.path.splitext(os.path.basename(i))
#                     if os.path.dirname(i).endswith('Making'):
#                         nnM=nnN + 'm'
#                     else:
#                         nnM = nnN
#                     iText='<a id="' + nnM + '"></a> !['+ os.path.basename(i) + '](' + i + ')\n'
#                     allImageText= allImageText + iText
#
#
#
#
#                 textImage = '''
# # [%s /](%s) [_%s_ /](%s) [%s /](%s)
#
# %s
# ''' % (
#                 Name, urlHome, mediumMain(info['medium'][0]), os.path.join(urlHome, mediumMain(info['medium'][0])), project, urlProject,
#                 allImageText)
#
#                 makeProjectFile(os.path.join(projectFolder, 'Carousel'), textImage)
#                 # print('Mk', projectFolder)
#                 allImage.clear()
#                 allImageText=''
#
#
#                 text=text+textMain
#                 if info['medium'][0].startswith('DESIGN'):
#                     textDESIGN=textDESIGN+textMain
#                 if info['medium'][0].startswith('ART'):
#                     textART=textART+textMain
#                 if info['medium'][0].startswith('PROGRAMMING'):
#                     textPROGRAMMING=textPROGRAMMING+textMain
#
# aboutPage()
# Name, urlHome, mediumMain(info['medium'][0]), os.path.join(urlHome, mediumMain(info['medium'][0]))
# '# [Name /](urlHome) [_%s_ /](%s) [%s /](%s)'
# text = headerMain + navigMain + text + footer
# textDESIGN = headerDESIGN + textDESIGN + footer
# textART = headerART + textART + footer
# textPROGRAMMING = headerPROGRAMMING + textPROGRAMMING + footer
#
# makeProjectFile(os.path.join(os.path.dirname(__file__)), text)
# # print('Mk', os.path.join(os.path.dirname(__file__)))
# makeProjectFile(os.path.join(os.path.dirname(__file__), 'DESIGN'), textDESIGN)
# makeProjectFile(os.path.join(os.path.dirname(__file__), 'ART'), textART)
# makeProjectFile(os.path.join(os.path.dirname(__file__), 'PROGRAMMING'), textPROGRAMMING)



