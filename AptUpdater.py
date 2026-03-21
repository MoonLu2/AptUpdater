def welcome():
    import os
    print('Welcome to APT_UPDATER')
    print("")
    exitq1 = input('   [APT_UPDATER(CurrentProgram)] Do you want to continue? (y/N)->')

# A  l o t  o f  c h e c k s  f o r  t h e  u s e r ' s  p r e f e r e n c e .

    if exitq1 == 'Y' or exitq1 == 'y':
        print('''Here it's "apt list --upgradable"''')
        os.system('sudo -S apt list --upgradable')


def upgrade():
    import os
    userq = input('   [APT_UPDATER(CurrentProgram)] Are you sure you wanna update everything or one package? (A/o/n < All/one/no)->')
    
    if userq == 'o' or userq == 'O':
        pkgname = input('What package to update for you? --->')
        os.system(f'sudo -S apt-get install --only-upgrade {pkgname}')
    
    elif userq == 'a' or userq == 'A':
        print('''Here it's "apt upgrade"''')
        os.system('sudo -S apt upgrade')


def end():
    import os
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

# welcome()
# upgrade()
# end()

# The code won't go over if it's imported. (the __main__ == "__name__" module was suggested)
if __name__ == "__main__":
    welcome()
    upgrade()
    exit(end())
else:
    print(f'''execution-err in {__name__}, this code was not intented for 'import'.''')
