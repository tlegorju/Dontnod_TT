from parsefilename import ParseFileName

def main():
    try:
        print(ParseFileName("Max-01.blend"))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName("Max-01.fbx"))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName("Max-Running-001.ma"))
    except ValueError as e:
        print(e)
    print("===========")
    try:        
        print(ParseFileName("Max-Running-001.fbx"))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName("EscapingTheBaddies-Max.uasset"))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName("Max-01blend"))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName("Max-01ablend"))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName("Max-1.blend"))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName("Max01.blend"))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName(".blend"))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName("Max-01."))
    except ValueError as e:
        print(e)
    print("===========")
    try:
        print(ParseFileName(""))
    except ValueError as e:
        print(e)
    print("===========")

if __name__ == "__main__":
    main()