In this code I used python as a program to guess the password like a brute force attack. You can check
it by coping the code and try it by your own password. If is is easy to guess or if it is one of the 
words which exists in the provided wordlist, program will find it. Otherwise it won't. 

So, mywordlist function returns the file content after taking the url as a parameter. hashing function 
takes the password as a parameter and returns its hash which contains hexadecimal digits. BruteForce 
function takes the hash of acutal password and the list of words, and then loops through the wordlist 
for each item and hashes it, then the program uses it to compare it with the hash of actual password. 
