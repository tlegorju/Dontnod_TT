from parsefilename.parsefilename import ParseFileName
import sys

def _DoParseFile(filePath):
    try:
        resultData = ParseFileName(filePath)
    except ValueError as err:
        print("Incorrect file path, please try again")
        print(err)
    except Exception as err:
        print(f"Unknown exception raised : {err}")
    else:
        print(resultData)

def main():
    print("Hello, please enter the path of the file you want to parse ('exit' to quit).")
    filePath = input("")

    while True:
        if filePath == "exit":
            break
        _DoParseFile(filePath)


        filePath = input("Enter a new file path ('exit' to quit) : ")


if __name__ == "__main__":
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
            _DoParseFile(arg)

    main()