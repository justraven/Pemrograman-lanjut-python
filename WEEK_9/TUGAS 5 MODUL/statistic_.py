#### TUGAS 5 ####

def mean(number) :

     hasil = 0

     for i in number :
          hasil =  hasil + number[i-1] 
          # i dikurangi satu karena index dimulai dari nol
     return hasil / len(number)
