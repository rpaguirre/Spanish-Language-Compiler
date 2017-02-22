#This code is the Spanish grammatical rule, specifically  ser and ir.

#Ser
IrregularPreteriteVerbsSer = ['IPVFPOVSer', 'IPVSPOVSer', 'IPVTPOVSer']

IrregularPreteriteVerbsFirstPersonSingularSer = ['fui']
IrregularPreteriteVerbsFirstPersonPluralSer = ['fuimos']
IrregularPreteriteVerbsFirstPersonSer = ['IrregularPreteriteVerbsFirstPersonSingularSer', 'IrregularPreteriteVerbsFirstPersonPluralSer']
IPVFPOVSer = ['IrregularPreteriteVerbsFirstPersonSer']
SingularOrPluralIPVFPOVSer = ((IrregularPreteriteVerbsFirstPersonSingularSer, IrregularPreteriteVerbsFirstPersonPluralSer),('singular', 'plural'))

IrregularPreteriteVerbsSecondPersonSingularSer = ['fuiste']
IrregularPreteriteVerbsSecondPersonPluralSer = ['fuisteis']
IrregularPreteriteVerbsSecondPersonSer = ['IrregularPreteriteVerbsSecondPersonSingularSer', 'IrregularPreteriteVerbsSecondPersonPluralSer']
IPVSPOVSer = ['IrregularPreteriteVerbsSecondPersonSer']
SingularOrPluralIPVSPOVSer = ((IrregularPreteriteVerbsSecondPersonSingularSer, IrregularPreteriteVerbsSecondPersonPluralSer),('singular', 'plural'))

IrregularPreteriteVerbsThirdPersonSingularSer = ['fue']
IrregularPreteriteVerbsThirdPersonPluralSer = ['fueron']
IrregularPreteriteVerbsThirdPersonSer = ['PreteriteIrregularVerbEndingsThirdPersonSingularSer', 'PreteriteIrregularVerbEndingsThirdPersonPluralSer'] 
IPVTPOVSer = ['IrregularPreteriteVerbsThirdPersonSer']
SingularOrPluralIPVTPOVSer = ((IrregularPreteriteVerbsThirdPersonSingularSer, IrregularPreteriteVerbsThirdPersonPluralSer),('singular', 'plural'))

#Ir
IrregularPreteriteVerbsIr = ['IPVFPOVIr', 'IPVSPOVIr', 'IPVTPOVIr']

IrregularPreteriteVerbsFirstPersonSingularIr = ['fui']
IrregularPreteriteVerbsFirstPersonPluralIr = ['fuimos']
IrregularPreteriteVerbsFirstPersonIr = ['IrregularPreteriteVerbsFirstPersonSingularIr', 'IrregularPreteriteVerbsFirstPersonPluralIr']
IPVFPOVIr = ['IrregularPreteriteVerbsFirstPersonIr']
SingularOrPluralIPVFPOVIr = ((IrregularPreteriteVerbsFirstPersonSingularIr, IrregularPreteriteVerbsFirstPersonPluralIr),('singular', 'plural'))

IrregularPreteriteVerbsSecondPersonSingularIr = ['fuiste']
IrregularPreteriteVerbsSecondPersonPluralIr = ['fuisteis']
IrregularPreteriteVerbsSecondPersonIr = ['IrregularPreteriteVerbsSecondPersonSingularIr', 'IrregularPreteriteVerbsSecondPersonPluralIr']
IPVSPOVIr = ['IrregularPreteriteVerbsSecondPersonIr']
SingularOrPluralIPVSPOVIr = ((IrregularPreteriteVerbsSecondPersonSingularIr, IrregularPreteriteVerbsSecondPersonPluralIr),('singular', 'plural'))

IrregularPreteriteVerbsThirdPersonSingularIr = ['fue']
IrregularPreteriteVerbsThirdPersonPluralIr = ['fueron']
IrregularPreteriteVerbsThirdPersonIr = ['PreteriteIrregularVerbEndingsThirdPersonSingularIr', 'PreteriteIrregularVerbEndingsThirdPersonPluralIr'] 
IPVTPOVIr = ['IrregularPreteriteVerbsThirdPersonIr']
SingularOrPluralIPVTPOVIr = ((IrregularPreteriteVerbsThirdPersonSingularIr, IrregularPreteriteVerbsThirdPersonPluralIr),('singular', 'plural'))
