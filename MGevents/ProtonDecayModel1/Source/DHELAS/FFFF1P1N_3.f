C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma5(2,1)*Gamma5(4,3)
C     
      SUBROUTINE FFFF1P1N_3(F1, F2, F4, COUP,F3)
      IMPLICIT NONE
      COMPLEX*16 CI
      PARAMETER (CI=(0D0,1D0))
      COMPLEX*16 COUP
      COMPLEX*16 F1(*)
      COMPLEX*16 F2(*)
      COMPLEX*16 F3(6)
      COMPLEX*16 F4(*)
      COMPLEX*16 TMP2
      TMP2 = (-F2(3)*F1(3)-F2(4)*F1(4)+F2(5)*F1(5)+F2(6)*F1(6))
      F3(3)= COUP*CI * F4(3)*TMP2
      F3(4)= COUP*CI * F4(4)*TMP2
      F3(5)= COUP*(-CI )* F4(5)*TMP2
      F3(6)= COUP*(-CI )* F4(6)*TMP2
      END


C     This File is Automatically generated by ALOHA 
C     The process calculated in this file is: 
C     Gamma5(2,1)*Gamma5(4,3)
C     
      SUBROUTINE FFFF1_2_3_4_5P1N_3(F1, F2, F4, COUP1, COUP2, COUP3,
     $  COUP4, COUP5,F3)
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
      COMPLEX*16 F3(6)
      COMPLEX*16 F4(*)
      COMPLEX*16 FTMP(6)
      INTEGER*4 I
      CALL FFFF1P1N_3(F1,F2,F4,COUP1,F3)
      CALL FFFF2P1N_3(F1,F2,F4,COUP2,FTMP)
      DO I = 3, 6
        F3(I) = F3(I) + FTMP(I)
      ENDDO
      CALL FFFF3P1N_3(F1,F2,F4,COUP3,FTMP)
      DO I = 3, 6
        F3(I) = F3(I) + FTMP(I)
      ENDDO
      CALL FFFF4P1N_3(F1,F2,F4,COUP4,FTMP)
      DO I = 3, 6
        F3(I) = F3(I) + FTMP(I)
      ENDDO
      CALL FFFF5P1N_3(F1,F2,F4,COUP5,FTMP)
      DO I = 3, 6
        F3(I) = F3(I) + FTMP(I)
      ENDDO
      END


