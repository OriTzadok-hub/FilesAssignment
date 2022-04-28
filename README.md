# FilesAssignment
The following script will generate a list of files inside the Windows root directory and match it according to a specific search criteria , it will output the final list that has the details of the files that matched the search criteria as a CSV file.

Description of the code: I created the class Target that gets the path of the root directory and a string that will hold the search criteria syntax.
the Target class has 2 classes that inherit from it TargetDiv for searching directories and TargetFile for searching files.

in the main code we create a class for each search criteria accordingly(TargtDir or TargetFile) ,

we run multiple processes , each of them gets a class and runs it's search function to find all the matching files/directories, all the details of the matching files/directories gets stored in the shared array.

when we finish searching we then create a CSV file from all the details in the shared array. 
