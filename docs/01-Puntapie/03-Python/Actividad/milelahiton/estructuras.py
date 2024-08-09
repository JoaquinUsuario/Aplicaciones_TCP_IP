#import markdown
import os

with open('curso.md', 'r') as f:
    lineas = f.readlines()
    #total = len(lineas)
    main = lineas[0]
    main = main[:-1]
    main = main[2:]
    os.makedirs(main)
    for l in lineas:
        if l[0:2] == '##':
            path = os.path.join(main, l[3:-1])
            os.makedirs(path)
        if l[0:1] == '-':
            newpath = os.path.join(path, l[2:-1])
            os.makedirs(newpath)
            os.makedirs(os.path.join(newpath,'assets'))
            textpath = os.path.join(newpath, l[2:-1])
            with open(textpath + '.md', 'w') as text:
                text.write('# Titulo del Tema \n## Resumen \n\nAqui puedes proporcionar un resumen breve del tema.\n\n\
## Introduccion\n\nAqui puedes introducir el tema y proporcionar contexto o informacion relevante\n\n\
## Desarrollo\n\nAqui puedes desarrollar el contenido del tema en detalle\n\n\
## Cierre\n\nAqui puedes hacer un resumen o conclusion del tema\n\n## Actividad')


