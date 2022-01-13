#!python3

""" 
Necklace numbers are a number sequence.  You start with 2 digits. The 3rd digit is created by adding the previous 2 digits, but if it's greater than 10, you add the sum of those 2 digits again.  You keep repeating this process until you get back to the 2 digits you started with
extra: What is the shortest necklace number sequence that can be made?
"""

def necklace(a,b):
    printlist = []
    printing = ""
    F = int(a)
    printlist.append(F)
    printing = printing + str(a)
    S = int(b)
    printlist.append(S)
    printing = printing + str(b)
    while True:
        F = int(printlist[len(printlist)-2])
        S = int(printlist[len(printlist)-1])
        T = F + S
        if T >= 10 :
            T = int(str(T)[0])+int(str(T)[1])
        printlist.append(T)
        printing = printing + str(T)
        if S == int(a) and T == int(b):
            return printing

def main():
  assert necklace(9,4) == "94483257314595516742685494"
  assert necklace(1,3) == "13472922461786527977538213"
  assert necklace(5,1) == "51674268549448325731459551"
  assert necklace(3,4) == "34729224617865279775382134"

if __name__ == "__main__":
  main()
