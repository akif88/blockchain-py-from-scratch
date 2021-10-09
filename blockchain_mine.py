from hashlib import sha256

"""
    proof no bir önceki proof no ile kullanılarak da ilk 4 basamağı 0 olan 
    bir hash fonksiyonu bulunmaya çalışılabilir
"""

proof_no = 0
while sha256(str(proof_no).encode()).hexdigest()[:4] != "0000":
    proof_no+=1


print("Proof: ", proof_no)
