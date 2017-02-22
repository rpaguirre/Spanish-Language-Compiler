#This code is comprised with the Spanish Grammar rules, specifically the rules
#That work with Preterite Regular Verb Endings

PreteriteRegularVerbEndingsPairs = [(1, 'RegularVerbEndingsAR'), (2, 'RegularVerbEndingsER'), (3, 'RegularVerbEndingsIR')]
PreteriteRegularVerbEndingsPairs.sort(key=lambda pair: pair[1])

PreteriteRegularVerbEndings = ['RegularVerbEndingsAR', 'RegularVerbEndingsER', 'RegularVerbEndingsIR']
print("""\
Usage: Preterite Regular Verb Endings Index:
    -To look up endings AR, ER, IR
    -Use 'PreteriteRegularVerbEndings'
    -PREVE, is Preterite Regulare Verb Engdings followed by:
    -FPOV--, is first point of view
    -SPOV--, is second point of view
    -TPOV--, is third point of view
""")

RegularVerbEndingsAR = ['PRVEFPOVAR', 'PRVESPOVAR', 'PRVETPOVAR']
PreteriteRegularVerbEndingsFirstPersonSingularAR = ['e']
PreteriteRegularVerbEndingsFirstPersonPluralAR = ['amos']
PreteriteRegularVerbEndingsFirstPersonAR = [('PreteriteRegularVerbEndingsFirstPersonSingularAR', 'PreteriteRegularVerbEndingsFirstPersonPluralAR')]
PRVEFPOVAR = ['PreteriteRegularVerbEndingsFirstPersonAR']
SingularOrPluralPRVEFPOVAR = ((PreteriteRegularVerbEndingsFirstPersonSingularAR, PreteriteRegularVerbEndingsFirstPersonPluralAR), ('singular', 'plural'))

#Debugged
PreteriteRegularVerbEndingsSecondPersonSingularAR = ['aste']
PreteriteRegularVerbEndingsSecondPersonPluralAR = ['asteis']
PreteriteRegularVerbEndingsSecondPersonAR = [('PreteriteRegularVerbEndingsSecondPersonSingularAR', 'PreteriteRegularVerbEndingsSecondPersonPluralAR')]
PRVESPOVAR = ['PreteriteRegularVerbEndingsSecondPersonAR']
SingularOrPluralPRVESPOVAR = ((PreteriteRegularVerbEndingsSecondPersonSingularAR, PreteriteRegularVerbEndingsSecondPersonPluralAR), ('singular', 'plural'))

#Debugged
PreteriteRegularVerbEndingsThirdPersonSingularAR = ['o']
PreteriteRegularVerbEndingsThirdPersonPluralAR = ['aron']
PreteriteRegularVerbEndingsThirdPersonAR = [('PreteriteRegularVerbEndingsThirdPersonSingularAR', 'PreteriteRegularVerbEndingsThirdPersonPluralAR')]
PRVETPOVAR = ['PreteriteRegularVerbEndingsThirdPersonAR']
SingularOrPluralPRVETPOVAR = ((PreteriteRegularVerbEndingsThirdPersonSingularAR, PreteriteRegularVerbEndingsThirdPersonPluralAR), ('singular', 'plural'))

#Debugged
RegularVerbEndingsER = ['PRVEFPOVER', 'PRVESPOVER', 'PRVETPOVER']
PreteriteRegularVerbEndingsFirstPersonSingularER = ['i']
PreteriteRegularVerbEndingsFirstPersonPluralER = ['imos']
PreteriteRegularVerbEndingsFirstPersonER = [('PreteriteRegularVerbEndingsFirstPersonSingularER', 'PreteriteRegularVerbEndingsFirstPersonPluralER')]
PRVEFPOVER = ['PreteriteRegularVerbEndingsFirstPersonER']
SingularOrPluralPRVEFPOVER = ((PreteriteRegularVerbEndingsFirstPersonSingularER, PreteriteRegularVerbEndingsFirstPersonPluralER), ('singular', 'plural'))

#Debugged
PreteriteRegularVerbEndingsSecondPersonSingularER = ['iste']
PreteriteRegularVerbEndingsSecondPersonPluralER = ['isteis']
PreteriteRegularVerbEndingsSecondPersonER = [('PreteriteRegularVerbEndingsSecondPersonSingularER', 'PreteriteRegularVerbEndingsSecondPersonPluralER')]
PRVESPOVER = ['PreteriteRegularVerbEndingsSecondPersonER']
SingularOrPluralPRVESPOVER = ((PreteriteRegularVerbEndingsSecondPersonSingularER,PreteriteRegularVerbEndingsSecondPersonPluralER), ('singular', 'plural'))

#Debugged
PreteriteRegularVerbEndingsThirdPersonSingularER = ['io']
PreteriteRegularVerbEndingsThirdPersonPluralER = ['ieron']
PreteriteRegularVerbEndingsThirdPersonER = [('PreteriteRegularVerbEndingsThirdPersonSingularER', 'PreteriteRegularVerbEndingsThirdPersonPluralER')]
PRVETPOVER = ['PreteriteRegularVerbEndingsThirdPersonER']
SingularOrPluralPRVETPOVER = ((PreteriteRegularVerbEndingsThirdPersonSingularER, PreteriteRegularVerbEndingsThirdPersonPluralER), ('singular', 'plural'))

#Debugged
RegularVerbEndingsIR = ['PRVEFPOVIR', 'PRVESPOVIR', 'PRVETPOVIR']
PreteriteRegularVerbEndingsFirstPersonSingularIR = ['i']
PreteriteRegularVerbEndingsFirstPersonPluralIR = ['imos']
PreteriteRegularVerbEndingsFirstPersonIR = [('PreteriteRegularVerbEndingsFirstPersonSingularIR', 'PreteriteRegularVerbEndingsFirstPersonPluralIR')]
PRVEFPOVIR = ['PreteriteRegularVerbEndingsFirstPersonIR']
SingularOrPluralPRVEFPOVIR = ((PreteriteRegularVerbEndingsFirstPersonSingularIR, PreteriteRegularVerbEndingsFirstPersonPluralIR), ('singular', 'plural'))

#Debugged
PreteriteRegularVerbEndingsSecondPersonSingularIR = ['iste']
PreteriteRegularVerbEndingsSecondPersonPluralIR = ['isteis']
PreteriteRegularVerbEndingsSecondPersonIR = [('PreteriteRegularVerbEndingsSecondPersonSingularIR', 'PreteriteRegularVerbEndingsSecondPersonPluralIR')]
PRVESPOVIR = ['PreteriteRegularVerbEndingsSecondPersonIR']
SingularOrPluralPRVESPOVIR = ((PreteriteRegularVerbEndingsSecondPersonSingularIR, PreteriteRegularVerbEndingsSecondPersonPluralIR), ('singular', 'plural'))

#Debugged
PreteriteRegularVerbEndingsThirdPersonSingularIR = ['io']
PreteriteRegularVerbEndingsThirdPersonPluralIR = ['ieron']
PreteriteRegularVerbEndingsThirdPersonIR = [('PreteriteRegularVerbEndingsThirdPersonSingularIR', 'PreteriteRegularVerbEndingsThirdPersonPluralIR')]
PRVETPOVIR = ['PreteriteRegularVerbEndingsThirdPersonIR']
SingularOrPluralPRVETPOVIR = ((PreteriteRegularVerbEndingsThirdPersonSingularIR, PreteriteRegularVerbEndingsThirdPersonPluralIR), ('singular', 'plural'))
