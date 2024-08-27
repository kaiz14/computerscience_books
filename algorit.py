staff = {
    'Juan': {
        'cargo': 'marketing',
        'desempeño': 71
    },
    'Sofia': {
        'cargo': 'marketing',
        'desempeño': 65
    },
    'Andres': {
        'cargo': 'marketing',
        'desempeño': 49
    },
    'Romina': {
        'cargo': 'marketing',
        'desempeño': 53
    }
}

def id_desempeño_bajo(staff):
    desempeño_bajo = []
    for empleado, datos in staff.items():
        if datos['desempeño'] < 50:
            desempeño_bajo.append(empleado)
    return desempeño_bajo

def eliminar_desempeño_bajo(staff, empleados_bajo_desempeño):
    for empleado in empleados_bajo_desempeño:
        del staff[empleado]

empleados_bajo = id_desempeño_bajo(staff)
if empleados_bajo:
    for empleado in empleados_bajo:
        print("Se recomienda despedir al siguiente empleado", empleado)
    eliminar_desempeño_bajo(staff, empleados_bajo)
else:
    print("No hay trabajadores con bajo desempeño.")

print("\nTrabajadores de alto desempeño:")
for empleado in staff:
    print(empleado)


'''
empleados_bajo = [empleado for empleado, datos in staff.items() if datos['desempeño'] < 50]

if empleados_bajo:
    for empleado in empleados_bajo:
        print("Se recomienda despedir al trabajador", empleado)
    staff = {empleado: datos for empleado, datos in staff.items() if empleado not in empleados_bajo}
    
print("Los trabajadores con mejor desempeño:")
for empleado in staff:
    print(empleado)

#-----------------------------------------------------------------------
def id_desempeno_bajo(staff):
    desempeno_bajo = []
    for empleado, datos in staff.items():
        if datos['desempeño'] < 50:
            desempeno_bajo.append(empleado)
    return desempeno_bajo

def eliminar_desempeno_bajo(staff, empleados_bajo_desempeno):
    for empleado in empleados_bajo_desempeno:
        del staff[empleado]

empleados_bajo = id_desempeno_bajo(staff)
if empleados_bajo:
    for empleado in empleados_bajo:
        print("Se recomienda despedir al trabajador", empleado)
    del staff[empleado]

print("Los trabajadores con mejor desempeño:")
for empleado in staff:
    print(empleado)
'''