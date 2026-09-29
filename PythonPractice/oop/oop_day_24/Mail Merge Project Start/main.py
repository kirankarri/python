#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
with open('./Input/Letters/starting_letter.txt') as starting_letter:
    content = starting_letter.read()
INames_list = []
with open('Input/Names/invited_names.txt') as INames:
    while True:
        name = INames.readline()
        if not name:
            break
        INames_list.append(name.strip())

for name in INames_list:
    updated_content = content.replace('[name]',name)
    with open(f'./Output/ReadyToSend/{name}.txt','w') as tmp:
        tmp.write(updated_content)
    