#This code is comprised of rules that Spanish grammar uses, specifically
#irregular verb endings.

PreteriteIrregularVerbEndings = ['PreteriteIrregularVerbEndingsER', 'PreteriteIrregularVerbEndingsECIR', 'PreteriteIrregularVerbEndingsUCIR']
print("""\
Usage: Preterite Irregular Verb Endings Index:
    -To look up endings ER, ECIR, UCIR
    -Use 'PreteriteIrregularVerbEndings'
    -PIVE, is the stem for Preterite Irregilar Verb Endings followed by:
    -FPOV--, is first point of view
    -SPOV--, is second point of view
    -TPOV--, is third point of view
""")

#ER
PreteriteIrregularVerbEndingsER = ['PIVEFPOVER' , 'PIVESPOVER', 'PIVETPOVER']
PreteriteIrregularVerbEndingsFirstPersonSingularER = ['je']
PreteriteIrregularVerbEndingsFirstPersonPluralER = ['jimos']
PreteriteIrregularVerbEndingsFirstPersonER = ['PreteriteIrregularVerbEndingsFirstPersonSingularER', 'PreteriteIrregularVerbEndingsFirstPersonPluralER']
PIVEFPOVER = ['PreteriteIrregularVerbEndingsFirstPersonER']
SingularOrPluralPIVEFPOVER = ((PreteriteIrregularVerbEndingsFirstPersonSingularER, PreteriteIrregularVerbEndingsFirstPersonPluralER),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularER = ['jiste']
PreteriteIrregularVerbEndingsSecondPersonPluralER = ['jisteis']
PreteriteIrregularVerbEndingsSecondPersonER= ['PreteriteIrregularVerbEndingsSecondPersonSingularER', 'PreteriteIrregularVerbEndingsSecondPersonPluralER']
PIVESPOVER = ['PreteriteIrregularVerbEndingsSecondPersonER']
SingularOrPluralPIVESPOVER = ((PreteriteIrregularVerbEndingsSecondPersonSingularER, PreteriteIrregularVerbEndingsSecondPersonPluralER),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularER = ['jo']
PreteriteIrregularVerbEndingsThirdPersonPluralER = ['jeron']
PreteriteIrregularVerbEndingsThirdPersonER = ['PreteriteIrregularVerbEndingsThirdPersonSingularER', 'PreteriteIrregularVerbEndingsThirdPersonPluralE']
PIVETPOVER = ['PreteriteIrregularVerbEndingsThirdPersonER']
SingularOrPluralPIVETPOVER = ((PreteriteIrregularVerbEndingsThirdPersonSingularER, PreteriteIrregularVerbEndingsThirdPersonPluralER),('singular', 'plural'))

#ECIR
PreteriteIrregularVerbEndingsECIR = ['PIVEFPOVECIR' , 'PIVESPOVECIR', 'PIVETPOVECIR']
PreteriteIrregularVerbEndingsFirstPersonSingularECIR = ['je']
PreteriteIrregularVerbEndingsFirstPersonPluralECIR = ['jimos']
PreteriteIrregularVerbEndingsFirstPersonECIR = ['PreteriteIrregularVerbEndingsFirstPersonSingularECIR', 'PreteriteIrregularVerbEndingsFirstPersonPluralECIR']
PIVEFPOVECIR = ['PreteriteIrregularVerbEndingsFirstPersonECIR']
SingularOrPluralPIVESPOVECIR = ((PreteriteIrregularVerbEndingsFirstPersonSingularECIR, PreteriteIrregularVerbEndingsFirstPersonPluralECIR),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularECIR = ['jiste']
PreteriteIrregularVerbEndingsSecondPersonPluralECIR = ['jisteis']
PreteriteIrregularVerbEndingsSecondPersonECIR = ['PreteriteIrregularVerbEndingsSecondPersonSingularECIR', 'PreteriteIrregularVerbEndingsSecondPersonPluralECIR']
PIVESPOVECIR = ['PreteriteIrregularVerbEndingsSecondPersonECIR']
SingularOrPluralPIVESPOVECIR = ((PreteriteIrregularVerbEndingsSecondPersonSingularECIR, PreteriteIrregularVerbEndingsSecondPersonPluralECIR),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularECIR = ['jo']
PreteriteIrregularVerbEndingsThirdPersonPluralECIR = ['jeron']
PreteriteIrregularVerbEndingsThirdPersonECIR = ['PreteriteIrregularVerbEndingsThirdPersonSingularER', 'PreteriteIrregularVerbEndingsThirdPersonPluralE']
PIVETPOVECIR = ['PreteriteIrregularVerbEndingsThirdPersonER']
SingularOrPluralPIVETPOVECIR = ((PreteriteIrregularVerbEndingsThirdPersonSingularECIR, PreteriteIrregularVerbEndingsThirdPersonPluralECIR),('singular', 'plural'))

#UCIR
PreteriteIrregularVerbEndingsUCIR = ['PIVEFPOVUCIR' , 'PIVESPOVUCIR', 'PIVETPOVUCIR']
PreteriteIrregularVerbEndingsFirstPersonSingularUCIR = ['je']
PreteriteIrregularVerbEndingsFirstPersonPluralUCIR = ['jimos']
PreteriteIrregularVerbEndingsFirstPersonUCIR = ['PreteriteIrregularVerbEndingsFirstPersonSingularUCIR', 'PreteriteIrregularVerbEndingsFirstPersonPluralUCIR']
PIVEFPOVUCIR = ['PreteriteIrregularVerbEndingsFirstPersonUCIR']
SingularOrPluralPIVEFPOVUCIR = ((PreteriteIrregularVerbEndingsFirstPersonSingularUCIR, PreteriteIrregularVerbEndingsFirstPersonPluralUCIR),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularUCIR = ['jiste']
PreteriteIrregularVerbEndingsSecondPersonPluralUCIR = ['jisteis']
PreteriteIrregularVerbEndingsSecondPersonUCIR = ['PreteriteIrregularVerbEndingsSecondPersonSingularUCIR', 'PreteriteIrregularVerbEndingsSecondPersonPluralUCIR']
PIVESPOVUCIR = ['PreteriteIrregularVerbEndingsSecondPersonUCIR']
SingularOrPluraPIVESPOVUCIR = ((PreteriteIrregularVerbEndingsSecondPersonSingularUCIR, PreteriteIrregularVerbEndingsSecondPersonPluralUCIR),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularUCIR = ['jo']
PreteriteIrregularVerbEndingsThirdPersonPluralUCIR = ['jeron']
PreteriteIrregularVerbEndingsThirdPersonUCIR = ['PreteriteIrregularVerbEndingsThirdPersonSingularUCIR', 'PreteriteIrregularVerbEndingsThirdPersonPluralUCIR']
PIVETPOVUCIR = ['PreteriteIrregularVerbEndingsThirdPersonUCIR']
SingularOrPluraPIVETPOVUCIR = ((PreteriteIrregularVerbEndingsThirdPersonSingularUCIR, PreteriteIrregularVerbEndingsThirdPersonPluralUCIR),('singular', 'plural'))
