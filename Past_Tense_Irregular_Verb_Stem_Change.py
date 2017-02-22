#This code is rules, specifically for irregular verbs with stem changes.
PreteriteIrregularVerbEndingsStemChange = ['RegularVerbEndingsAnduv' , 'RegularVerbEndingsCup', 'RegularVerbEndingsEstuv', 'RegularVerbEndingsEstuv', 'RegularVerbEndingsHub', 'RegularVerbEndingsHic', 'RegularVerbEndingsPud', 'RegularVerbEndingsPus', 'RegularVerbEndingsQuis', 'RegularVerbEndingsSup', 'RegularVerbEndingsSup', 'RegularVerbEndingsTuv', 'RegularVerbEndingsVin']

#Anduve
RegularVerbEndingsAnduv = ['PIVEFPOVEAnduv', 'PIVESPOVAnduv', 'PIVETPOVAnduv']

PreteriteIrregularVerbEndingsFirstPersonSingularAnduv = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralAnduv = ['imos']
PreteriteIrregularVerbEndingsFirstPersonAnduv = ['PreteriteIrregularVerbEndingsFirstPersonSingularAnduv', 'PreteriteIrregularVerbEndingsFirstPersonPluralAnduv']
PIVEFPOVAnduv = ['PreteriteIrregularVerbEndingsFirstPersonAnduv']
SingularOrPluralPIVEFPOVAnduv = ((PreteriteIrregularVerbEndingsFirstPersonSingularAnduv, PreteriteIrregularVerbEndingsFirstPersonPluralAnduv),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularAnduv = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralAnduv = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonAnduv = ['PreteriteIrregularVerbEndingsSecondPersonSingularAnduv', 'PreteriteIrregularVerbEndingsSecondPersonPluralAnduv']
PIVESPOVAnduv = ['PreteriteIrregularVerbEndingsSecondPersonAnduv']
SingularOrPluralPIVESPOVAnduv = ((PreteriteIrregularVerbEndingsSecondPersonSingularAnduv, PreteriteIrregularVerbEndingsSecondPersonPluralAnduv),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularAnduv = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralAnduv = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonAnduv = ['PreteriteIrregularVerbEndingsThirdPersonSingularAnduv', 'PreteriteIrregularVerbEndingsThirdPersonPluralAnduv'] 
PIVETPOVAnduv = ['PreteriteIrregularVerbEndingsThirdPersonUCIR']
SingularOrPluralPIVETPOVAnduv = ((PreteriteIrregularVerbEndingsThirdPersonSingularAnduv, PreteriteIrregularVerbEndingsThirdPersonPluralAnduv),('singular', 'plural'))

#Cup
RegularVerbEndingsCup = ['PIVEFPOVECup', 'PIVESPOVCup', 'PIVETPOVCup']

PreteriteIrregularVerbEndingsFirstPersonSingularCup = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralCup = ['imos']
PreteriteIrregularVerbEndingsFirstPersonCup = ['PreteriteIrregularVerbEndingsFirstPersonSingularCup', 'PreteriteIrregularVerbEndingsFirstPersonPluralCup']
PIVEFPOVCup = ['PreteriteIrregularVerbEndingsFirstPersonCup']
SingularOrPluralPIVEFPOVCup = ((PreteriteIrregularVerbEndingsFirstPersonSingularCup, PreteriteIrregularVerbEndingsFirstPersonPluralCup),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularCup = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralCup = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonCup = ['PreteriteIrregularVerbEndingsSecondPersonSingularCup', 'PreteriteIrregularVerbEndingsSecondPersonPluralCup']
PIVESPOVCup = ['PreteriteIrregularVerbEndingsSecondPersonCup']
SingularOrPluralPIVESPOVCup = ((PreteriteIrregularVerbEndingsSecondPersonSingularCup, PreteriteIrregularVerbEndingsSecondPersonPluralCup),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularCup = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralCup = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonCup = ['PreteriteIrregularVerbEndingsThirdPersonSingularCup', 'PreteriteIrregularVerbEndingsThirdPersonPluralCup'] 
PIVETPOVCup = ['PreteriteIrregularVerbEndingsThirdPersonCup']
SingularOrPluralPIVETPOVCup = ((PreteriteIrregularVerbEndingsThirdPersonSingularCup, PreteriteIrregularVerbEndingsThirdPersonPluralCup),('singular', 'plural'))

#Estuve
RegularVerbEndingsEstuv = ['PIVEFPOVEEstuv', 'PIVESPOVEstuv', 'PIVETPOVEstuv']

PreteriteIrregularVerbEndingsFirstPersonSingularEstuv = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralEstuv = ['imos']
PreteriteIrregularVerbEndingsFirstPersonEstuv = ['PreteriteIrregularVerbEndingsFirstPersonSingularEstuv', 'PreteriteIrregularVerbEndingsFirstPersonPluralEstuv']
PIVEFPOVEstuv = ['PreteriteIrregularVerbEndingsFirstPersonEstuv']
SingularOrPluralPIVEFPOVEstuv = ((PreteriteIrregularVerbEndingsFirstPersonSingularEstuv, PreteriteIrregularVerbEndingsFirstPersonPluralEstuv),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularEstuv = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralEstuv = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonEstuv = ['PreteriteIrregularVerbEndingsSecondPersonSingularEstuv', 'PreteriteIrregularVerbEndingsSecondPersonPluralEstuv']
PIVESPOVEstuv = ['PreteriteIrregularVerbEndingsSecondPersonEstuv']
SingularOrPluralPIVESPOVEstuv = ((PreteriteIrregularVerbEndingsSecondPersonSingularEstuv, PreteriteIrregularVerbEndingsSecondPersonPluralEstuv),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularEstuv = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralEstuv = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonEstuv = ['PreteriteIrregularVerbEndingsThirdPersonSingularEstuv', 'PreteriteIrregularVerbEndingsThirdPersonPluralEstuv'] 
PIVETPOVEstuv = ['PreteriteIrregularVerbEndingsThirdPersonEstuv']
SingularOrPluralPIVETPOVEstuv = ((PreteriteIrregularVerbEndingsThirdPersonSingularEstuv, PreteriteIrregularVerbEndingsThirdPersonPluralEstuv),('singular', 'plural'))

#Hube
RegularVerbEndingsHub = ['PIVEFPOVEHub', 'PIVESPOVHub', 'PIVETPOVHub']

PreteriteIrregularVerbEndingsFirstPersonSingularHub = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralHub = ['imos']
PreteriteIrregularVerbEndingsFirstPersonHub = ['PreteriteIrregularVerbEndingsFirstPersonSingularHub', 'PreteriteIrregularVerbEndingsFirstPersonPluralHub']
PIVEFPOVEHub = ['PreteriteIrregularVerbEndingsFirstPersonHub']
SingularOrPluralPIVEFPOVEHub = ((PreteriteIrregularVerbEndingsFirstPersonSingularHub, PreteriteIrregularVerbEndingsFirstPersonPluralHub),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularHub = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralHub = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonHub = ['PreteriteIrregularVerbEndingsSecondPersonSingularHub', 'PreteriteIrregularVerbEndingsSecondPersonPluralHub']
PIVESPOVHub = ['PreteriteIrregularVerbEndingsSecondPersonHub']
SingularOrPluralPIVESPOVHub = ((PreteriteIrregularVerbEndingsSecondPersonSingularHub, PreteriteIrregularVerbEndingsSecondPersonPluralHub),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularHub = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralHub = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonHub = ['PreteriteIrregularVerbEndingsThirdPersonSingularHub', 'PreteriteIrregularVerbEndingsThirdPersonPluralHub'] 
PIVETPOVHub = ['PreteriteIrregularVerbEndingsThirdPersonHub']
SingularOrPluralPIVETPOVHub = ((PreteriteIrregularVerbEndingsThirdPersonSingularHub, PreteriteIrregularVerbEndingsThirdPersonPluralHub),('singular', 'plural'))

#Hice
RegularVerbEndingsHic = ['PIVEFPOVEHic', 'PIVESPOVHic', 'PIVETPOVHic']

PreteriteIrregularVerbEndingsFirstPersonSingularHic = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralHic = ['imos']
PreteriteIrregularVerbEndingsFirstPersonHic = ['PreteriteIrregularVerbEndingsFirstPersonSingularHic', 'PreteriteIrregularVerbEndingsFirstPersonPluralHic']
PIVEFPOVEHic = ['PreteriteIrregularVerbEndingsFirstPersonHic']
SingularOrPluralPIVEFPOVEHic = ((PreteriteIrregularVerbEndingsFirstPersonSingularHic, PreteriteIrregularVerbEndingsFirstPersonPluralHic),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularHic = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralHic = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonHic = ['PreteriteIrregularVerbEndingsSecondPersonSingularHic', 'PreteriteIrregularVerbEndingsSecondPersonPluralHic']
PIVESPOVHic = ['PreteriteIrregularVerbEndingsSecondPersonHic']
SingularOrPluralPIVESPOVHic = ((PreteriteIrregularVerbEndingsSecondPersonSingularHic, PreteriteIrregularVerbEndingsSecondPersonPluralHic),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularHic = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralHic = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonHic = ['PreteriteIrregularVerbEndingsThirdPersonSingularHic', 'PreteriteIrregularVerbEndingsThirdPersonPluralHic'] 
PIVETPOVHic = ['PreteriteIrregularVerbEndingsThirdPersonHic']
SingularOrPluralPIVETPOVHic = ((PreteriteIrregularVerbEndingsThirdPersonSingularHic, PreteriteIrregularVerbEndingsthirdPersonPluralHic),('singular', 'plural'))

#Pude
RegularVerbEndingsPud = ['PIVEFPOVEPud', 'PIVESPOVPud', 'PIVETPOVPud']

PreteriteIrregularVerbEndingsFirstPersonSingularPud = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralPud = ['imos']
PreteriteIrregularVerbEndingsFirstPersonPud = ['PreteriteIrregularVerbEndingsFirstPersonSingularPud', 'PreteriteIrregularVerbEndingsFirstPersonPluralPud']
PIVEFPOVEPud = ['PreteriteIrregularVerbEndingsFirstPersonPud']
SingularOrPluralPIVEFPOVEPud = ((PreteriteIrregularVerbEndingsFirstPersonSingularPud, PreteriteIrregularVerbEndingsFirstPersonPluralPud),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularPud = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralPud = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonPud = ['PreteriteIrregularVerbEndingsSecondPersonSingularPud', 'PreteriteIrregularVerbEndingsSecondPersonPluralPud']
PIVESPOVPud = ['PreteriteIrregularVerbEndingsSecondPersonPud']
SingularOrPluralPIVESPOVPud = ((PreteriteIrregularVerbEndingsSecondPersonSingularPud, PreteriteIrregularVerbEndingsSecondPersonPluralPud),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularPud = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralPud = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonPud = ['PreteriteIrregularVerbEndingsThirdPersonSingularPud', 'PreteriteIrregularVerbEndingsThirdPersonPluralPud'] 
PIVETPOVPud = ['PreteriteIrregularVerbEndingsThirdPersonPud']
SingularOrPluralPIVETPOVPud = ((PreteriteIrregularVerbEndingsThirdPersonSingularPud, PreteriteIrregularVerbEndingsThirdPersonPluralPud),('singular', 'plural'))

#Puse
RegularVerbEndingsPus = ['PIVEFPOVEPus', 'PIVESPOVPus', 'PIVETPOVPus']

PreteriteIrregularVerbEndingsFirstPersonSingularPus = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralPus = ['imos']
PreteriteIrregularVerbEndingsFirstPersonPus = ['PreteriteIrregularVerbEndingsFirstPersonSingularPus', 'PreteriteIrregularVerbEndingsFirstPersonPluralPus']
PIVEFPOVEPus = ['PreteriteIrregularVerbEndingsFirstPersonPus']
SingularOrPluralPIVEFPOVEPus = ((PreteriteIrregularVerbEndingsFirstPersonSingularPus, PreteriteIrregularVerbEndingsFirstPersonPluralPus),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularPus = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralPus = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonPus = ['PreteriteIrregularVerbEndingsSecondPersonSingularPus', 'PreteriteIrregularVerbEndingsSecondPersonPluralPus']
PIVESPOVPus = ['PreteriteIrregularVerbEndingsSecondPersonPus']
SingularOrPluralPIVESPOVPus = ((PreteriteIrregularVerbEndingsSecondPersonSingularPus, PreteriteIrregularVerbEndingsSecondPersonPluralPus),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularPus = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralPus = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonPus = ['PreteriteIrregularVerbEndingsThirdPersonSingularPus', 'PreteriteIrregularVerbEndingsThirdPersonPluralPus'] 
PIVETPOVPus = ['PreteriteIrregularVerbEndingsThirdPersonPus']
SingularOrPluralPIVETPOVPus = ((PreteriteIrregularVerbEndingsThirdPersonSingularPus, PreteriteIrregularVerbEndingsThirdPersonPluralPus),('singular', 'plural'))

#Quise
RegularVerbEndingsQuis = ['PIVEFPOVEQuis', 'PIVESPOVQuis', 'PIVETPOVQuis']

PreteriteIrregularVerbEndingsFirstPersonSingularQuis = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralQuis = ['imos']
PreteriteIrregularVerbEndingsFirstPersonQuis = ['PreteriteIrregularVerbEndingsFirstPersonSingularQuis', 'PreteriteIrregularVerbEndingsFirstPersonPluralQuis']
PIVEFPOVEQuis = ['PreteriteIrregularVerbEndingsFirstPersonQuis']
SingularOrPluralPIVEFPOVEQuis = ((PreteriteIrregularVerbEndingsFirstPersonSingularQuis, PreteriteIrregularVerbEndingsFirstPersonPluralQuis),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularQuis = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralQuis = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonQuis = ['PreteriteIrregularVerbEndingsSecondPersonSingularQuis', 'PreteriteIrregularVerbEndingsSecondPersonPluralQuis']
PIVESPOVQuis = ['PreteriteIrregularVerbEndingsSecondPersonQuis']
SingularOrPluralPIVESPOVQuis = ((PreteriteIrregularVerbEndingsSecondPersonSingularQuis, PreteriteIrregularVerbEndingsSecondPersonPluralQuis),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularQuis = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralQuis = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonQuis = ['PreteriteIrregularVerbEndingsThirdPersonSingularQuis', 'PreteriteIrregularVerbEndingsThirdPersonPluralQuis'] 
PIVETPOVQuis = ['PreteriteIrregularVerbEndingsThirdPersonQuis']
SingularOrPluralPIVETPOVQuis = ((PreteriteIrregularVerbEndingsThirdPersonSingularQuis, PreteriteIrregularVerbEndingsThirdPersonPluralQuis),('singular', 'plural'))

#Supe
RegularVerbEndingsSup = ['PIVEFPOVESup', 'PIVESPOVSup', 'PIVETPOVSup']

PreteriteIrregularVerbEndingsFirstPersonSingularSup = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralSup = ['imos']
PreteriteIrregularVerbEndingsFirstPersonSup = ['PreteriteIrregularVerbEndingsFirstPersonSingularSup', 'PreteriteIrregularVerbEndingsFirstPersonPluralSup']
PIVEFPOVESup = ['PreteriteIrregularVerbEndingsFirstPersonSup']
SingularOrPluralPIVEFPOVESup = ((PreteriteIrregularVerbEndingsFirstPersonSingularSup, PreteriteIrregularVerbEndingsFirstPersonPluralSup),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularSup = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralSup = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonSup = ['PreteriteIrregularVerbEndingsSecondPersonSingularSup', 'PreteriteIrregularVerbEndingsSecondPersonPluralSup']
PIVESPOVSup = ['PreteriteIrregularVerbEndingsSecondPersonSup']
SingularOrPluralPIVESPOVSup = ((PreteriteIrregularVerbEndingsSecondPersonSingularSup, PreteriteIrregularVerbEndingsSecondPersonPluralSup),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularSup = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralSup = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonSup = ['PreteriteIrregularVerbEndingsThirdPersonSingularSup', 'PreteriteIrregularVerbEndingsThirdPersonPluralSup'] 
PIVETPOVSup = ['PreteriteIrregularVerbEndingsThirdPersonSup']
SingularOrPluralPIVETPOVSup = ((PreteriteIrregularVerbEndingsThirdPersonSingularSup, PreteriteIrregularVerbEndingsThirdPersonPluralSup),('singular', 'plural'))

#Tuve
RegularVerbEndingsTuv = ['PIVEFPOVETuv', 'PIVESPOVTuv', 'PIVETPOVTuv']

PreteriteIrregularVerbEndingsFirstPersonSingularTuv = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralTuv = ['imos']
PreteriteIrregularVerbEndingsFirstPersonTuv = ['PreteriteIrregularVerbEndingsFirstPersonSingularTuv', 'PreteriteIrregularVerbEndingsFirstPersonPluralTuv']
PIVEFPOVETuv = ['PreteriteIrregularVerbEndingsFirstPersonTuv']
SingularOrPluralPIVEFPOVETuv = ((PreteriteIrregularVerbEndingsFirstPersonSingularTuv, PreteriteIrregularVerbEndingsFirstPersonPluralTuv),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularTuv = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralTuv = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonTuv = ['PreteriteIrregularVerbEndingsSecondPersonSingularTuv', 'PreteriteIrregularVerbEndingsSecondPersonPluralTuv']
PIVESPOVTuv = ['PreteriteIrregularVerbEndingsSecondPersonTuv']
SingularOrPluralPIVESPOVTuv = ((PreteriteIrregularVerbEndingsSecondPersonSingularTuv, PreteriteIrregularVerbEndingsSecondPersonPluralTuv),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularTuv = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralTuv = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonTuv = ['PreteriteIrregularVerbEndingsThirdPersonSingularTuv', 'PreteriteIrregularVerbEndingsThirdPersonPluralTuv'] 
PIVETPOVTuv = ['PreteriteIrregularVerbEndingsThirdPersonTuv']
SingularOrPluralPIVETPOVTuv = ((PreteriteIrregularVerbEndingsThirdPersonSingularTuv, PreteriteIrregularVerbEndingsThirdPersonPluralTuv),('singular', 'plural'))

#Vine
RegularVerbEndingsVin = ['PIVEFPOVEVin', 'PIVESPOVVin', 'PIVETPOVVin']

PreteriteIrregularVerbEndingsFirstPersonSingularVin = ['e']
PreteriteIrregularVerbEndingsFirstPersonPluralVin = ['imos']
PreteriteIrregularVerbEndingsFirstPersonVin = ['PreteriteIrregularVerbEndingsFirstPersonSingularVin', 'PreteriteIrregularVerbEndingsFirstPersonPluralVin']
PIVEFPOVEVin = ['PreteriteIrregularVerbEndingsFirstPersonVin']
SingularOrPluralPIVEFPOVEVin = ((PreteriteIrregularVerbEndingsFirstPersonSingularVin, PreteriteIrregularVerbEndingsFirstPersonPluralVin),('singular', 'plural'))

PreteriteIrregularVerbEndingsSecondPersonSingularVin = ['iste']
PreteriteIrregularVerbEndingsSecondPersonPluralVin = ['isteis']
PreteriteIrregularVerbEndingsSecondPersonVin = ['PreteriteIrregularVerbEndingsSecondPersonSingularVin', 'PreteriteIrregularVerbEndingsSecondPersonPluralVin']
PIVESPOVVin = ['PreteriteIrregularVerbEndingsSecondPersonVin']
SingularOrPluralPIVESPOVVin = ((PreteriteIrregularVerbEndingsSecondPersonSingularVin, PreteriteIrregularVerbEndingsSecondPersonPluralVin),('singular', 'plural'))

PreteriteIrregularVerbEndingsThirdPersonSingularVin = ['o']
PreteriteIrregularVerbEndingsThirdPersonPluralVin = ['ieron']
PreteriteIrregularVerbEndingsThirdPersonVin = ['PreteriteIrregularVerbEndingsThirdPersonSingularVin', 'PreteriteIrregularVerbEndingsThirdPersonPluralVin'] 
PIVETPOVVin = ['PreteriteIrregularVerbEndingsThirdPersonVin']
SingularOrPluralPIVETPOVVin = ((PreteriteIrregularVerbEndingsThirdPersonSingularVin, PreteriteIrregularVerbEndingsThirdPersonPluralVin),('singular', 'plural'))
