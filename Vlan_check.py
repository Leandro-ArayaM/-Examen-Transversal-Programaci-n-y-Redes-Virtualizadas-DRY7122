vlan = int(input("Ingrese el número de VLAN: "))

if 1 <= vlan <= 1005:
    print("La VLAN corresponde al rango normal.")
elif 1006 <= vlan <= 4094:
    print("La VLAN corresponde al rango extendido.")
else:
    print("El número de VLAN no es válido.")
def verificar_vlan(vlan_id):
    if 1 <= vlan_id <= 1005:
        return "La VLAN corresponde al rango **normal** (1 - 1005)."
    elif 1006 <= vlan_id <= 4094:
        return "La VLAN corresponde al rango **extendido** (1006 - 4094)."
    else:
        return "Número de VLAN no válido. Debe estar entre 1 y 4094."

def main():
    try:
        vlan_input = int(input("Ingrese el número de VLAN: "))
        resultado = verificar_vlan(vlan_input)
        print(resultado)
    except ValueError:
        print("Debe ingresar un número entero válido.")
if __name__ == "__main__":
    main()
