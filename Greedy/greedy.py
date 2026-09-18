LC 1520. Maximum Number of Non-Overlapping Substrings

Lemma:             Any two valid substrings are either disjoint or one contains the other.

Exchange argument: Let \(I\) be the shortest remaining valid substring. 
                   Any valid substring \(J\) that overlaps \(I\) must contain \(I\). 
                   Therefore, if an optimal solution contains \(J\), 
                   replacing \(J\) with \(I\) preserves the number of substrings and cannot increase total length. 
                   Hence some optimal solution always contains \(I\).

Therefore:         repeatedly taking the shortest non-overlapping valid substring is optimal.
