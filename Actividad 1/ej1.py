# Ejercicio resuelto N°4

class Edades:
    @staticmethod
    def calcular_edAlber(edJuan):
        return (2/3) * edJuan

    @staticmethod
    def calcular_edAna(edJuan):
        return (4/3) * edJuan

    @staticmethod
    def calcular_edMama(edJuan, edAlber, edAna):
        return edJuan + edAlber + edAna

edJuan = 9
edAlber =Edades.calcular_edAlber(edJuan)
edAna = Edades.calcular_edAna(edJuan)
edMama = Edades.calcular_edMama(edJuan, edAlber, edAna)
print(f"Las edades son: \n- Alberto: {edAlber:.0f}\n- Juan: {edJuan:.0f} \n- Ana: {edAna:.0f} \n- Mama: {edMama:.0f}")