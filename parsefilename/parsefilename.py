import os.path
import re

# Regex to make sure file name format is correct
REG_BLEND_SCENE = "^[a-zA-Z0-9]+-[0-9]{2}[.]blend$"
REG_BLEND_FBX = "^[a-zA-Z0-9]+-[0-9]{2}[.]fbx$"
REG_ANIM_SCENE = "^[a-zA-Z0-9]+-[a-zA-Z0-9]+-[0-9]{3}[.]ma$"
REG_ANIM_FBX = "^[a-zA-Z0-9]+-[a-zA-Z0-9]+-[0-9]{3}[.]fbx$"
REG_CINEMATIC_UASSET = "^[a-zA-Z0-9]+-[a-zA-Z0-9]+[.]uasset$"

"""
    Main function to use
    Take a file path as argument and returns dictionnary of data
"""
def ParseFileName(inputPath):
    if __debug__:
        print("DEBUG: Extracting path ", inputPath)

    if len(inputPath)==0:
        raise ValueError("Incorrect input path (empty)")

    # 1. Extracte the fileName from the path, in case it's a full path
    fileNameExtention = os.path.basename(inputPath)

    # 2. Get fileName without extension
    fileName, _fileExtension = os.path.splitext(fileNameExtention)

    if len(fileName) == 0:
        raise ValueError("Incorrect file name (empty)")
    
    # 3. Check fileName format and call the corresponding parsing function 
    resultData = {}
    if re.search(REG_BLEND_SCENE, fileNameExtention):
        resultData = _ParseFileNameBlenderScene(fileName)
    elif re.search(REG_BLEND_FBX, fileNameExtention):
        resultData = _ParseFileNameBlenderFBX(fileName)
    elif re.search(REG_ANIM_SCENE, fileNameExtention):
        resultData = _ParseFileNameAnimScene(fileName)
    elif re.search(REG_ANIM_FBX, fileNameExtention):
        resultData = _ParseFileNameAnimFBX(fileName)
    elif re.search(REG_CINEMATIC_UASSET, fileNameExtention):
        resultData = _ParseFileNameCinematic(fileName)
    else:
        raise ValueError(f"Unable to parse the given path '{inputPath}'")

    return resultData

"""
    Parse a .blend scene file
    Take a fileName argument and return the corresponding data
"""
def _ParseFileNameBlenderScene(fileName):  
    if __debug__:
        print("DEBUG: Extracting Blender Scene ", fileName)  
    
    splitPath = __GetDataFromFileName(fileName, 2)
    
    resultData = {}
    resultData["Character"] = {"name":splitPath[0], "version":splitPath[1]}

    return resultData

"""
    Parse a .fbx blender model file
    Take a fileName argument and return the corresponding data
"""
def _ParseFileNameBlenderFBX(fileName):  
    if __debug__:
        print("DEBUG: Extracting Blender FBX ", fileName)  

    splitPath = __GetDataFromFileName(fileName, 2)
    
    resultData = {}
    resultData["Character"] = {"name":splitPath[0], "version":splitPath[1]}

    return resultData

"""
    Parse a .ma animation scene file
    Take a fileName argument and return the corresponding data
"""
def _ParseFileNameAnimScene(fileName):  
    if __debug__:
        print("DEBUG: Extracting Animation Scene ", fileName)  

    splitPath = __GetDataFromFileName(fileName, 3)
    
    resultData = {}
    resultData["Character"] = {"name":splitPath[0]}
    resultData["Animation"] = {"action":splitPath[1], "version":splitPath[2]}

    return resultData

"""
    Parse a .fbx maya animation file
    Take a fileName argument and return the corresponding data
"""
def _ParseFileNameAnimFBX(fileName):  
    if __debug__:
        print("DEBUG: Extracting Animation FBX ", fileName)  

    splitPath = __GetDataFromFileName(fileName, 3)
    
    resultData = {}
    resultData["Character"] = {"name":splitPath[0]}
    resultData["Animation"] = {"action":splitPath[1], "version":splitPath[2]}

    return resultData

"""
    Parse a .uasset cinematic file
    Take a fileName argument and return the corresponding data
"""
def _ParseFileNameCinematic(fileName):  
    if __debug__:
        print("DEBUG: Extracting Cinematic Asset ", fileName)  

    splitPath = __GetDataFromFileName(fileName, 2)
    
    resultData = {}
    resultData["Cinematic"] = {"name":splitPath[0]}
    resultData["Character"] = {"name":splitPath[1]}

    return resultData


"""
    Ensure the fileName format is adequate and return an array of data to parse
    Prevent code redundancy among parsing functions
"""
def __GetDataFromFileName(fileName, expectedDataCount):
    if len(fileName) == 0:
        raise ValueError("Incorrect file name (empty)")

    splitPath = fileName.split("-")
    if len(splitPath) != expectedDataCount:
        raise ValueError(f"Incorrect file name (wrong format) {fileName}")
    
    return splitPath
    