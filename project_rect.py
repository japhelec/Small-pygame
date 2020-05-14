
obj_list = []
creature_list = []

obj_Width = 10
obj_Height = 10

creature_Width = 50
creature_Height =80

undefended_creature = 0

newObj = {'rect':pygame.rect(starting_X,starting_Y, ObjSize_X, ObjSize_Y), 'surface':pygame.transform.scale(obj_image, (objSize_X, objSize_Y))}
obj_list.append(newObj)

newCreature = {'rect':pygame.rect(starting_X,starting_Y, creatureSize_X, creatureSize_Y), 'surface':pygame.transform.scale(creature_image, (creatureSize_X, creatureSize_Y))}
creature_list.append(newCreature)

def creatureWasHit(obj_list, z):
    for o in obj_list:
        if o['rect'].colliderect(z['rect']):
            obj_list.remove(o)
            gameHitSound.play()
            return True
    return False

for o in obj_list[:]:
    if o['rect'].right>SCREENSIZE[0]:
        obj_list.remove(o)
    if o['rect'].left < 0:
        obj_list.remove(o)
    if o['rect'].down <0: #not sure whether to be "down"
        obj_list.remove(o)
    
for z in creature_list:
    z['rect'].move_ip(delta_X, delta_Y)

for z in creature_list[:]:
    if z['rect'].left<0:
        creature_list.remove(z)
        undefended_creature += 1 #or 2 or 10

for z in creature_list:
    if creatureWasHit(obj_list, z):
        Score += 1 #or 2 or 10
        creature_list.remove(z)
        
