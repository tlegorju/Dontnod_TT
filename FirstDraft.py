# First draft

# Exercice 1 : extract data from Character scene
def ExtractDataFromBlendSceneFile(inputPath):
    print("DEBUG: Extracting path ", inputPath)

    resultData = {}

    splitPath = inputPath.split(".")
    if len(splitPath) != 2:
        raise ValueError(f"ValueError: incorrect path '{inputPath}'")
    
    if splitPath[1] != "blend":
        raise ValueError(f"ValueError: file is not a .blend '{inputPath}'")
    
    splitPath = splitPath[0].split("-")
    if len(splitPath) != 2:
        raise ValueError(f"ValueError: incorrect path '{inputPath}'")
    
    if len(splitPath[0]) == 0 or len(splitPath[1]) != 2:
        raise ValueError(f"ValueError: file path has wrong format '{inputPath}'")

    try:
        int(splitPath[1])
    except ValueError:
        raise ValueError(f"ValueError: file version is incorrect '{inputPath}'")
    
    resultData["Character"] = {"name":splitPath[0], "version":splitPath[1]}

    return resultData

def TestExo1():
    testPath1 = "Max-01.blend"
    testPath2 = "Max-1.blend"
    testPath3 = "Max-01.ma"
    testPath4 = "-01.blend"
    testPath5 = "Max01.blend"

    try:
        print(ExtractDataFromBlendSceneFile(testPath1))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ExtractDataFromBlendSceneFile(testPath2))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ExtractDataFromBlendSceneFile(testPath3))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ExtractDataFromBlendSceneFile(testPath4))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ExtractDataFromBlendSceneFile(testPath5))
    except ValueError as e:
        print(e)
    print("===========")

# Exercice 3 : extract data from Animation fbx
def ExtractDataFromAnimFBXFile(inputPath):
    print("DEBUG: Extracting path ", inputPath)

    resultData = {}

    splitPath = inputPath.split(".")
    if len(splitPath) != 2:
        raise ValueError(f"ValueError: file path has wrong format '{inputPath}'")
    
    if splitPath[1] != "fbx":
        raise ValueError(f"ValueError: file is not a .fbx '{inputPath}'")
    
    splitPath = splitPath[0].split("-")
    if len(splitPath) != 3:
        raise ValueError(f"ValueError: file path has wrong format '{inputPath}'")
    
    if len(splitPath[0]) == 0 or len(splitPath[1]) == 0 or len(splitPath[2]) != 3:
        raise ValueError(f"ValueError: file path has wrong format '{inputPath}'")

    try:
        int(splitPath[2])
    except ValueError:
        raise ValueError(f"ValueError: file version is incorrect '{inputPath}'")
    
    resultData["Character"] = {"name":splitPath[0]}
    resultData["Animation"] = {"action":splitPath[1], "version":splitPath[2]}

    return resultData

def TestExo3():
    testPath1 = "Max-Running-001.fbx"
    testPath2 = "Max-Running-001.ma"
    testPath3 = "Max-Running-01.fbx"
    testPath4 = "Max--001.fbx"
    testPath5 = "MaxRunning001.fbx"

    try:
        print(ExtractDataFromAnimFBXFile(testPath1))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ExtractDataFromAnimFBXFile(testPath2))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ExtractDataFromAnimFBXFile(testPath3))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ExtractDataFromAnimFBXFile(testPath4))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ExtractDataFromAnimFBXFile(testPath5))
    except ValueError as e:
        print(e)
    print("===========")

TestExo1()
TestExo3()
