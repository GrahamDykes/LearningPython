import numpy as np
from time import sleep
random = np.random.randint

msg = "Roll a dice"
#print(msg)

R1 = np.random.randint(1,9)
R2 = np.random.randint(1,9)
R3 = np.random.randint(1,9)
R4 = np.random.randint(1,9)
R5 = np.random.randint(1,9)


#print(R1)
#print(R2)
#print(R3)
#print(R4)
#print(R5)
# print(np.random.randint(1,9))
totalAttack = R1+R2+R3+R4+R5


#if totalAttack > 30:
    # print('you dealt ' totalAttack ' damage!')
    #print ('You killed the Goblin')
#else:
    #print ('You died')


print('so you dare to test me?')
sleep(2)
print('very well then, roll the D20')
sleep(2)
outcome = random(1,20)
print('you have rolled ',outcome)
sleep(2)

if outcome == 1:
    print('you shall now suffer a fate worse than death. Not only you, but your entire lineage show now only know pain. They will wake up and eat broken glass and go to sleep with a red hot iron cathider. SUFFER!')
else:
    print('your ok')