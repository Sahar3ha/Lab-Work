#
N = int(input("Enter the number of students: "))
K = int(input("Enter the number of apples: "))
Eachwillget = (K//N)
RemainingK = (Eachwillget % K)
print(f"Each student will get {Eachwillget}")
print(f"{RemainingK} no of apples will remain")