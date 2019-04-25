# calcolo di superfici e volume di un parallelepipedo

latoParallelepipedo_A = int(input("Qual è il valore in centimetri del PRIMO lato di base del parallelepipedo? "))

# -----------> AGGIUNTA <----------------

# il parallelepipedo ha tre lati quindi bisogna chiederne altri due
latoParallelepipedo_B = int(input("Qual è il valore in centimetri del SECONDO lato di base del parallelepipedo? "))
latoParallelepipedo_H = int(input("Qual è il valore in centimetri dell'ALTEZZA del parallelepipedo? "))
# calcoliamo il perimetro di base, che può essere comodo, superficie di base e laterale per cominciare
perimetroBaseParallelepipedo = 2*latoParallelepipedo_A + 2*latoParallelepipedo_B
supBaseParallelepipedo = latoParallelepipedo_A * latoParallelepipedo_B
supLateraleParallelepipedo = perimetroBaseParallelepipedo * latoParallelepipedo_H

# -----------> FINE AGGIUNTA <------------

# ora che hai calcolato supLaterae e supBase puoi utilizzare i valori per fare le somme
# diversamente il computer non sa cosa sono e quanto valgono

supTotaleParallelepipedo = supLateraleParallelepipedo + 2* supBaseParallelepipedo
volumeParallelepipedo = supBaseParallelepipedo * latoParallelepipedo_H

print("Il valore della superficie laterale è ", supLateraleParallelepipedo, "cm2")
print("Il valore della superficie totale è ", supTotaleParallelepipedo, "cm2")
print("Il valore del volume è ", volumeParallelepipedo, "cm3")
