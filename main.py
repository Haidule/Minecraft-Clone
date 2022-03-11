from ursina import *
from ursina.prefabs.\
    first_person_controller \
    import FirstPersonController

app = Ursina()
Sky(texture= 'sky_sunset')
player = FirstPersonController()

boxes = []
for n in range(12):
    for k in range(12):
        box = Button(
            color=color.white,
            model='cube',
            position=(k,0,n),
            texture= 'grass',
            parent=scene,
            orgin_y=1
        )
        boxes.append(box)

def input(key):
    for box in boxes:
        if box.hovered:
            if key == 'left mouse down':
                new = Button(
                    color=color.green,
                    model='cube',
                    position=
                    box.position + mouse.normal,
                    texture='/Textures/alex-downham-low-poly-crate-diffuse.jpeg',
                    parent=scene,
                    origin_y=1
                )
                boxes.append(new)
            if key == 'right mouse down':
                boxes.remove(box)
                destroy(box)

app.run()