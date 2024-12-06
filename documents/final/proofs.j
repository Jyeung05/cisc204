CONJECTUREPANEL MostEpicSequents
PROOF "¬(Q∧¬Q)"
INFER ¬(Q∧¬Q)
FORMULAE
0 ⊥,
1 ¬Q,
2 Q,
3 Q∧¬Q 
IS
SEQ ("¬ intro"[A\3]) (cut[B,C\1,0]) (LAYOUT "∧ elim" (0) ("∧ elim(R)"[A,B\2,1]) (hyp[A\3])) (cut[B,C\2,0]) (LAYOUT "∧ elim" (0) ("∧ elim(L)"[A,B\2,1]) (hyp[A\3])) (cut[B,C\0,0]) ("¬ elim"[B\2]) (hyp[A\2]) (hyp[A\1]) (hyp[A\0])
END
CONJECTUREPANEL MostEpicSequents
PROOF "(DA→Q11), (DB→Q12), DA, DB ⊢ Q11∨Q12"
INFER (DA→Q11),
     (DB→Q12),
     DA,
     DB 
     ⊢ Q11∨Q12 
FORMULAE
0 Q11,
1 Q12,
2 DA,
3 DA→Q11,
4 Q11∨Q12,
5 DB,
6 DB→Q12 
IS
SEQ (cut[B,C\1,4]) ("→ elim"[A,B\5,1]) (hyp[A\6]) (hyp[A\5]) (cut[B,C\0,4]) ("→ elim"[A,B\2,0]) (hyp[A\3]) (hyp[A\2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\1,0]) (hyp[A\0]))
END
CONJECTUREPANEL MostEpicSequents
PROOF "((TA∨TB)→(Q11∨Q5)), TA→Q11, TA ⊢ Q11∨Q5"
INFER ((TA∨TB)→(Q11∨Q5)),
     TA→Q11,
     TA 
     ⊢ Q11∨Q5 
FORMULAE
0 Q11,
1 Q5,
2 TA,
3 TA→Q11,
4 Q11∨Q5,
5 (TA∨TB)→(Q11∨Q5)
IS
SEQ (cut[B,C\0,4]) ("→ elim"[A,B\2,0]) (hyp[A\3]) (hyp[A\2]) (LAYOUT "∨ intro" (0) ("∨ intro(L)"[B,A\1,0]) (hyp[A\0]))
END
