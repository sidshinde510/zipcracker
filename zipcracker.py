from termcolor import colored # type: ignore
from tqdm import tqdm # type: ignore
import zipfile

var =""
wordlist = [passwords.strip() for passwords in open("wordlist.txt")]
zip_file = zipfile.ZipFile("p1.zip")

for i in tqdm(wordlist,desc="checking passwords in wordlist"):
    try:
        zip_file.extractall(pwd=i.encode())
        var=i
        break
    except:
        continue
print(colored("[+] Password Found: {}".format(var),'green'))
