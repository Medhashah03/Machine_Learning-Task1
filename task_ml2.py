creepy_doll = ['red_light', 'green_light', 'red_light', 'you_got_shot', 'green_light', 'you_got_shot',
'you_got_shot', 'green_light', 'you_ got_shot', 'red_light', 'green_light', 'red_light', 'you_got_shot',
'green_light','red_light', 'red_light', 'green_light', 'you_got_shot','red_light', 'you_got_shot']
creepy_doll = creepy_doll[1:len(creepy_doll)-3]
creepy_doll = creepy_doll[0:len(creepy_doll):3]
print(creepy_doll)
