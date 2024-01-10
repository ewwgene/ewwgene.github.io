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
imgCash = []
nameCash = []
height=606
heightA4=644
width=910
cellpadding=3


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


def htmlData(projectPath):
    print('---->', projectPath)


    return '''
    
    <html>
    <head>
    <title>My first styled page</title>
    <style type="text/css">
    p { text-indent: 0px; 
    margin: 10px 20;
    padding: 0px;
    }
    body {}
    </style>
    </head>
    <body>
    
    %s
    
    </body>
    </html>
    
    ''' % (htmlTable(projectPath))



def htmlTable(projectPath):
    return '''

    <table cellpadding="%s" cellspacing="0" height="%s">
        <tr >
    %s
        </tr>
    </table>
    
        ''' % (cellpadding, heightA4+2*cellpadding, htmlBlocks(projectPath))


def htmlBlocks(projectPath):
    htmlBlocks = ''
    imgFolders.clear()
    imgCash.clear()
    nameCash.clear()
    findImgFolders(projectPath)
    projectName = os.path.basename(projectPath)

    for imgFolder in imgFolders:
        subProjectName = splitName(os.path.basename(imgFolder.removesuffix('\\IMG')))
        htmlBlocks = htmlBlocks + htmlBlock(imgFolder, subProjectName, projectName)
    return htmlBlocks


def htmlBlock(imgFolder, subProjectName, projectName):
    htmlBlock = ''
    imgs.clear()
    findImgs(imgFolder)
    if not len(imgs) == 0:
        for n, img in enumerate(imgs):
            htmlBlock = htmlBlock + htmlA4(imgFolder, subProjectName, projectName, n, img)
    return htmlBlock

def htmlA4(imgFolder, subProjectName, projectName, n, img):
    if projectName == subProjectName:
        projectName = ''
    if n==0:
        A5_L = htmlA5_intro_L(imgFolder, subProjectName, projectName, n, img)
        A5_R = htmlA5_intro_R(imgFolder, subProjectName, projectName, n, img)
        heightHtmlA4 = height
        widthHtmlA4 = width
    else:
        if chekVert(img):
            if len(imgCash) == 0:
                imgCash.append(img)
                return ''
            else:
                imgCash.append(img)
                A5_L = htmlA5(imgFolder, subProjectName, projectName, n, imgCash[0], 'right', '50%', True)
                A5_R = htmlA5(imgFolder, subProjectName, projectName, n, img, 'left', '50%', True)
                heightHtmlA4 = '100%'
                widthHtmlA4 = width
                imgCash.clear()
        else:
            A5_L = htmlA5(imgFolder, subProjectName, projectName, n, img, 'center', '100%', False)
            A5_R = ''
            heightHtmlA4 = '100%'
            widthHtmlA4 = width


    return '''
                    <td valign="top">
                        <table cellpadding="0" cellspacing="0" height="%s" width="%s">
    	                    <tr>
                                %s
                                %s
    	                    </tr>        
                        </table>
                    </td>
    ''' % (heightHtmlA4, widthHtmlA4, A5_L, A5_R)

def chekVert(img):
    im = Image.open(img)
    iMwidth, iMheight = im.size
    if iMheight>iMwidth:
        return True
    else:
        return False


def htmlA5_intro_L(imgFolder, subProjectName, projectName, n, img):
    if not len(nameCash)==0:
        projectName=''
    nameCash.append(projectName)
    print('projectName', projectName, nameCash)
    return ''' 
                <td align="center" valign="top" height="100%%" width="100%%">
                    <table cellpadding="0" cellspacing="0" height="100%%" width="392">
                        <tr height="25%%">
                            <td align="left" valign="top">
                                <p><big><big>%s</big></big>
                            </td>
                        </tr>
                        <tr height="33%%">
                            <td align="center" valign="top">
                                <p><big><big><big>%s</big></big></big><br>
                                <p><big>%s</big>
                            </td>
                        </tr>
                        <tr>
                            <td align="center" valign="top">
                                <p>
                            </td>
                        </tr>
                    </table>
                </td> 
                ''' % (projectName, subProjectName, makeInfoText(imgFolder.removesuffix('\\IMG')))



def htmlA5_intro_R(imgFolder, subProjectName, projectName, n, img):
    return '''
    <td align="right" valign="top" height="%s">
    %s
    </td>
    ''' % (height, htmlImg(img, 'height="100%" border="1"'))


def htmlA5(imgFolder, subProjectName, projectName, n, img, orient, size, Vert):
    if Vert:
        AtrTd, AtrImg = check3x4(img)
    else:
        AtrTd, AtrImg = check3x2(img)
    return '''
    		                 <td align="center" height="100%%" width="%s">
			                    <table cellpadding="0" cellspacing="0" height="100%%" width="100%%">
				                    <tr>
    		         	            	<td align="%s" valign="top" %s>
						                    %s
					                    </td>
				                    </tr>
				                    <tr>
					                    <td align="left" valign="top" height="100%%">
						                    %s
					                    </td>
				                    </tr>
				                </table>
				             </td>
				                   
    ''' % (size, orient, AtrTd, htmlImg(img, AtrImg), comment(img))


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


def check3x4(img):
    im = Image.open(img)
    iMwidth, iMheight = im.size
    if iMwidth/iMheight>0.75:
        # print(os.path.basename(img), iMwidth, iMheight, iMwidth/iMheight,'width="' )
        AtrTd = 'width="' + str(width/2) + '"'
        AtrImg = 'width="100%" border="1"'
    else:
        # print(os.path.basename(img), iMwidth, iMheight, iMwidth/iMheight,'height="' )
        AtrTd = 'height="' + str(height) + '"'
        AtrImg = 'height="100%" border="1"'
    return AtrTd, AtrImg

def check3x2(img):
    im = Image.open(img)
    iMwidth, iMheight = im.size
    if iMwidth/iMheight>1.5:
        AtrTd = 'width="' + str(width) + '"'
        AtrImg = 'width="100%" border="1"'
    else:
        AtrTd = 'height="' + str(height) + '"'
        AtrImg = 'height="100%" border="1"'
    return AtrTd, AtrImg


def htmlImg(img, atr):
    return '''
    <img src="%s" %s>
    ''' % (os.path.normpath(os.path.join(introWWW, os.path.relpath(img, folder))), atr)


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


def splitName(subProjectName):
    try:
        subProjectName=subProjectName.split('_')[1]
    except:
        pass
    return subProjectName







###########################################################################################
###########################################################################################
###########################################################################################

for project in os.listdir(mainFolder):
    projectFolder=os.path.join(mainFolder, project)
    if os.path.exists(os.path.join(projectFolder, projectFile)):
        projectFolders.append(projectFolder)

for folder in projectFolders:
    if os.path.basename(folder) in fatherFolders:
        introWWW='../'
    else:
        introWWW = ''
    makeIndexFile(folder, htmlData(folder))

