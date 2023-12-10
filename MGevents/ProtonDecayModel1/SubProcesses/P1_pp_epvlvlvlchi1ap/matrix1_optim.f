      SUBROUTINE SMATRIX1(P,ANS)
C     
C     Generated by MadGraph5_aMC@NLO v. 3.5.0, 2023-05-12
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     MadGraph5_aMC@NLO for Madevent Version
C     
C     Returns amplitude squared summed/avg over colors
C     and helicities
C     for the point in phase space P(0:3,NEXTERNAL)
C     
C     Process: pp > e+ vm~ ve vm chi1 ap QEDp<=5 @1
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      Include 'genps.inc'
      Include 'maxconfigs.inc'
      Include 'nexternal.inc'
      Include 'maxamps.inc'
      INTEGER                 NCOMB         
      PARAMETER (             NCOMB=48)
      INTEGER    NGRAPHS
      PARAMETER (NGRAPHS=1) 
      INTEGER    NDIAGS
      PARAMETER (NDIAGS=1) 
      INTEGER    THEL
      PARAMETER (THEL=2*NCOMB)
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL),ANS
C     
C     LOCAL VARIABLES 
C     
      INTEGER CONFSUB(MAXSPROC,LMAXCONFIGS)
      INCLUDE 'config_subproc_map.inc'
      INTEGER NHEL(NEXTERNAL,NCOMB)
      REAL*8 T
      REAL*8 R,SUMHEL,TS(NCOMB)
      INTEGER I,IDEN
      INTEGER JC(NEXTERNAL),II
      REAL*8 XTOT
      INTEGER  J, JJ

      double precision get_channel_cut
      external get_channel_cut

C     
C     GLOBAL VARIABLES
C     
      DOUBLE PRECISION AMP2(MAXAMPS), JAMP2(0:MAXFLOW)
      COMMON/TO_AMPS/  AMP2,       JAMP2


C     
C     INFORMATION TO WRITE THE HELICITY IN THE EVENT --not memory
C      efficient--
C     
      CHARACTER*101         HEL_BUFF
      COMMON/TO_HELICITY/  HEL_BUFF

      INTEGER NB_SPIN_STATE_in(2)
      common /nb_hel_state/ nb_spin_state_in

      REAL*8 POL(2)

      COMMON/TO_POLARIZATION/ POL
      double precision tmin_for_channel
      integer sde_strat    !  1 means standard single diagram enhancement strategy,
C     2 means approximation by the	denominator of the propagator
      common/TO_CHANNEL_STRAT/tmin_for_channel,	sde_strat

      INTEGER          ISUM_HEL
      LOGICAL                    MULTI_CHANNEL
      COMMON/TO_MATRIX/ISUM_HEL, MULTI_CHANNEL
      INTEGER MAPCONFIG(0:LMAXCONFIGS), ICONFIG
      COMMON/TO_MCONFIGS/MAPCONFIG, ICONFIG
      INTEGER SUBDIAG(MAXSPROC),IB(2)
      COMMON/TO_SUB_DIAG/SUBDIAG,IB
      
      DATA (NHEL(I,1),I=1,7) / 1, 1,-1, 1,-1,-1,-1/
      DATA (NHEL(I,2),I=1,7) / 1, 1,-1, 1,-1,-1, 0/
      DATA (NHEL(I,3),I=1,7) / 1, 1,-1, 1,-1,-1, 1/
      DATA (NHEL(I,4),I=1,7) / 1, 1,-1, 1,-1, 1,-1/
      DATA (NHEL(I,5),I=1,7) / 1, 1,-1, 1,-1, 1, 0/
      DATA (NHEL(I,6),I=1,7) / 1, 1,-1, 1,-1, 1, 1/
      DATA (NHEL(I,7),I=1,7) / 1, 1,-1, 1, 1,-1,-1/
      DATA (NHEL(I,8),I=1,7) / 1, 1,-1, 1, 1,-1, 0/
      DATA (NHEL(I,9),I=1,7) / 1, 1,-1, 1, 1,-1, 1/
      DATA (NHEL(I,10),I=1,7) / 1, 1,-1, 1, 1, 1,-1/
      DATA (NHEL(I,11),I=1,7) / 1, 1,-1, 1, 1, 1, 0/
      DATA (NHEL(I,12),I=1,7) / 1, 1,-1, 1, 1, 1, 1/
      DATA (NHEL(I,13),I=1,7) / 1,-1,-1, 1,-1,-1,-1/
      DATA (NHEL(I,14),I=1,7) / 1,-1,-1, 1,-1,-1, 0/
      DATA (NHEL(I,15),I=1,7) / 1,-1,-1, 1,-1,-1, 1/
      DATA (NHEL(I,16),I=1,7) / 1,-1,-1, 1,-1, 1,-1/
      DATA (NHEL(I,17),I=1,7) / 1,-1,-1, 1,-1, 1, 0/
      DATA (NHEL(I,18),I=1,7) / 1,-1,-1, 1,-1, 1, 1/
      DATA (NHEL(I,19),I=1,7) / 1,-1,-1, 1, 1,-1,-1/
      DATA (NHEL(I,20),I=1,7) / 1,-1,-1, 1, 1,-1, 0/
      DATA (NHEL(I,21),I=1,7) / 1,-1,-1, 1, 1,-1, 1/
      DATA (NHEL(I,22),I=1,7) / 1,-1,-1, 1, 1, 1,-1/
      DATA (NHEL(I,23),I=1,7) / 1,-1,-1, 1, 1, 1, 0/
      DATA (NHEL(I,24),I=1,7) / 1,-1,-1, 1, 1, 1, 1/
      DATA (NHEL(I,25),I=1,7) /-1, 1,-1, 1,-1,-1,-1/
      DATA (NHEL(I,26),I=1,7) /-1, 1,-1, 1,-1,-1, 0/
      DATA (NHEL(I,27),I=1,7) /-1, 1,-1, 1,-1,-1, 1/
      DATA (NHEL(I,28),I=1,7) /-1, 1,-1, 1,-1, 1,-1/
      DATA (NHEL(I,29),I=1,7) /-1, 1,-1, 1,-1, 1, 0/
      DATA (NHEL(I,30),I=1,7) /-1, 1,-1, 1,-1, 1, 1/
      DATA (NHEL(I,31),I=1,7) /-1, 1,-1, 1, 1,-1,-1/
      DATA (NHEL(I,32),I=1,7) /-1, 1,-1, 1, 1,-1, 0/
      DATA (NHEL(I,33),I=1,7) /-1, 1,-1, 1, 1,-1, 1/
      DATA (NHEL(I,34),I=1,7) /-1, 1,-1, 1, 1, 1,-1/
      DATA (NHEL(I,35),I=1,7) /-1, 1,-1, 1, 1, 1, 0/
      DATA (NHEL(I,36),I=1,7) /-1, 1,-1, 1, 1, 1, 1/
      DATA (NHEL(I,37),I=1,7) /-1,-1,-1, 1,-1,-1,-1/
      DATA (NHEL(I,38),I=1,7) /-1,-1,-1, 1,-1,-1, 0/
      DATA (NHEL(I,39),I=1,7) /-1,-1,-1, 1,-1,-1, 1/
      DATA (NHEL(I,40),I=1,7) /-1,-1,-1, 1,-1, 1,-1/
      DATA (NHEL(I,41),I=1,7) /-1,-1,-1, 1,-1, 1, 0/
      DATA (NHEL(I,42),I=1,7) /-1,-1,-1, 1,-1, 1, 1/
      DATA (NHEL(I,43),I=1,7) /-1,-1,-1, 1, 1,-1,-1/
      DATA (NHEL(I,44),I=1,7) /-1,-1,-1, 1, 1,-1, 0/
      DATA (NHEL(I,45),I=1,7) /-1,-1,-1, 1, 1,-1, 1/
      DATA (NHEL(I,46),I=1,7) /-1,-1,-1, 1, 1, 1,-1/
      DATA (NHEL(I,47),I=1,7) /-1,-1,-1, 1, 1, 1, 0/
      DATA (NHEL(I,48),I=1,7) /-1,-1,-1, 1, 1, 1, 1/
      DATA IDEN/ 2/

C     ----------
C     BEGIN CODE
C     ----------

      DO I=1,NEXTERNAL
        JC(I) = +1
      ENDDO

      IF (multi_channel) THEN
        DO I=1,NDIAGS
          AMP2(I)=0D0
        ENDDO
        JAMP2(0)=1
        DO I=1,INT(JAMP2(0))
          JAMP2(I)=0D0
        ENDDO
      ENDIF
      ANS = 0D0
      WRITE(HEL_BUFF,'(20I5)') (0,I=1,NEXTERNAL)
C     Kiran please check if you need this:    
      DO I=1,NCOMB
        TS(I)=0d0
      ENDDO

      call MATRIX1(P ,JC(1), TS)
      DO I=1,NCOMB     
        T=TS(I)  
        DO JJ=1,nincoming
          IF(POL(JJ).NE.1d0.AND.NHEL(JJ,I).EQ.INT(SIGN(1d0,POL(JJ))))
     $      THEN
            T=T*ABS(POL(JJ))*NB_SPIN_STATE_IN(JJ)/2d0    !  NB_SPIN_STATE(JJ)/2d0 is added for polarised beam
          ELSE IF(POL(JJ).NE.1d0)THEN
            T=T*(2d0-ABS(POL(JJ)))*NB_SPIN_STATE_IN(JJ)/2d0
          ENDIF
        ENDDO
        ANS=ANS+DABS(T)
        TS(I)=T
      ENDDO

      IF (ANS.ne.0d0) THEN
        CALL RANMAR(R)
        SUMHEL=0d0
        DO I=1,NCOMB
          SUMHEL=SUMHEL+DABS(TS(I))/ANS
          IF(R.LT.SUMHEL)THEN
            WRITE(HEL_BUFF,'(20i5)')(NHEL(II,I),II=1,NEXTERNAL)
C           Set right sign for ANS, based on sign of chosen helicity
            ANS=DSIGN(ANS,TS(I))
            GOTO 10
          ENDIF
        ENDDO
 10     CONTINUE   
      ENDIF
      IF (MULTI_CHANNEL) THEN
        XTOT=0D0
        DO I=1,LMAXCONFIGS
          J = CONFSUB(1, I)
          if (J.ne.0)then
            if (sde_strat.eq.1)then
              AMP2(J) = AMP2(J) * GET_CHANNEL_CUT(P, I)
            else
              AMP2(J) = GET_CHANNEL_CUT(P, I)
            endif
            XTOT=XTOT+AMP2(J)

          endif
        ENDDO
        IF (XTOT.NE.0D0) THEN
          ANS=ANS*AMP2(SUBDIAG(1))/XTOT
        ELSE IF(ANS.ne.0d0) THEN
          write(*,*) 'Problem in the multi-channeling. All amp2 are'
     $     //' zero but not the total matrix-element'
          stop 1
        ENDIF
      ENDIF
      ANS=ANS/DBLE(IDEN)
      END


      Subroutine  MATRIX1(P,IC, TS)
C     
C     Generated by MadGraph5_aMC@NLO v. 3.5.0, 2023-05-12
C     By the MadGraph5_aMC@NLO Development Team
C     Visit launchpad.net/madgraph5 and amcatnlo.web.cern.ch
C     
C     Returns amplitude squared summed/avg over colors
C     for the point with external lines W(0:6,NEXTERNAL)
C     
C     Process: pp > e+ vm~ ve vm chi1 ap QEDp<=5 @1
C     
      IMPLICIT NONE
C     
C     CONSTANTS
C     
      INTEGER    NGRAPHS
      PARAMETER (NGRAPHS=1) 
      include 'genps.inc'
      include 'nexternal.inc'
      include 'maxamps.inc'
      INTEGER    NWAVEFUNCS,     NCOLOR
      PARAMETER (NWAVEFUNCS=21, NCOLOR=1) 
      REAL*8     ZERO
      PARAMETER (ZERO=0D0)
      COMPLEX*16 IMAG1
      PARAMETER (IMAG1=(0D0,1D0))
      INTEGER NAMPSO, NSQAMPSO
      PARAMETER (NAMPSO=1, NSQAMPSO=1)
      LOGICAL CHOSEN_SO_CONFIGS(NSQAMPSO)
      DATA CHOSEN_SO_CONFIGS/.TRUE./
      SAVE CHOSEN_SO_CONFIGS
      INTEGER                 NCOMB         
      PARAMETER (             NCOMB=48)
C     
C     ARGUMENTS 
C     
      REAL*8 P(0:3,NEXTERNAL)
      INTEGER NHEL(NEXTERNAL), IC(NEXTERNAL)
      REAL*8 TS(NCOMB)
C     
C     LOCAL VARIABLES 
C     
      INTEGER I,J,M,N,K
      COMPLEX*16 ZTEMP,TMP_JAMP(0)
      COMPLEX*16 TMP(6)
      REAL*8 CF(NCOLOR,NCOLOR)
      COMPLEX*16 AMP(NCOMB,NGRAPHS), JAMP(NCOLOR,NAMPSO)
      COMPLEX*16 W(6,NWAVEFUNCS)
C     Needed for v4 models
      COMPLEX*16 DUM0,DUM1
      DATA DUM0, DUM1/(0d0, 0d0), (1d0, 0d0)/

      double precision fk_mdl_WAp 
      double precision fk_mdl_Wchi2 
      double precision fk_ZERO 
      save fk_mdl_WAp 
      save fk_mdl_Wchi2 
      save fk_ZERO 

      logical first
      data first /.true./
      save first
C     
C     FUNCTION
C     
      INTEGER SQSOINDEX1

C     
C     GLOBAL VARIABLES
C     
      Double Precision amp2(maxamps), jamp2(0:maxflow)
      common/to_amps/  amp2,       jamp2
      include 'coupl.inc'

      double precision tmin_for_channel
      integer sde_strat    !  1 means standard single diagram enhancement strategy,
C     2 means approximation by the	denominator of the propagator
      common/TO_CHANNEL_STRAT/tmin_for_channel,	sde_strat

      double precision small_width_treatment
      common/narrow_width/small_width_treatment
C     
C     COLOR DATA
C     
      DATA (CF(i,  1),i=  1,  1) /1.000000000000000d+00/
C     1 ColorOne()
C     ----------
C     BEGIN CODE
C     ----------
      if (first) then
        first=.false.
        IF(ZERO.ne.0d0) fk_ZERO = SIGN(MAX(ABS(ZERO), ABS(ZERO
     $   *small_width_treatment)), ZERO)
        IF(mdl_WAp.ne.0d0) fk_mdl_WAp = SIGN(MAX(ABS(mdl_WAp),
     $    ABS(mdl_MAp*small_width_treatment)), mdl_WAp)
        IF(ZERO.ne.0d0) fk_ZERO = SIGN(MAX(ABS(ZERO), ABS(mdl_MMU
     $   *small_width_treatment)), ZERO)
        IF(ZERO.ne.0d0) fk_ZERO = SIGN(MAX(ABS(ZERO), ABS(mdl_Mchi1
     $   *small_width_treatment)), ZERO)
        IF(mdl_Wchi2.ne.0d0) fk_mdl_Wchi2 = SIGN(MAX(ABS(mdl_Wchi2),
     $    ABS(mdl_Mchi2*small_width_treatment)), mdl_Wchi2)
        IF(ZERO.ne.0d0) fk_ZERO = SIGN(MAX(ABS(ZERO), ABS(mdl_Me
     $   *small_width_treatment)), ZERO)
        IF(ZERO.ne.0d0) fk_ZERO = SIGN(MAX(ABS(ZERO), ABS(mdl_Mp
     $   *small_width_treatment)), ZERO)
      endif
      AMP(:,:) = (0d0,0d0)
            CALL IXXXXX(P(0,1),MDL_MP,+1,+1*IC(1),W(1,1))  !  count 24
      CALL IXXXXX(P(0,1),MDL_MP,-1,+1*IC(1),W(1,2))  !  count 24
      CALL IXXXXX(P(0,2),MDL_ME,+1,-1*IC(2),W(1,3))  !  count 1
      CALL IXXXXX(P(0,2),MDL_ME,-1,-1*IC(2),W(1,4))  !  count 1
      CALL IXXXXX(P(0,3),ZERO,-1,-1*IC(3),W(1,5))  !  count 2
      CALL OXXXXX(P(0,4),ZERO,+1,+1*IC(4),W(1,6))  !  count 2
      CALL OXXXXX(P(0,5),ZERO,+1,+1*IC(5),W(1,7))  !  count 24
      CALL OXXXXX(P(0,5),ZERO,-1,+1*IC(5),W(1,8))  !  count 24
      CALL OXXXXX(P(0,6),MDL_MCHI1,+1,+1*IC(6),W(1,9))  !  count 3
      CALL OXXXXX(P(0,6),MDL_MCHI1,-1,+1*IC(6),W(1,10))  !  count 3
      CALL VXXXXX(P(0,7),MDL_MAP,+1,+1*IC(7),W(1,11))  !  count 2
      CALL VXXXXX(P(0,7),MDL_MAP, 0,+1*IC(7),W(1,12))  !  count 2
      CALL VXXXXX(P(0,7),MDL_MAP,-1,+1*IC(7),W(1,13))  !  count 2
      CALL FFFF6_2(W(1,5),W(1,3),W(1,6),GC_3,MDL_MMU,FK_ZERO,W(1,14))  !  count 24
      CALL FFFF6_2(W(1,5),W(1,4),W(1,6),GC_3,MDL_MMU,FK_ZERO,W(1,15))  !  count 24
      CALL FFV1_2_1(W(1,9),W(1,11),GC_10,GC_11,MDL_MCHI2,FK_MDL_WCHI2,W(
     $1,16))  !  count 8
      CALL FFV1_2_1(W(1,9),W(1,12),GC_10,GC_11,MDL_MCHI2,FK_MDL_WCHI2,W(
     $1,17))  !  count 8
      CALL FFV1_2_1(W(1,9),W(1,13),GC_10,GC_11,MDL_MCHI2,FK_MDL_WCHI2,W(
     $1,18))  !  count 8
      CALL FFV1_2_1(W(1,10),W(1,11),GC_10,GC_11,MDL_MCHI2,FK_MDL_WCHI2,W
     $(1,19))  !  count 8
      CALL FFV1_2_1(W(1,10),W(1,12),GC_10,GC_11,MDL_MCHI2,FK_MDL_WCHI2,W
     $(1,20))  !  count 8
      CALL FFV1_2_1(W(1,10),W(1,13),GC_10,GC_11,MDL_MCHI2,FK_MDL_WCHI2,W
     $(1,21))  !  count 8
      CALL FFFF1_2_3_4_5P1N_2(W(1,1), W(1,14), W(1,7), GC_6, GC_9, GC_5,
     $ GC_8, GC_7, TMP(1))
      call CombineAmp(6,
     & (/12,11,10,9,8,7/), 
     & (/16,17,18,19,20,21/),
     & TMP, W, AMP(1,1))
      CALL FFFF1_2_3_4_5P1N_2(W(1,1), W(1,14), W(1,8), GC_6, GC_9, GC_5,
     $ GC_8, GC_7, TMP(1))
      call CombineAmp(6,
     & (/6,5,4,3,2,1/), 
     & (/16,17,18,19,20,21/),
     & TMP, W, AMP(1,1))
      CALL FFFF1_2_3_4_5P1N_2(W(1,1), W(1,15), W(1,7), GC_6, GC_9, GC_5,
     $ GC_8, GC_7, TMP(1))
      call CombineAmp(6,
     & (/24,23,22,21,20,19/), 
     & (/16,17,18,19,20,21/),
     & TMP, W, AMP(1,1))
      CALL FFFF1_2_3_4_5P1N_2(W(1,1), W(1,15), W(1,8), GC_6, GC_9, GC_5,
     $ GC_8, GC_7, TMP(1))
      call CombineAmp(6,
     & (/18,17,16,15,14,13/), 
     & (/16,17,18,19,20,21/),
     & TMP, W, AMP(1,1))
      CALL FFFF1_2_3_4_5P1N_2(W(1,2), W(1,14), W(1,7), GC_6, GC_9, GC_5,
     $ GC_8, GC_7, TMP(1))
      call CombineAmp(6,
     & (/36,35,34,33,32,31/), 
     & (/16,17,18,19,20,21/),
     & TMP, W, AMP(1,1))
      CALL FFFF1_2_3_4_5P1N_2(W(1,2), W(1,14), W(1,8), GC_6, GC_9, GC_5,
     $ GC_8, GC_7, TMP(1))
      call CombineAmp(6,
     & (/30,29,28,27,26,25/), 
     & (/16,17,18,19,20,21/),
     & TMP, W, AMP(1,1))
      CALL FFFF1_2_3_4_5P1N_2(W(1,2), W(1,15), W(1,7), GC_6, GC_9, GC_5,
     $ GC_8, GC_7, TMP(1))
      call CombineAmp(6,
     & (/48,47,46,45,44,43/), 
     & (/16,17,18,19,20,21/),
     & TMP, W, AMP(1,1))
      CALL FFFF1_2_3_4_5P1N_2(W(1,2), W(1,15), W(1,8), GC_6, GC_9, GC_5,
     $ GC_8, GC_7, TMP(1))
      call CombineAmp(6,
     & (/42,41,40,39,38,37/), 
     & (/16,17,18,19,20,21/),
     & TMP, W, AMP(1,1))  !  count 1

      JAMP(:,:)  = (0d0,0d0)
      DO K = 1, NCOMB
        
        JAMP(:,:) = (0D0,0D0)
C       JAMPs contributing to orders ALL_ORDERS=1
        JAMP(1,1) = (-1.000000000000000D+00)*AMP( K,1)

        TS(K) = 0.D0 
        DO M = 1, NAMPSO
          DO I = 1, NCOLOR
            ZTEMP = (0.D0,0.D0)
            DO J = 1, NCOLOR
              ZTEMP = ZTEMP + CF(J,I)*JAMP(J,M)
            ENDDO
            DO N = 1, NAMPSO

              TS(K) = TS(K) + ZTEMP*DCONJG(JAMP(I,N))

            ENDDO
          ENDDO
        ENDDO
        if(sde_strat.eq.1) then
        
        IF(SDE_STRAT.EQ.1)THEN
          AMP2(1)=AMP2(1)+AMP( K,1)*DCONJG(AMP( K,1))
        ENDIF

        endif
        Do I = 1, NCOLOR
          DO M = 1, NAMPSO
            DO N = 1, NAMPSO

              Jamp2(i)=Jamp2(i)+DABS(DBLE(Jamp(i,m)*dconjg(Jamp(i,n))))

            enddo
          enddo
        Enddo
      ENDDO

      END


      SUBROUTINE PRINT_ZERO_AMP_1()

      integer i
      i =1
      return
      end
C     Set of functions to handle the array indices of the split orders


      INTEGER FUNCTION SQSOINDEX1(ORDERINDEXA, ORDERINDEXB)
C     
C     This functions plays the role of the interference matrix. It can
C      be hardcoded or 
C     made more elegant using hashtables if its execution speed ever
C      becomes a relevant
C     factor. From two split order indices, it return the
C      corresponding index in the squared 
C     order canonical ordering.
C     
C     CONSTANTS
C     

      INTEGER    NSO, NSQUAREDSO, NAMPSO
      PARAMETER (NSO=1, NSQUAREDSO=1, NAMPSO=1)
C     
C     ARGUMENTS
C     
      INTEGER ORDERINDEXA, ORDERINDEXB
C     
C     LOCAL VARIABLES
C     
      INTEGER I, SQORDERS(NSO)
      INTEGER AMPSPLITORDERS(NAMPSO,NSO)
      DATA (AMPSPLITORDERS(  1,i),i=  1,  1) /    1/
      COMMON/AMPSPLITORDERS1/AMPSPLITORDERS
C     
C     FUNCTION
C     
      INTEGER SOINDEX_FOR_SQUARED_ORDERS1
C     
C     BEGIN CODE
C     
      DO I=1,NSO
        SQORDERS(I)=AMPSPLITORDERS(ORDERINDEXA,I)
     $   +AMPSPLITORDERS(ORDERINDEXB,I)
      ENDDO
      SQSOINDEX1=SOINDEX_FOR_SQUARED_ORDERS1(SQORDERS)
      END

      INTEGER FUNCTION SOINDEX_FOR_SQUARED_ORDERS1(ORDERS)
C     
C     This functions returns the integer index identifying the squared
C      split orders list passed in argument which corresponds to the
C      values of the following list of couplings (and in this order).
C     []
C     
C     CONSTANTS
C     
      INTEGER    NSO, NSQSO, NAMPSO
      PARAMETER (NSO=1, NSQSO=1, NAMPSO=1)
C     
C     ARGUMENTS
C     
      INTEGER ORDERS(NSO)
C     
C     LOCAL VARIABLES
C     
      INTEGER I,J
      INTEGER SQSPLITORDERS(NSQSO,NSO)
      DATA (SQSPLITORDERS(  1,i),i=  1,  1) /    2/
      COMMON/SQPLITORDERS1/SQPLITORDERS
C     
C     BEGIN CODE
C     
      DO I=1,NSQSO
        DO J=1,NSO
          IF (ORDERS(J).NE.SQSPLITORDERS(I,J)) GOTO 1009
        ENDDO
        SOINDEX_FOR_SQUARED_ORDERS1 = I
        RETURN
 1009   CONTINUE
      ENDDO

      WRITE(*,*) 'ERROR:: Stopping in function' 
      WRITE(*,*) 'SOINDEX_FOR_SQUARED_ORDERS1'
      WRITE(*,*) 'Could not find squared orders ',(ORDERS(I),I=1,NSO)
      STOP

      END

      SUBROUTINE GET_NSQSO_BORN1(NSQSO)
C     
C     Simple subroutine returning the number of squared split order
C     contributions returned when calling smatrix_split_orders 
C     

      INTEGER    NSQUAREDSO
      PARAMETER  (NSQUAREDSO=1)

      INTEGER NSQSO

      NSQSO=NSQUAREDSO

      END

C     This is the inverse subroutine of SOINDEX_FOR_SQUARED_ORDERS.
C      Not directly useful, but provided nonetheless.
      SUBROUTINE GET_SQUARED_ORDERS_FOR_SOINDEX1(SOINDEX,ORDERS)
C     
C     This functions returns the orders identified by the squared
C      split order index in argument. Order values correspond to
C      following list of couplings (and in this order):
C     []
C     
C     CONSTANTS
C     
      INTEGER    NSO, NSQSO
      PARAMETER (NSO=1, NSQSO=1)
C     
C     ARGUMENTS
C     
      INTEGER SOINDEX, ORDERS(NSO)
C     
C     LOCAL VARIABLES
C     
      INTEGER I
      INTEGER SQPLITORDERS(NSQSO,NSO)
      COMMON/SQPLITORDERS1/SQPLITORDERS	  
C     
C     BEGIN CODE
C     
      IF (SOINDEX.gt.0.and.SOINDEX.le.NSQSO) THEN
        DO I=1,NSO
          ORDERS(I) =  SQPLITORDERS(SOINDEX,I)
        ENDDO
        RETURN
      ENDIF

      WRITE(*,*) 'ERROR:: Stopping function'
     $ //' GET_SQUARED_ORDERS_FOR_SOINDEX1'
      WRITE(*,*) 'Could not find squared orders index ',SOINDEX
      STOP

      END SUBROUTINE

C     This is the inverse subroutine of getting amplitude SO orders.
C      Not directly useful, but provided nonetheless.
      SUBROUTINE GET_ORDERS_FOR_AMPSOINDEX1(SOINDEX,ORDERS)
C     
C     This functions returns the orders identified by the split order
C      index in argument. Order values correspond to following list of
C      couplings (and in this order):
C     []
C     
C     CONSTANTS
C     
      INTEGER    NSO, NAMPSO
      PARAMETER (NSO=1, NAMPSO=1)
C     
C     ARGUMENTS
C     
      INTEGER SOINDEX, ORDERS(NSO)
C     
C     LOCAL VARIABLES
C     
      INTEGER I
      INTEGER AMPSPLITORDERS(NAMPSO,NSO)
      COMMON/AMPSPLITORDERS1/AMPSPLITORDERS
C     
C     BEGIN CODE
C     
      IF (SOINDEX.gt.0.and.SOINDEX.le.NAMPSO) THEN
        DO I=1,NSO
          ORDERS(I) =  AMPSPLITORDERS(SOINDEX,I)
        ENDDO
        RETURN
      ENDIF

      WRITE(*,*) 'ERROR:: Stopping function GET_ORDERS_FOR_AMPSOINDEX1'
      WRITE(*,*) 'Could not find amplitude split orders index ',SOINDEX
      STOP

      END SUBROUTINE

C     This function is not directly useful, but included for
C      completeness
      INTEGER FUNCTION SOINDEX_FOR_AMPORDERS1(ORDERS)
C     
C     This functions returns the integer index identifying the
C      amplitude split orders passed in argument which correspond to
C      the values of the following list of couplings (and in this
C      order):
C     []
C     
C     CONSTANTS
C     
      INTEGER    NSO, NAMPSO
      PARAMETER (NSO=1, NAMPSO=1)
C     
C     ARGUMENTS
C     
      INTEGER ORDERS(NSO)
C     
C     LOCAL VARIABLES
C     
      INTEGER I,J
      INTEGER AMPSPLITORDERS(NAMPSO,NSO)
      COMMON/AMPSPLITORDERS1/AMPSPLITORDERS
C     
C     BEGIN CODE
C     
      DO I=1,NAMPSO
        DO J=1,NSO
          IF (ORDERS(J).NE.AMPSPLITORDERS(I,J)) GOTO 1009
        ENDDO
        SOINDEX_FOR_AMPORDERS1 = I
        RETURN
 1009   CONTINUE
      ENDDO

      WRITE(*,*) 'ERROR:: Stopping function SOINDEX_FOR_AMPORDERS1'
      WRITE(*,*) 'Could not find squared orders ',(ORDERS(I),I=1,NSO)
      STOP

      END

