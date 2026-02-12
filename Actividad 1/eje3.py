# Ejercicio Propuesto N°12
 
class Calcular:
    @staticmethod
    def salario_bruto(horas_trabajadas, valor_hora):
        return horas_trabajadas * valor_hora
    @staticmethod
    def retencion_en_fuente(salario_bruto):
        return salario_bruto * 0.125 
    @staticmethod
    def salario_neto(salario_bruto, retencion_en_fuente):
        return salario_bruto -  retencion_en_fuente
    
sb = Calcular.salario_bruto(48,5000)
ref = Calcular.retencion_en_fuente(sb)
sn = Calcular.salario_neto(sb, ref)

print(f"Salario bruto: {sb:.0f}\nretención en la fuente: {ref:.0f}\nsalario neto: {sn:.0f}")