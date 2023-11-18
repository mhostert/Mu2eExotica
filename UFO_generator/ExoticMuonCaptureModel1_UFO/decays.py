# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Mac OS X x86 (64-bit) (July 24, 2023)
# Date: Fri 17 Nov 2023 18:25:49


from object_library import all_decays, Decay
import particles as P


Decay_Ap = Decay(name = 'Decay_Ap',
                 particle = P.Ap,
                 partial_widths = {(P.chi1,P.chi2bar):'((4*MAp**2*tcon**2 - 2*Mchi1**2*tcon**2 - (2*Mchi1**4*tcon**2)/MAp**2 + 12*Mchi1*Mchi2*tcon**2 - 2*Mchi2**2*tcon**2 + (4*Mchi1**2*Mchi2**2*tcon**2)/MAp**2 - (2*Mchi2**4*tcon**2)/MAp**2 + 24*MAp**2*Mchi1*tcon*tdip - 24*Mchi1**3*tcon*tdip + 24*MAp**2*Mchi2*tcon*tdip + 24*Mchi1**2*Mchi2*tcon*tdip + 24*Mchi1*Mchi2**2*tcon*tdip - 24*Mchi2**3*tcon*tdip + 8*MAp**4*tdip**2 + 8*MAp**2*Mchi1**2*tdip**2 - 16*Mchi1**4*tdip**2 + 48*MAp**2*Mchi1*Mchi2*tdip**2 + 8*MAp**2*Mchi2**2*tdip**2 + 32*Mchi1**2*Mchi2**2*tdip**2 - 16*Mchi2**4*tdip**2)*cmath.sqrt(MAp**4 - 2*MAp**2*Mchi1**2 + Mchi1**4 - 2*MAp**2*Mchi2**2 - 2*Mchi1**2*Mchi2**2 + Mchi2**4))/(48.*cmath.pi*abs(MAp)**3)',
                                   (P.chi2,P.chi1bar):'((4*MAp**2*tcon**2 - 2*Mchi1**2*tcon**2 - (2*Mchi1**4*tcon**2)/MAp**2 + 12*Mchi1*Mchi2*tcon**2 - 2*Mchi2**2*tcon**2 + (4*Mchi1**2*Mchi2**2*tcon**2)/MAp**2 - (2*Mchi2**4*tcon**2)/MAp**2 + 24*MAp**2*Mchi1*tcon*tdip - 24*Mchi1**3*tcon*tdip + 24*MAp**2*Mchi2*tcon*tdip + 24*Mchi1**2*Mchi2*tcon*tdip + 24*Mchi1*Mchi2**2*tcon*tdip - 24*Mchi2**3*tcon*tdip + 8*MAp**4*tdip**2 + 8*MAp**2*Mchi1**2*tdip**2 - 16*Mchi1**4*tdip**2 + 48*MAp**2*Mchi1*Mchi2*tdip**2 + 8*MAp**2*Mchi2**2*tdip**2 + 32*Mchi1**2*Mchi2**2*tdip**2 - 16*Mchi2**4*tdip**2)*cmath.sqrt(MAp**4 - 2*MAp**2*Mchi1**2 + Mchi1**4 - 2*MAp**2*Mchi2**2 - 2*Mchi1**2*Mchi2**2 + Mchi2**4))/(48.*cmath.pi*abs(MAp)**3)',
                                   (P.e__minus__,P.e__plus__):'((4*gp**2*MAp**2 + 8*gp**2*Me**2)*cmath.sqrt(MAp**4 - 4*MAp**2*Me**2))/(48.*cmath.pi*abs(MAp)**3)'})

Decay_chi2 = Decay(name = 'Decay_chi2',
                   particle = P.chi2,
                   partial_widths = {(P.Ap,P.chi1):'((-4*MAp**2*tcon**2 + 2*Mchi1**2*tcon**2 + (2*Mchi1**4*tcon**2)/MAp**2 - 12*Mchi1*Mchi2*tcon**2 + 2*Mchi2**2*tcon**2 - (4*Mchi1**2*Mchi2**2*tcon**2)/MAp**2 + (2*Mchi2**4*tcon**2)/MAp**2 - 24*MAp**2*Mchi1*tcon*tdip + 24*Mchi1**3*tcon*tdip - 24*MAp**2*Mchi2*tcon*tdip - 24*Mchi1**2*Mchi2*tcon*tdip - 24*Mchi1*Mchi2**2*tcon*tdip + 24*Mchi2**3*tcon*tdip - 8*MAp**4*tdip**2 - 8*MAp**2*Mchi1**2*tdip**2 + 16*Mchi1**4*tdip**2 - 48*MAp**2*Mchi1*Mchi2*tdip**2 - 8*MAp**2*Mchi2**2*tdip**2 - 32*Mchi1**2*Mchi2**2*tdip**2 + 16*Mchi2**4*tdip**2)*cmath.sqrt(MAp**4 - 2*MAp**2*Mchi1**2 + Mchi1**4 - 2*MAp**2*Mchi2**2 - 2*Mchi1**2*Mchi2**2 + Mchi2**4))/(32.*cmath.pi*abs(Mchi2)**3)'})

Decay_chi1 = Decay(name = 'Decay_chi1',
                   particle = P.chi1,
                   partial_widths = {(P.Ap,P.chi2):'((-4*MAp**2*tcon**2 + 2*Mchi1**2*tcon**2 + (2*Mchi1**4*tcon**2)/MAp**2 - 12*Mchi1*Mchi2*tcon**2 + 2*Mchi2**2*tcon**2 - (4*Mchi1**2*Mchi2**2*tcon**2)/MAp**2 + (2*Mchi2**4*tcon**2)/MAp**2 - 24*MAp**2*Mchi1*tcon*tdip + 24*Mchi1**3*tcon*tdip - 24*MAp**2*Mchi2*tcon*tdip - 24*Mchi1**2*Mchi2*tcon*tdip - 24*Mchi1*Mchi2**2*tcon*tdip + 24*Mchi2**3*tcon*tdip - 8*MAp**4*tdip**2 - 8*MAp**2*Mchi1**2*tdip**2 + 16*Mchi1**4*tdip**2 - 48*MAp**2*Mchi1*Mchi2*tdip**2 - 8*MAp**2*Mchi2**2*tdip**2 - 32*Mchi1**2*Mchi2**2*tdip**2 + 16*Mchi2**4*tdip**2)*cmath.sqrt(MAp**4 - 2*MAp**2*Mchi1**2 + Mchi1**4 - 2*MAp**2*Mchi2**2 - 2*Mchi1**2*Mchi2**2 + Mchi2**4))/(32.*cmath.pi*abs(Mchi1)**3)'})

