C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma(-2,-4,3)*Gamma(-2,-3,1)*Gamma(-1,2,-3)*Gamma(-1,4,-4)
C     
      SUBROUTINE FFFF4P1N_4(F1, F2, F3, COUP,F4)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 F3(*)
      COMPLEX*16 F4(6)
      F4(3)= COUP*(-8D0 * CI)*(F3(3)*1D0/2D0*(+2D0*(F2(4)*F1(4))+F2(5)
     $ *F1(5)+F2(6)*F1(6))-F3(4)*F2(4)*F1(3))
      F4(4)= COUP*(-8D0 * CI)*(F3(4)*1D0/2D0*(+2D0*(F2(3)*F1(3))+F2(5)
     $ *F1(5)+F2(6)*F1(6))-F3(3)*F2(3)*F1(4))
      F4(5)= COUP*(-4D0 * CI)*(F3(5)*(F2(3)*F1(3)+F2(4)*F1(4)+2D0
     $ *(F2(6)*F1(6)))-2D0*(F3(6)*F2(6)*F1(5)))
      F4(6)= COUP*(-4D0 * CI)*(F3(6)*(F2(3)*F1(3)+F2(4)*F1(4)+2D0
     $ *(F2(5)*F1(5)))-2D0*(F3(5)*F2(5)*F1(6)))
      END

