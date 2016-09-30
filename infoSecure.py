"""
(C) Iftekhar Hyder 2016
"""

import os, sys


wordlist = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
            'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A',
            'B', 'C', 'D', 'E', 'F', 'G','H', 'I', 'J',
            'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S',
            'T', 'U', 'V', 'W', 'X','Y', 'Z', '0', '1',
            '2', '3', '4', '5', '6', '7', '8', '9', '.', ';', ':', ',', ' ', '!', "(", ")", "~", "{", "}"];

keylist = ['20ex', '13y', '342t', '4345c', '343424s', '6656345x', '77677c', '775454t', '213867s', '345469c',
           '1e0sda', '1451df', '143322sd', '13453f', '13244d', '12342355s','32416d', '1324327b', '1234328c',
           '1e9xc', '2e0er', '2331vcx', '2332vf', '3423423', '23244', '2443235', '26457', '253324237',
           '4557', '90476324', 'ygy3u24783', '457843nd', '32472344gdfd','78236487gbsat78', '234243868dsh',
           'fdyugasd8734', '4543245345',
           '3424223437327634534g', '3423423438', '4543539', '23423423440', '32423441',
           '3242344sdsd2', '32423443', '55532423444', '3432434545',
           '3423443243246', '354423524623447', '34223423432423448', '12331245424349','2342342355',
           '2342345524352341', '324435sda324s2',
           '342344556353', '3242342343354','677685566555', '23423456', '43534534557', '435363453445358',
           '5saddas9', '60assad', '61sdasd',
           '2342342390x', '46363324fg', '544532hy', '34543765474589x', '23443432324xxx', "5846d", "23473t6gdf78", "2347842367dfd78", "458943897erbf89",
           '23d3f323432434', '2342344454w64']



class InfoSecure:


    def displayMenu(self):
        print ". . . . . .\n"
        print "1. Store Information With Key\n"
        print "2. Unlock Information With Key\n"
        print "3. View All Information Stored(Admin Pass Required)\n"
        print "4. Quit\n"
        print ". . . . . .\n"

    def getString(self, prompt):
        try:
            x = str(raw_input(prompt));
            return x
        except err:
            print str(err) + "\n"
        
    def storeInfo(self):
        global wordlist, keylist
        
        info = self.getString("Enter information you want to store > ")
        pwd = self.getString("Enter a key for your information > ")
        pwdcode = ''
        for i in range(len(pwd)):
            pwdcode += keylist[wordlist.index(pwd[i])]

        
        keyInput = []
        for i in range(len(info)):
            keyInput.append(keylist[wordlist.index(info[i])])

        keyString = ''

        for i in range(len(keyInput)):
            if i != len(keyInput) - 1:
                keyString += keyInput[i] + "-"
            else:
                keyString += keyInput[i]

        f = open("data.txt", "a")
        f.write(keyString + "-" + pwdcode + "\n")
        f.close()
        

        self.__init__()
        
    def unlockInfo(self):
        # most complex function
        global wordlist, keylist

        f = open("data.txt", "a")
        f.close()
        
        pwd = self.getString("Enter key for your information > ")
        pwdcode = ''
        for i in range(len(pwd)):
            pwdcode += keylist[wordlist.index(pwd[i])]
        
        
        x = []
        codeString = ''
        with open("data.txt", "r") as f:
            codeString += ''.join(f.readlines())


        codeList = codeString.split('\n')


        for i in range(len(codeList)):
            code = codeList[i].split('-')
            String = ""
            found = ""

            if code[-1] == pwdcode:
                for i in range(len(code) - 1):
                    if code[i] != '':
                        String += (wordlist[keylist.index(code[i])])

                found = "==========================\nUnlocked Information: " + String + "\n==========================\n"
                break;
                
            else:
                continue;

        if found == "":
            print "\n. . . No Information found with that key . . . \n"
        else:
            print found
        

        

        self.__init__()
    def viewAll(self):

        f = open("data.txt", "a")
        f.close()
        pwd = self.getString("Enter Admin Password: ")
        if pwd == "infosecureifty":
            global wordlist, keylist
            print ". . . Encrypted Codes . . . \n"

            x = []
            codeString = ''


            with open("data.txt", "r") as f:
                codeString += ''.join(f.readlines())

            print codeString

            codeList = codeString.split('\n')

            print ". . . Decrypted Codes . . . \n"

            for i in range(len(codeList)):
                code = codeList[i].split('-')
                String = ""

                for i in range(len(code) - 1):
                    if code[i] != '':
                        String += (wordlist[keylist.index(code[i])])
                print String + "\n"
        else:
            print "!!! Wrong password!~\n"
        


        self.__init__()
        
    def __init__(self):
        self.displayMenu()
        choice = self.getString("Enter Choice >> ")

        if choice == "1":
            # 1
            self.storeInfo()
        elif choice == "2":
            # 2
            self.unlockInfo()
        elif choice == "3":
            # 3
            self.viewAll()


if __name__ == "__main__":

    print ". . Info Secure / Ver: Beta . . . \n. . (C) Iftekhar Hyder 2016 . . .\n"
    print ". . . . . . . . . . . . . . . . . \n"
    InfoSecure()
    
