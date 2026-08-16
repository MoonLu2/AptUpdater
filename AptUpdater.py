import os

#----------------------------------
def welcome():
    print('Welcome to APT_UPDATER')
    print("")
exitq1 = input('   [APT_UPDATER(CurrentProgram)] Do you want to continue? (y/N)->')
#----------------------------------
#Welcoming
welcome()
if exitq1 == 'Y' or exitq1 == 'y':
   print('''Here it's "apt list --upgradable"''')
   os.system('sudo -S apt list --upgradable')
welcome()
#-------------------------------------------------
def upgrade():
    userq = input('   [APT_UPDATER(CurrentProgram)] Are you sure you wanna update everything or one package? (A/o/n < All/one/no)->')

    if userq == 'o' or userq == 'O':
        pkgname = input('What package to update for you? --->')
        os.system(f'sudo -S apt-get install --only-upgrade {pkgname}')
    
    elif userq == 'a' or userq == 'A':
        print('''Here it's "apt upgrade"''')
        os.system('sudo -S apt upgrade')
#-------------------------------------------------
# sudo apt upgrade/update (both)
upgrade()
#----------------------------------
def end():  
    exitq2 = input('   [APT_UPDATER(CurrentProgram)] Are you sure you need to update? (y/N)->')

    if exitq2 == 'Y' or exitq2 == 'y':
        print('''Here it's "apt list --upgradable"''')
        os.system('sudo -S apt list --upgradable')
    
    if exitq2 == 'N' or exitq2 == 'n' or exitq2 == '':
        print(f'{exitq2}')
        print(" ")
        return 0
    else:
        print('[APT_UPDATER(CurrentProgram)] syntax-error: input invalid')
        return 64
#----------------------------------
# End of the script
end()
#----------------------------------
# The code won't go over if it's imported. (the __main__ == "__name__" module was suggested)
if __name__ == "__main__":
    welcome()
    upgrade()
    exit(end())
else:
    print(f'''execution-err in {__name__}, this code was not intented for 'import'.''')
