import os, json, random

projectFile= '.project'
README= 'README.md'
Name= 'ewwgene.github.io'
urlHome= 'https://ewwgene.github.io/'
smallHeight= '66'
about= '### [ABOUT/](https://ewwgene.github.io/)<br> '
mailTo= '### [MAIL_TO:](mailto:r0cam@me.com)<br> '
preFoot= '\n '
allImage=[]
allImageText=''

header= '## [_DESIGN_/](https://ewwgene.github.io/DESIGN)<br>[_ART_/](https://ewwgene.github.io/ART)<br>[_PROGRAMMING_/](https://ewwgene.github.io/PROGRAMMING)\n'
headerDESIGN= '# [' + Name + ' /](' + urlHome + ') [_DESIGN_ /](' + os.path.join(urlHome,'DESIGN') + ')'
headerART= '# [' + Name + ' /](' + urlHome + ') [_ART_ /](' + os.path.join(urlHome,'ART') + ')'
headerPROGRAMMING= '# [' + Name + ' /](' + urlHome + ') [_PROGRAMMING_ /](' + os.path.join(urlHome,'PROGRAMMING') + ')'

footer= about + mailTo

def getProjectInfo(path):
    filePath = os.path.join(path, projectFile)
    with open(filePath) as f:
        return json.load(f)

def makeProjectFile(path, data):
    pathREADME= os.path.join(path, README)
    with open(pathREADME, 'w', encoding='utf-8') as f:
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
            if ext=='.jpg':
                urlImg=os.path.join(urlProject, file)
                imgHeight=''
                # print(name)
                if name=='000':
                    imgHeight = '200'
                    imgTextInsertAll = imgCreateHTML(urlImg, imgHeight, project)
                else:
                    if name!='100':
                        imgLittle.append(urlImg)
    volRand= random.randint(0, 3)
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
            if ext=='.jpg':
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
                if name.startswith('1') and name!='100':
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
            if ext == '.jpg':
                if name=='100':
                    imgPath = os.path.join(project, file)
                    imgPath = file
                    imgPath=normPath(imgPath)
                    urlImg = os.path.join(urlProject, file)
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
    return medium.split()[0]

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

# print(os.path.join(os.path.dirname(__file__), 'projects'))
text=''
textProject=''
dateIndex=[]
textDESIGN=''
textART=''
textPROGRAMMING=''
mainFolder=os.path.dirname(os.path.dirname(__file__))
for project in os.listdir(mainFolder):
    projectFolder=os.path.join(mainFolder, project)
    if os.path.exists(os.path.join(projectFolder, projectFile)):
        info= getProjectInfo(projectFolder)
        dateIndex.append(info['date'][1])
        # if info['medium'][0].startswith('DESIGN'):
        #     dateIndexDESIGN.append(info['date'][1])

dateIndex.sort()
dateIndex.reverse()
# dateIndexDESIGN.sort()
# dateIndexDESIGN.reverse()
# for dID in dateIndexDESIGN:
#     for project in os.listdir(mainFolder):
#         projectFolder=os.path.join(mainFolder, project)
#         if os.path.exists(os.path.join(projectFolder, projectFile)):
#             info= getProjectInfo(projectFolder)
#             if info['date'][1] == dI:
#                 urlProject=normPath(os.path.join(urlHome, project))
#                 ################################################################################################################
#                 textMainDESIGN = '''
# ### [%s.](%s)
# _%s-%s._
# %s... [[more...]](%s/#text) <br>
# %s
#
# %s
#
# ''' % (
#                 project, urlProject, info['date'][0], info['date'][1], info['overview'][0:99], urlProject, mediumBubbles(info['medium']), imgMain2(projectFolder, urlProject, project))
#                 ################################################################################################################
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
%s... [[more...]](%s/#text) <br>
%s

%s

''' % (
                project, urlProject, info['date'][0], info['date'][1], info['overview'][0:99], urlProject, mediumBubbles(info['medium']), imgMain2(projectFolder, urlProject, project))
                ################################################################################################################


                textProject = '''
# [%s /](%s) [_%s_ /](%s) %s

[![%s](/%s)](%s)%s<a id="text">&#160;</a>

%s

%s

### Making — _%s-%s._
%s 

%s %s

%s

%s

%s
''' % (
                Name, urlHome, mediumMain(info['medium'][0]), os.path.join(urlHome, mediumMain(info['medium'][0])), project,
                project, imgProjectIntro100(projectFolder, project), normPath(os.path.join(urlProject, 'Carousel')), imgProjectIntro(projectFolder, urlProject, project),
                materialBubbles(info['material']),
                info['overview'],
                info['date'][0], info['date'][1],
                imgTextProjectMaking2(os.path.join(projectFolder, 'Making'), urlProject, 'Making', project),
                softwareBubbles(info['software']), hardwareBubbles(info['hardware']),
                info['making'],
                imgTextProject(projectFolder, urlProject, '3', project),
                mediumBubbles(info['medium']))
                ################################################################################################################
                # print(textProject)
                # print(text)
                textProject = textProject + footer

                makeProjectFile(projectFolder, textProject)

                for i in allImage:
                    i=normPath(i)


                    nnN, extN= os.path.splitext(os.path.basename(i))
                    if os.path.dirname(i).endswith('Making'):
                        nnM=nnN + 'm'
                    else:
                        nnM = nnN
                    iText='<a id="' + nnM + '"></a> !['+ os.path.basename(i) + '](' + i + ')\n'
                    allImageText= allImageText + iText




                textImage = '''
# [%s /](%s) [_%s_ /](%s) [%s /](%s)

%s
''' % (
                Name, urlHome, mediumMain(info['medium'][0]), os.path.join(urlHome, mediumMain(info['medium'][0])), project, urlProject, allImageText)
                # textImage = textImage
                # textImage=textImage + about + preFoot + footer + footer + footer
                makeProjectFile(os.path.join(projectFolder, 'Carousel'), textImage)
                allImage.clear()
                allImageText=''


                text=text+textMain
                if info['medium'][0].startswith('DESIGN'):
                    textDESIGN=textDESIGN+textMain
                if info['medium'][0].startswith('ART'):
                    textART=textART+textMain
                if info['medium'][0].startswith('PROGRAMMING'):
                    textPROGRAMMING=textPROGRAMMING+textMain


Name, urlHome, mediumMain(info['medium'][0]), os.path.join(urlHome, mediumMain(info['medium'][0]))
'# [Name /](urlHome) [_%s_ /](%s) [%s /](%s)'
text = header + text + footer
textDESIGN = headerDESIGN + textDESIGN + footer
textART = headerART + textART + footer
textPROGRAMMING = headerPROGRAMMING + textPROGRAMMING + footer

makeProjectFile(os.path.join(os.path.dirname(__file__)), text)
makeProjectFile(os.path.join(os.path.dirname(__file__), 'DESIGN'), textDESIGN)
makeProjectFile(os.path.join(os.path.dirname(__file__), 'ART'), textART)
makeProjectFile(os.path.join(os.path.dirname(__file__), 'PROGRAMMING'), textPROGRAMMING)



