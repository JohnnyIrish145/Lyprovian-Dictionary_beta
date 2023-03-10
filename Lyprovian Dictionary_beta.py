import io

directoryEN = "englishlower.txt"
directoryLP = "translatedlower.txt"
Error = "Sorry, but we currently do not have that word"
Design = "---------------------------------------------"
DesignLp = "English:"
DesignEn = "Lieprulaviu:"
Eqalizer = "\n"
Eqalizer = str(Eqalizer)

print(Design)
print("----Welcome to the Lieprulaviu dictionary----")
print(Design)
print("")
print("Type a word in english below to translate it to Lieprulaviu")
print("")

while True:
    print(DesignLp)
    console = input()
    Letters = [str(Letters) for Letters in console]
    First_letter = str(Letters[0])
    WordPlace = 0
    console = list(console + Eqalizer)
    console = str(console)
    print(DesignEn)
    with open(directoryEN,"r") as EnFile:
        EnWords = EnFile.readlines()
    if First_letter.isnumeric():
        while True:
            Wordlist = list(EnWords[WordPlace])
            EnWord = str(Wordlist)
            if console == EnWord:
                with io.open(directoryLP, mode = "r", encoding = "utf-8") as LpFile:
                    LpWords = LpFile.readlines()
                FinaleLpWord = LpWords[WordPlace]
                print(FinaleLpWord)
                print(Design)
                WordPlace = 0
                EnFile.close()
                LpFile.close()
                break
            elif WordPlace > 390:
                print(Error)
                print(Design)
                EnFile.close()
                break
            else:
                WordPlace += 1
    elif First_letter.isupper():
        g = console.lower()
        while True:
            Wordlist = list(EnWords[WordPlace])
            EnWord = str(Wordlist)
            if console == EnWord:
                with io.open(directoryLP, mode = "r", encoding = "utf-8") as LpFile:
                    LpWords = LpFile.readlines()
                FinaleLpWord = LpWords[WordPlace]
                print(FinaleLpWord)
                print(Design)
                WordPlace = 0
                EnFile.close()
                LpFile.close()
                break
            elif WordPlace>390:
                print(Error)
                print(Design)
                EnFile.close()
                break
            else:
                WordPlace += 1
    elif First_letter.islower():
        console.lower()
        while True:
            Wordlist = list(EnWords[WordPlace])
            EnWord = str(Wordlist)
            if console == EnWord:
                with io.open(directoryLP, mode = "r", encoding = "utf-8") as LpFile:
                    LpWords = LpFile.readlines()
                FinaleLpWord = LpWords[WordPlace].lower()
                print(FinaleLpWord)
                print(Design)
                WordPlace = 0
                EnFile.close()
                LpFile.close()
                break
            elif WordPlace>390:
                print(Error)
                print(Design)
                EnFile.close()
                break
            else:
                WordPlace += 1