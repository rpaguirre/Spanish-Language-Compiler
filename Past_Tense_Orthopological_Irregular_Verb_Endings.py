#This code consists of the Spanish grammar, specifically orthopological 
#Irregular verb endings.

OrthopologicalIrregularVerbEndingsPairs = [(1, 'OrthopologicalIrregularVerbEndingsCAR'), (2, 'OrthopologicalIrregularVerbEndingsGAR'), (3, 'OrthopologicalIrregularVerbEndingsZAR')]
OrthopologicalIrregularVerbEndingsPairs.sort(key=lambda pair: pair[1])

PreteriteRegularVerbEndings = ['OrthopologicalIrregularVerbEndingsCAR', 'OrthopologicalIrregularVerbEndingsGAR', 'OrthopologicalIrregularVerbEndingsGAR']
print("""\
Usage: Preterite Regular Verb Endings Index:
    -To look up endings CAR, GAR, ZAR
    -Use 'PreteriteRegularVerbEndings'
    -OIVE, is Orthopological Irregular Verb Endings followed by:
    -FPOV--, is first point of view
    -SPOV--, is second point of view
    -TPOV--, is third point of view
""")


#-car c -> qu
OrthopologicalIrregularVerbEndingsCAR = ['OIVEFPOVCAR', 'OIVESPOVCAR', 'OIVETPOVCAR']
OrthopologicalIrregularVerbEndingsFirstPersonSingularCAR = ['qu' + 'e']
OrthopologicalIrregularVerbEndingsFirstPersonPluralCAR = ['amos']
OrthopologicalIrregularVerbEndingsFirstPersonCAR = ['PreteriteIrregularVerbEndingsFirstPersonSingularCAR', 'PreteriteIrregularVerbEndingsFirstPersonPluralCAR']
OIVEFPOVCAR = ['OrthopologicalIrregularVerbEndingsFirstPersonAnduvCAR']
SingularOrPluralOIVEFPOVCAR = ((OrthopologicalIrregularVerbEndingsFirstPersonSingularCAR, OrthopologicalIrregularVerbEndingsFirstPersonPluralCAR),('singular', 'plural'))

OrthopologicalIrregularVerbEndingsSecondPersonSingularCAR = ['aste']
OrthopologicalIrregularVerbEndingsSecondPersonPluralCAR = ['asteis']
OrthopologicalIrregularVerbEndingsSecondPersonCAR = [('OrthopologicalIrregularVerbEndingsSecondPersonSingularCAR', 'OrthopologicalIrregularVerbEndingsSecondPersonPluralCAR')]
OIVESPOVCAR = ['PreteriteRegularVerbEndingsSecondPersonCAR']
SingularOrPluralOIVESPOVCAR = ((OrthopologicalIrregularVerbEndingsSecondPersonSingularCAR, OrthopologicalIrregularVerbEndingsSecondPersonPluralCAR), ('singular', 'plural'))

OrthopologicalIrregularVerbEndingsThirdPersonSingularCAR = ['o']
OrthopologicalIrregularVerbEndingsThirdPersonPluralCAR = ['aron']
OrthopologicalIrregularVerbEndingsThirdPersonCAR = [('OrthopologicalIrregularVerbEndingsThirdPersonSingularCAR', 'OrthopologicalIrregularVerbEndingsThirdPersonPluralCAR')]
OIVETPOVCAR = ['PreteriteRegularVerbEndingsThirdPersonCAR']
SingularOrPluralOIVETPOVCAR = ((PreteriteRegularVerbEndingsThirdPersonSingularCAR, PreteriteRegularVerbEndingsThirdPersonPluralCAR), ('singular', 'plural'))

#-gar g -> gu
OrthopologicalIrregularVerbEndingsGAR = ['OIVEFPOVGAR', 'OIVESPOVGAR', 'OIVETPOVGAR']
OrthopologicalIrregularVerbEndingsFirstPersonSingularGAR = ['gu' + 'e']
OrthopologicalIrregularVerbEndingsFirstPersonPluralGAR = ['amos']
OrthopologicalIrregularVerbEndingsFirstPersonGAR = ['PreteriteIrregularVerbEndingsFirstPersonSingularGAR', 'PreteriteIrregularVerbEndingsFirstPersonPluralGAR']
OIVEFPOVGAR = ['OrthopologicalIrregularVerbEndingsFirstPersonAnduvGAR']
SingularOrPluralOIVEFPOVGAR = ((OrthopologicalIrregularVerbEndingsFirstPersonSingularGAR, OrthopologicalIrregularVerbEndingsFirstPersonPluralGAR),('singular', 'plural'))

OrthopologicalIrregularVerbEndingsSecondPersonSingularGAR = ['aste']
OrthopologicalIrregularVerbEndingsSecondPersonPluralGAR = ['asteis']
OrthopologicalIrregularVerbEndingsSecondPersonGAR = [('OrthopologicalIrregularVerbEndingsSecondPersonSingularGAR', 'OrthopologicalIrregularVerbEndingsSecondPersonPluralGAR')]
OIVESPOVGAR = ['PreteriteRegularVerbEndingsSecondPersonGAR']
SingularOrPluralOIVESPOVGAR = ((OrthopologicalIrregularVerbEndingsSecondPersonSingularGAR, OrthopologicalIrregularVerbEndingsSecondPersonPluralGAR), ('singular', 'plural'))

OrthopologicalIrregularVerbEndingsThirdPersonSingularGAR = ['o']
OrthopologicalIrregularVerbEndingsThirdPersonPluralGAR = ['aron']
OrthopologicalIrregularVerbEndingsThirdPersonGAR = [('OrthopologicalIrregularVerbEndingsThirdPersonSingularGAR', 'OrthopologicalIrregularVerbEndingsThirdPersonPluralGAR')]
OIVETPOVGAR = ['PreteriteRegularVerbEndingsThirdPersonCAR']
SingularOrPluralPRVETPOVGAR = ((PreteriteRegularVerbEndingsThirdPersonSingularGAR, PreteriteRegularVerbEndingsThirdPersonPluralGAR), ('singular', 'plural'))

#-zar z -> c
OrthopologicalIrregularVerbEndingsZAR = ['OIVEFPOVZAR', 'OIVESPOVZAR', 'OIVETPOVZAR']
OrthopologicalIrregularVerbEndingsFirstPersonSingularZAR = ['c' + 'e']
OrthopologicalIrregularVerbEndingsFirstPersonPluralZAR = ['amos']
OrthopologicalIrregularVerbEndingsFirstPersonZAR = ['PreteriteIrregularVerbEndingsFirstPersonSingularZAR', 'PreteriteIrregularVerbEndingsFirstPersonPluralZAR']
OIVEFPOVZAR = ['OrthopologicalIrregularVerbEndingsFirstPersonAnduvZAR']
SingularOrPluralOIVEFPOVZAR = ((OrthopologicalIrregularVerbEndingsFirstPersonSingularZAR, OrthopologicalIrregularVerbEndingsFirstPersonPluralZAR),('singular', 'plural'))

OrthopologicalIrregularVerbEndingsSecondPersonSingularZAR = ['aste']
OrthopologicalIrregularVerbEndingsSecondPersonPluralZAR = ['asteis']
OrthopologicalIrregularVerbEndingsSecondPersonZAR = [('OrthopologicalIrregularVerbEndingsSecondPersonSingularZAR', 'OrthopologicalIrregularVerbEndingsSecondPersonPluralZAR')]
OIVESPOVZAR = ['PreteriteRegularVerbEndingsSecondPersonZAR']
SingularOrPluralOIVESPOVZAR = ((OrthopologicalIrregularVerbEndingsSecondPersonSingularZAR, OrthopologicalIrregularVerbEndingsSecondPersonPluralZAR), ('singular', 'plural'))

OrthopologicalIrregularVerbEndingsThirdPersonSingularZAR = ['o']
OrthopologicalIrregularVerbEndingsThirdPersonPluralZAR = ['aron']
OrthopologicalIrregularVerbEndingsThirdPersonZAR = [('OrthopologicalIrregularVerbEndingsThirdPersonSingularZAR', 'OrthopologicalIrregularVerbEndingsThirdPersonPluralZAR')]
OIVETPOVZAR = ['PreteriteRegularVerbEndingsThirdPersonZAR']
SingularOrPluralPRVETPOVZAR = ((PreteriteRegularVerbEndingsThirdPersonSingularZAR, PreteriteRegularVerbEndingsThirdPersonPluralZAR), ('singular', 'plural'))
