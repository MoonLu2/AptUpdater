#!/bin/python3
import os
print('Welcome to APT_UPDATER')
print("")
exitq = input('   [APT_UPDATER(CurrentProgram)] Do you want to continue? (y/N)->')
 
while exitq == 'Y' or exitq == 'y':
    print('''Here it's "apt list --upgradable"''')
    os.system('sudo -S apt list --upgradable')
    exitq2 = input('   [APT_UPDATER(CurrentProgram)] Do you want to continue? (y/N)->')
    if exitq2 == 'N' or exitq2 == 'n' or exitq2 == '':
        exit(0)
    print(f'{exitq2}')
    userq = input('   [APT_UPDATER(CurrentProgram)] Are you sure you wanna update everything or one package? (A/o/n < All/one/no)->')
    print(" ")
    if userq == 'o' or userq == 'O':
        pkgname = input('What package to update for you? --->')
        os.system(f'sudo -S apt-get install --only-upgrade {pkgname}') 
    elif userq == 'a' or userq == 'A':
        print('''Here it's "apt upgrade"''')
        os.system('sudo -S apt upgrade')
    if exitq == 'N' or exitq == 'n' or exitq == '':
        exit(0)
