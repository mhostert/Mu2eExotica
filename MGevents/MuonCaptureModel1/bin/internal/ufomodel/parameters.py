# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Mac OS X x86 (64-bit) (July 24, 2023)
# Date: Fri 17 Nov 2023 18:25:49



from object_library import all_parameters, Parameter


from function_library import complexconjugate, re, im, csc, sec, acsc, asec, cot

# This is a default parameter object representing 0.
ZERO = Parameter(name = 'ZERO',
                 nature = 'internal',
                 type = 'real',
                 value = '0.0',
                 texname = '0')

# User-defined parameters.
epsilon = Parameter(name = 'epsilon',
                    nature = 'external',
                    type = 'real',
                    value = 0.001,
                    texname = '\\epsilon',
                    lhablock = 'BSMINPUTS',
                    lhacode = [ 1 ])

Lambda = Parameter(name = 'Lambda',
                   nature = 'external',
                   type = 'real',
                   value = 1,
                   texname = '\\text{Lambda}',
                   lhablock = 'BSMINPUTS',
                   lhacode = [ 2 ])

cS = Parameter(name = 'cS',
               nature = 'external',
               type = 'real',
               value = 1,
               texname = '\\text{cS}',
               lhablock = 'BSMINPUTS',
               lhacode = [ 3 ])

cPS = Parameter(name = 'cPS',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = '\\text{cPS}',
                lhablock = 'BSMINPUTS',
                lhacode = [ 4 ])

cV = Parameter(name = 'cV',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = '\\text{cV}',
               lhablock = 'BSMINPUTS',
               lhacode = [ 5 ])

cAV = Parameter(name = 'cAV',
                nature = 'external',
                type = 'real',
                value = 0,
                texname = '\\text{cAV}',
                lhablock = 'BSMINPUTS',
                lhacode = [ 6 ])

cT = Parameter(name = 'cT',
               nature = 'external',
               type = 'real',
               value = 0,
               texname = '\\text{cT}',
               lhablock = 'BSMINPUTS',
               lhacode = [ 7 ])

tdip = Parameter(name = 'tdip',
                 nature = 'external',
                 type = 'real',
                 value = 0,
                 texname = '\\text{tdip}',
                 lhablock = 'BSMINPUTS',
                 lhacode = [ 8 ])

tcon = Parameter(name = 'tcon',
                 nature = 'external',
                 type = 'real',
                 value = 1,
                 texname = '\\text{tcon}',
                 lhablock = 'BSMINPUTS',
                 lhacode = [ 9 ])

aEM = Parameter(name = 'aEM',
                nature = 'external',
                type = 'real',
                value = 0.0072992700729927005,
                texname = '\\text{aEM}',
                lhablock = 'SMINPUTS',
                lhacode = [ 1 ])

GF = Parameter(name = 'GF',
               nature = 'external',
               type = 'real',
               value = 0.00001166,
               texname = '\\text{GF}',
               lhablock = 'SMINPUTS',
               lhacode = [ 2 ])

Me = Parameter(name = 'Me',
               nature = 'external',
               type = 'real',
               value = 0.000511,
               texname = '\\text{Me}',
               lhablock = 'MASS',
               lhacode = [ 11 ])

MMU = Parameter(name = 'MMU',
                nature = 'external',
                type = 'real',
                value = 0.10566,
                texname = '\\text{MMU}',
                lhablock = 'MASS',
                lhacode = [ 13 ])

MTA = Parameter(name = 'MTA',
                nature = 'external',
                type = 'real',
                value = 1.777,
                texname = '\\text{MTA}',
                lhablock = 'MASS',
                lhacode = [ 15 ])

Mchi1 = Parameter(name = 'Mchi1',
                  nature = 'external',
                  type = 'real',
                  value = 0.9,
                  texname = '\\text{Mchi1}',
                  lhablock = 'MASS',
                  lhacode = [ 999901 ])

Mchi2 = Parameter(name = 'Mchi2',
                  nature = 'external',
                  type = 'real',
                  value = 1.02,
                  texname = '\\text{Mchi2}',
                  lhablock = 'MASS',
                  lhacode = [ 999902 ])

Mp = Parameter(name = 'Mp',
               nature = 'external',
               type = 'real',
               value = 0.93827,
               texname = '\\text{Mp}',
               lhablock = 'MASS',
               lhacode = [ 999900 ])

MAp = Parameter(name = 'MAp',
                nature = 'external',
                type = 'real',
                value = 0.02,
                texname = '\\text{MAp}',
                lhablock = 'MASS',
                lhacode = [ 999903 ])

Wchi2 = Parameter(name = 'Wchi2',
                  nature = 'external',
                  type = 'real',
                  value = 0.001,
                  texname = '\\text{Wchi2}',
                  lhablock = 'DECAY',
                  lhacode = [ 999902 ])

WAp = Parameter(name = 'WAp',
                nature = 'external',
                type = 'real',
                value = 0.001,
                texname = '\\text{WAp}',
                lhablock = 'DECAY',
                lhacode = [ 999903 ])

ee = Parameter(name = 'ee',
               nature = 'internal',
               type = 'real',
               value = '2*cmath.sqrt(aEM)*cmath.sqrt(cmath.pi)',
               texname = 'e')

gp = Parameter(name = 'gp',
               nature = 'internal',
               type = 'real',
               value = 'ee*epsilon',
               texname = '\\text{gp}')

