C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma5(2,1)*Gamma5(4,3)
C     
      SUBROUTINE FFFF1_0(F1, F2, F3, F4, COUP,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 F3(*)
      COMPLEX*16 F4(*)
      COMPLEX*16 TMP0
      COMPLEX*16 TMP1
      COMPLEX*16 VERTEX
      TMP0 = (-F4(3)*F3(3)-F4(4)*F3(4)+F4(5)*F3(5)+F4(6)*F3(6))
      TMP1 = (-F2(3)*F1(3)-F2(4)*F1(4)+F2(5)*F1(5)+F2(6)*F1(6))
      VERTEX = COUP*(-CI * TMP0*TMP1)
      END


C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma5(2,1)*Gamma5(4,3)
C     
      SUBROUTINE FFFF1_2_3_4_5_0(F1, F2, F3, F4, COUP1, COUP2, COUP3,
     $  COUP4, COUP5,VERTEX)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP1
      COMPLEX*16 COUP2
      COMPLEX*16 COUP3
      COMPLEX*16 COUP4
      COMPLEX*16 COUP5
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 F3(*)
      COMPLEX*16 F4(*)
      COMPLEX*16 TMP
      COMPLEX*16 VERTEX
      CALL FFFF1_0(F1,F2,F3,F4,COUP1,VERTEX)
      CALL FFFF2_0(F1,F2,F3,F4,COUP2,TMP)
      VERTEX = VERTEX + TMP
      CALL FFFF3_0(F1,F2,F3,F4,COUP3,TMP)
      VERTEX = VERTEX + TMP
      CALL FFFF4_0(F1,F2,F3,F4,COUP4,TMP)
      VERTEX = VERTEX + TMP
      CALL FFFF5_0(F1,F2,F3,F4,COUP5,TMP)
      VERTEX = VERTEX + TMP
      END


