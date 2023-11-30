# This file was automatically created by FeynRules 2.3.49
# Mathematica version: 13.3.1 for Mac OS X x86 (64-bit) (July 24, 2023)
# Date: Fri 17 Nov 2023 18:25:49


from __future__ import division
from object_library import all_particles, Particle
import parameters as Param

import propagators as Prop

e__minus__ = Particle(pdg_code = 11,
                      name = 'e-',
                      antiname = 'e+',
                      spin = 2,
                      color = 1,
                      mass = Param.Me,
                      width = Param.ZERO,
                      texname = 'e-',
                      antitexname = 'e+',
                      charge = -1,
                      BaryonNumber = 0,
                      LeptonNumber = 1,
                      Qp = 0)

e__plus__ = e__minus__.anti()

mu__minus__ = Particle(pdg_code = 13,
                       name = 'mu-',
                       antiname = 'mu+',
                       spin = 2,
                       color = 1,
                       mass = Param.MMU,
                       width = Param.ZERO,
                       texname = 'mu-',
                       antitexname = 'mu+',
                       charge = -1,
                       BaryonNumber = 0,
                       LeptonNumber = 1,
                       Qp = 0)

mu__plus__ = mu__minus__.anti()

ta__minus__ = Particle(pdg_code = 15,
                       name = 'ta-',
                       antiname = 'ta+',
                       spin = 2,
                       color = 1,
                       mass = Param.MTA,
                       width = Param.ZERO,
                       texname = 'ta-',
                       antitexname = 'ta+',
                       charge = -1,
                       BaryonNumber = 0,
                       LeptonNumber = 1,
                       Qp = 0)

ta__plus__ = ta__minus__.anti()

ve = Particle(pdg_code = 12,
              name = 've',
              antiname = 've~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 've',
              antitexname = 've~',
              charge = 0,
              BaryonNumber = 0,
              LeptonNumber = 1,
              Qp = 0)

ve__tilde__ = ve.anti()

vm = Particle(pdg_code = 14,
              name = 'vm',
              antiname = 'vm~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vm',
              antitexname = 'vm~',
              charge = 0,
              BaryonNumber = 0,
              LeptonNumber = 1,
              Qp = 0)

vm__tilde__ = vm.anti()

vt = Particle(pdg_code = 16,
              name = 'vt',
              antiname = 'vt~',
              spin = 2,
              color = 1,
              mass = Param.ZERO,
              width = Param.ZERO,
              texname = 'vt',
              antitexname = 'vt~',
              charge = 0,
              BaryonNumber = 0,
              LeptonNumber = 1,
              Qp = 0)

vt__tilde__ = vt.anti()

chi1 = Particle(pdg_code = 999901,
                name = 'chi1',
                antiname = 'chi1bar',
                spin = 2,
                color = 1,
                mass = Param.Mchi1,
                width = Param.ZERO,
                texname = 'chi1',
                antitexname = 'chi1bar',
                charge = 0,
                BaryonNumber = 0,
                LeptonNumber = 0,
                Qp = 0)

chi1bar = chi1.anti()

chi2 = Particle(pdg_code = 999902,
                name = 'chi2',
                antiname = 'chi2bar',
                spin = 2,
                color = 1,
                mass = Param.Mchi2,
                width = Param.Wchi2,
                texname = 'chi2',
                antitexname = 'chi2bar',
                charge = 0,
                BaryonNumber = 0,
                LeptonNumber = 0,
                Qp = 0)

chi2bar = chi2.anti()

pp = Particle(pdg_code = 999900,
              name = 'pp',
              antiname = 'ppbar',
              spin = 2,
              color = 1,
              mass = Param.Mp,
              width = Param.ZERO,
              texname = 'pp',
              antitexname = 'ppbar',
              charge = 1,
              BaryonNumber = 1,
              LeptonNumber = 0,
              Qp = 0)

ppbar = pp.anti()

a = Particle(pdg_code = 22,
             name = 'a',
             antiname = 'a',
             spin = 3,
             color = 1,
             mass = Param.ZERO,
             width = Param.ZERO,
             texname = 'a',
             antitexname = 'a',
             charge = 0,
             BaryonNumber = 0,
             LeptonNumber = 0,
             Qp = 0)

Ap = Particle(pdg_code = 999903,
              name = 'Ap',
              antiname = 'Ap',
              spin = 3,
              color = 1,
              mass = Param.MAp,
              width = Param.WAp,
              texname = 'Ap',
              antitexname = 'Ap',
              charge = 0,
              BaryonNumber = 0,
              LeptonNumber = 0,
              Qp = 0)

