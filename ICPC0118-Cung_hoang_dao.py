t = int(input())
while t > 0:
    ngay, thang = map(int, input().split())
    if thang == 1:
        if ngay <= 19: print("Ma Ket")
        else: print("Bao Binh")
    elif thang == 2:
        if ngay <= 18: print("Bao Binh")
        else: print("Song Ngu")
    elif thang == 3:
        if ngay <= 20: print("Song Ngu")
        else: print("Bach Duong")
    elif thang == 4:
        if ngay <= 19: print("Bach Duong")
        else: print("Kim Nguu")
    elif thang == 5:
        if ngay <= 20: print("Kim Nguu")
        else: print("Song Tu")
    elif thang == 6:
        if ngay <= 20: print("Song Tu")
        else: print("Cu Giai")
    elif thang == 7:
        if ngay <= 22: print("Cu Giai")
        else: print("Su Tu")
    elif thang == 8:
        if ngay <= 22: print("Su Tu")
        else: print("Xu Nu")
    elif thang == 9:
        if ngay <= 22: print("Xu Nu")
        else: print("Thien Binh")
    elif thang == 10:
        if ngay <= 22: print("Thien Binh")
        else: print("Thien Yet")
    elif thang == 11:
        if ngay <= 22: print("Thien Yet")
        else: print("Nhan Ma")
    elif thang == 12:
        if ngay <= 21: print("Nhan Ma")
        else: print("Ma Ket")
    t -= 1