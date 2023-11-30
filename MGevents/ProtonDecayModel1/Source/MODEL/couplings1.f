ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc
c      written by the UFO converter
ccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccccc

      SUBROUTINE COUP1()

      IMPLICIT NONE
      INCLUDE 'model_functions.inc'

      DOUBLE PRECISION PI, ZERO
      PARAMETER  (PI=3.141592653589793D0)
      PARAMETER  (ZERO=0D0)
      INCLUDE 'input.inc'
      INCLUDE 'coupl.inc'
      GC_3 = 2.000000D+00*MDL_COMPLEXI*MDL_GF*MDL_SQRT__2
      GC_5 = (MDL_CAV*MDL_COMPLEXI)/MDL_LAMBDA__EXP__2
      GC_6 = (MDL_CPS*MDL_COMPLEXI)/MDL_LAMBDA__EXP__2
      GC_7 = (MDL_CS*MDL_COMPLEXI)/MDL_LAMBDA__EXP__2
      GC_8 = (MDL_CT*MDL_COMPLEXI)/MDL_LAMBDA__EXP__2
      GC_9 = (MDL_CV*MDL_COMPLEXI)/MDL_LAMBDA__EXP__2
      GC_10 = MDL_COMPLEXI*MDL_TCON
      GC_11 = MDL_COMPLEXI*MDL_TDIP
      END
