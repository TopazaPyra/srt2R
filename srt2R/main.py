#!/usr/bin/env python
# -*- coding: utf-8 -*-

import copy, re, ntpath, sys, linecache,  os,  codecs

from collections import OrderedDict
from PyQt4 import QtGui, QtCore
from mainwindow import Ui_MainWindow

class Srt2RApplication(QtGui.QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super (Srt2RApplication, self).__init__(parent)
        self.setupUi(self)
        self.connectActions()
    
    
    def connectActions(self):
        self.srtFilesFolderButton.clicked.connect(self.openSrtFiles)
        self.folderButton.clicked.connect(self.openFolder)
        self.convertButton.clicked.connect(self.convert)
    

    def openSrtFiles(self):
        srtFilesFolder = QtGui.QFileDialog.getExistingDirectory(self,  u"Répertoire",  QtCore.QDir.homePath())
        
        if srtFilesFolder:
            self.srtFilesFolderEdit.setText(srtFilesFolder)
    
    
    def openFolder(self):
        folder = QtGui.QFileDialog.getExistingDirectory(self,  u"Répertoire",  QtCore.QDir.homePath())
        
        if folder:
            self.folderEdit.setText(folder)
    
    
    def convert(self):
        srtFilesFolder = str(unicode(self.srtFilesFolderEdit.text()).encode("utf-8"))
        folder = str(unicode(self.folderEdit.text()).encode("utf-8"))
    
    
        def getConfig(srtFilesFolder):
            
            try:
                # Retrieve title variable names from config file
                
                f = codecs.open(srtFilesFolder + '//config',  'r',  'utf-8')
                config = f.read()
                
                titleFields = config.split('\t')
                
                return titleFields
                
            except IOError,  configError:
                popupMsg(u'Erreur lors de la lecture du fichier de configuration.')
        
        
        def listSrtFiles(srtFilesFolder):
            
            try:
                srtFiles = []
            
                for fileInFolder in os.listdir(srtFilesFolder):
                        if fileInFolder.endswith('.srt'):
                            srtFiles.append(str(srtFilesFolder + '//' + fileInFolder))
                            
                if (srtFiles):
                    return srtFiles
                
                else:
                    popupMsg(u"Erreur : il ne semble pas y avoir de fichier srt dans ce répertoire.")
            
            except OSError,  srtFolderError:
                popupMsg(u'Erreur lors de la récupération des fichiers srt.\nLe chemin d\'accès est peut-être invalide.')
     
     
        def parser(srtFile, config):
            
            parsedFile = {}
            
            parsedFile['fileName'] = unicode(ntpath.basename(srtFile), sys.stdin.encoding)
            
            content = file(srtFile).read()
            content = content.replace('\n',  ' ')
            
            parsedFile['lines'] = []
            titleData = []
            
            # Retrieve variable values from file title
            
            regName = '(.*?)(__|.srt)'
            titleVariables = re.findall(regName, parsedFile['fileName'])
            
            for variable in titleVariables:
                titleData.append(variable[0])
                
            if (len(titleData) == len(config)):
            
                # Retrieve metadata from first sequence
                
                firstSequence = linecache.getline(srtFile,  3)
                metadata = metaSplit(firstSequence)
                
                # First split based on the sequence number and sequence time
                
                reg = '([0-9]{1,4}\s(?:[0-9]{2}:){2}[0-9]{2},[0-9]{3} --> (?:[0-9]{2}:){2}[0-9]{2},[0-9]{3})'
                sections = re.split(reg,  content)
                del sections[0] # remove empty first line
                
                # Second split for storing elements in a double dimension array
                
                for section in sections:
                    reg2 = '[0-9]{1,4}\s((?:[0-9]{2}:){2}[0-9]{2},[0-9]{3}) --> ((?:[0-9]{2}:){2}[0-9]{2},[0-9]{3})'
                    matches = re.search(reg2,  section)
                    if (matches) :
                        debut = timeConverter(matches.group(1))
                        fin = timeConverter(matches.group(2))
                        
                        infoSequence = [(u'début', str(debut)), (u'fin', str(fin))]
                        
                        duration = fin - debut
                        infoSequence.append((u'durée', str(duration)))
                        
                        infoSequence.append((u'vidéo', parsedFile['fileName']))
                        
                        for meta in metadata:
                            infoSequence.append((meta, metadata[meta]))

                        i = 0

                        for Data in titleData :
                            infoSequence.append((config[i], Data))
                            i = i + 1
                    else :
                        tags = tagsSplit(section)
                        for tag in tags:
                            seq = copy.copy(infoSequence)
                            seq.insert(0,('tag', tag))
                            parsedFile['lines'].append(OrderedDict(seq))
                
                # Retrieve headers form first line
                
                headers = []
                
                for element in parsedFile['lines'][0]:
                    headers.append(element.strip())

                parsedFile['headers'] = headers
                
                return parsedFile
            
            else:
                popupMsg(u'Le nombre de variables contenues dans le titre de ' + parsedFile['fileName'] +' ne correspond pas avec le fichier de configuration.\nLes fichiers R n\'ont pas pu être créés pour cet élément.')


        def createCsv(fileName, folder, headersList, lines):

            csvFile = codecs.open(folder+'//'+ fileName + '.csv',  'w',  'utf-8')
            
            headers = ''
            
            for element in headersList:
                headers = headers + '\"' + element + '\",'
            
            csvFile.write(headers[:-1] + '\n')
            
            for line in lines:
                output = ''
                
                for element in line:
                    output = output + '\"' + line[element] + '\",'
                
                output = output[:-1] + '\n'
                csvFile.write(output)
                
            return True


        def timeConverter(time):
            reg = '([0-9]{2}):([0-9]{2}):([0-9]{2},[0-9]{3})'
            matches = re.search(reg,  time)
            
            hours = int(matches.group(1)) * 3600
            minutes = int(matches.group(2)) * 60
            seconds = float(re.sub(',', '.',  matches.group(3)))
            
            total = hours + minutes + seconds
            return total


        def tagsSplit(string):
            reg = '\[(.*?)\]'
            tags = re.findall(reg, string)
            
            return tags


        def metaSplit(string):
            reg = '\*\*(.*?):(.*?)\*\*'
            metadata = re.findall(reg, string)
            
            return OrderedDict(metadata)


        def createRSyntax(fileName, folder, headersList):
            rSyntaxFile = codecs.open(folder+'//'+fileName+'.R',  'w',  'utf-8')
            
            rSyntaxFile.write('if(!exists(\"Data\")) { Data <- data.frame() }\n\n')
            rSyntaxFile.write(fileName+' <- read.csv(\"'+fileName+'.csv\", na.strings = \"NA\", nrows = -1, skip = 0, check.names = TRUE, strip.white = FALSE, blank.lines.skip = TRUE)\n\n')
            
            i = 1
            
            for header in headersList:
                rSyntaxFile.write('# ' + header + '\nattributes('+fileName+')$variable.labels[' + str(i) + '] <- \"' + header + '\"\n\n')
                i = i + 1
            
            rSyntaxFile.write('Data = merge(Data, '+fileName+', all=TRUE)\n\n')
            rSyntaxFile.write('for (i in 1:length (attributes('+fileName+')$variable.labels)) { rk.set.label (Data[[i]], attributes('+fileName+')$variable.labels[i]) }\n\n')
            rSyntaxFile.write('rm('+fileName+')')
            
            return True
            
        def popupMsg(msg,  status = u'Erreur'):
            popup = QtGui.QMessageBox()
            popup.setWindowTitle(status)
            popup.setText(msg)
            popup.exec_()


        if srtFilesFolder and folder:
            
            srtFiles = listSrtFiles(srtFilesFolder)
            
            if (srtFiles):
                config = getConfig(srtFilesFolder)
                
                if (config):
                    
                    if (os.path.isdir(folder)):
                    
                        try:
                            for srtFile in srtFiles:
                                parsedFile = parser(srtFile, config)
                                
                                if (parsedFile):
                                    if (createCsv(parsedFile['fileName'],  folder,  parsedFile['headers'],  parsedFile['lines'])):
                                        createRSyntax(parsedFile['fileName'],  folder, parsedFile['headers'])
                            
                            popupMsg(u'Fichiers R créés avec succès !',  u'Succès')
                        
                        except  IOError,  e:
                            popupMsg(str(e))
                           
                    else:
                        popupMsg(u'Erreur : le répertoire de destination ne semble pas exister.')

        else :
            popupMsg(u'Vous devez spécifier un dossier contenant les fichiers srt et un dossier de destination.')
