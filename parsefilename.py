import os
import re

REG_BLEND_SCENE = "[a-zA-Z0-9]+-[0-9]{2}[.]blend$"
REG_BLEND_FBX = "[a-zA-Z0-9]+-[0-9]{2}[.]fbx$"
REG_ANIM_SCENE = "[a-zA-Z0-9]+-[a-zA-Z0-9]+-[0-9]{3}[.]ma$"
REG_ANIM_FBX = "[a-zA-Z0-9]+-[a-zA-Z0-9]+-[0-9]{3}[.]fbx$"
REG_CINEMATIC_UASSET = "[a-zA-Z0-9]+-[a-zA-Z0-9]+[.]uasset$"

def ParseFileName(inputPath):
    print("DEBUG: Extracting path ", inputPath)

    resultData = {}

    # 1. GetFileExtension
    fileName, fileExtension = os.path.splitext(inputPath)

    #if len(fileName) == 0:
    #    raise ValueError(f"ValueError: file name is empty '{inputPath}'")
    #if len(fileExtension) == 0:
    #    raise ValueError(f"ValueError: file extension is empty '{inputPath}'")
    
    if re.search(REG_BLEND_SCENE, inputPath):
        print("Blend scene !")
        resultData = ParseFileNameBlenderScene(fileName)
    elif re.search(REG_BLEND_FBX, inputPath):
        print("Blend modele !")
        resultData = ParseFileNameBlenderFBX(fileName)
    elif re.search(REG_ANIM_SCENE, inputPath):
        print("Maya scene !")
        resultData = ParseFileNameAnimScene(fileName)
    elif re.search(REG_ANIM_FBX, inputPath):
        print("Animation !")
        resultData = ParseFileNameAnimFBX(fileName)
    elif re.search(REG_CINEMATIC_UASSET, inputPath):
        print("Cinematic !")
        resultData = ParseFileNameCinematic(fileName)
    else:
        raise ValueError(f"ValueError: Unable to parse the given path '{inputPath}'")

    # 2. Call corresponding function

    return resultData

def ParseFileNameBlenderScene(fileName):  
    print("DEBUG: Extracting path ", fileName)  

    resultData = {}

    splitPath = fileName.split("-")
    resultData["Character"] = {"name":splitPath[0], "version":splitPath[1]}

    return resultData

def ParseFileNameBlenderFBX(fileName):  
    print("DEBUG: Extracting path ", fileName)  

    resultData = {}

    splitPath = fileName.split("-")
    resultData["Character"] = {"name":splitPath[0], "version":splitPath[1]}

    return resultData

def ParseFileNameAnimScene(fileName):  
    print("DEBUG: Extracting path ", fileName)  

    resultData = {}

    splitPath = fileName.split("-")
    resultData["Character"] = {"name":splitPath[0]}
    resultData["Animation"] = {"action":splitPath[1], "version":splitPath[2]}

    return resultData

def ParseFileNameAnimFBX(fileName):  
    print("DEBUG: Extracting path ", fileName)  

    resultData = {}

    splitPath = fileName.split("-")
    resultData["Character"] = {"name":splitPath[0]}
    resultData["Animation"] = {"action":splitPath[1], "version":splitPath[2]}

    return resultData

def ParseFileNameCinematic(fileName):  
    print("DEBUG: Extracting path ", fileName)  

    resultData = {}

    splitPath = fileName.split("-")
    resultData["Cinematic"] = {"name":splitPath[0]}
    resultData["Character"] = {"name":splitPath[1]}

    return resultData
