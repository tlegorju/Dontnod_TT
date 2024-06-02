Author: Thibault Le Gorju
Dontnod Technical Test for Tools Programmer position

The goal of this project is to propose a solution to the problem of extracting data from a file name depending on its format and extension.

=== STRUCTURE ===
The project is divised in a main file, a parsefilename package which contains the logic of the solution and a test package.
The test package aims to provide extensive and thorough tests for the solution in a way that would be easily maintanable and reproducible if the rules for the file name format were to change.
The parsefilename in itself is composed of a main function ParseFileName that take a fileName in input and return a dictionnary of expected data.
Several other function perform the actual parsing of the data depending on its type (format & extension). While this may cause code redundancy, I believe the readability of the file makes it worth it.
If existing file name formats were to be changed, or new ones be added, it would be easy and quick to adapt the code to these changes while remaining performant.

=== TESTS ===
You can quickly try the program using RunCode.bat in the project folder.
You can quickly run the tests for this program using RunTestCode.bat in the project folder. 

=== COMMENTS ===
Considering the only function to use is ParseFileName, it could be said that there are a lot of parameter verification and a certain redundancy accross them.
Thought it's better to be safe than sorry, and it make sure that each function has always and will always have correct parameters as input. Therefore it prevents unexpected behavior.

It is assumed that the parsed file either exists, or its existance is irrelevant so we don't check that
It is assumed that file names can only be composed of alphanumerical characters, and no special characters (-,_,\,...). If this changes the regex will have to be updated and some tests as well.
