import CommandExecuter
print('NTerminal Loaded Successfully')
while(True):
    command = input('$')
    CommandExecuter.Execute(command)