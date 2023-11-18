# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Mac OS X x86 (64-bit) (July 24, 2023)
# Date: Fri 17 Nov 2023 18:25:49


from object_library import all_vertices, Vertex
import particles as P
import couplings as C
import lorentz as L


V_1 = Vertex(name = 'V_1',
             particles = [ P.vm__tilde__, P.mu__minus__, P.chi2bar, P.pp ],
             color = [ '1' ],
             lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5 ],
             couplings = {(0,0):C.GC_6,(0,2):C.GC_5,(0,1):C.GC_9,(0,3):C.GC_8,(0,4):C.GC_7})

V_2 = Vertex(name = 'V_2',
             particles = [ P.ppbar, P.chi2, P.mu__plus__, P.vm ],
             color = [ '1' ],
             lorentz = [ L.FFFF1, L.FFFF2, L.FFFF3, L.FFFF4, L.FFFF5 ],
             couplings = {(0,0):C.GC_6,(0,2):C.GC_5,(0,1):C.GC_9,(0,3):C.GC_8,(0,4):C.GC_7})

V_3 = Vertex(name = 'V_3',
             particles = [ P.chi2bar, P.chi1, P.Ap ],
             color = [ '1' ],
             lorentz = [ L.FFV1, L.FFV2 ],
             couplings = {(0,0):C.GC_10,(0,1):C.GC_11})

V_4 = Vertex(name = 'V_4',
             particles = [ P.chi1bar, P.chi2, P.Ap ],
             color = [ '1' ],
             lorentz = [ L.FFV1, L.FFV2 ],
             couplings = {(0,0):C.GC_10,(0,1):C.GC_11})

V_5 = Vertex(name = 'V_5',
             particles = [ P.e__plus__, P.e__minus__, P.Ap ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_4})

V_6 = Vertex(name = 'V_6',
             particles = [ P.e__plus__, P.e__minus__, P.a ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_7 = Vertex(name = 'V_7',
             particles = [ P.mu__plus__, P.mu__minus__, P.a ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_8 = Vertex(name = 'V_8',
             particles = [ P.ta__plus__, P.ta__minus__, P.a ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_1})

V_9 = Vertex(name = 'V_9',
             particles = [ P.ppbar, P.pp, P.a ],
             color = [ '1' ],
             lorentz = [ L.FFV1 ],
             couplings = {(0,0):C.GC_2})

V_10 = Vertex(name = 'V_10',
              particles = [ P.vm__tilde__, P.mu__minus__, P.e__plus__, P.ve ],
              color = [ '1' ],
              lorentz = [ L.FFFF6 ],
              couplings = {(0,0):C.GC_3})

V_11 = Vertex(name = 'V_11',
              particles = [ P.ve__tilde__, P.e__minus__, P.mu__plus__, P.vm ],
              color = [ '1' ],
              lorentz = [ L.FFFF6 ],
              couplings = {(0,0):C.GC_3})

