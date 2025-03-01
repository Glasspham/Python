from tkinter import *
from main import *
tk = Tk()
tk.title("Bảng Tuần Hoàn")
tk.iconbitmap("logo-bang-tuan-hoan.ico")
tk.geometry("850x530")
tk.configure(bg="white")
Label(tk,text="Code By Đức Chính",bg="white").place(x=0,y=510)
dulieu = StringVar()
tdy = 20
ban_tuan_hoan = [
    [146,127,128,129,130,0,131,132,133,134,135,136,137,138,139,140,141,142,143,144,145],
    [126,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [119,0,1,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,2],
    [120,0,3,4,0,0,0,0,0,0,0,0,0,0,0,5,6,7,8,9,10],
    [121,0,11,12,0,0,0,0,0,0,0,0,0,0,0,13,14,15,16,17,18],
    [122,0,19,20,21,0,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36],
    [123,0,37,38,39,0,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54],
    [124,0,55,56,57,0,72,73,74,75,76,77,78,79,80,81,82,83,84,85,86],
    [125,0,87,88,89,0,104,105,106,107,108,109,110,111,112,113,114,115,116,117,118],
    [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,58,59,60,61,62,63,64,65,66,67,68,69,70,71,0],
    [0,0,0,0,0,0,90,91,92,93,94,95,96,97,98,99,100,101,102,103,0]
]
bth = ['H', 'He', 'Li', 'Be', 'B', 'C', 'N', 'O', 'F', 'Ne','Na', 'Mg', 'Al', 'Si', 'P', 'S', 'Cl', 'Ar','K', 'Ca', 'Sc', 'Ti', 'V', 'Cr', 'Mn', 'Fe','Co', 'Ni', 'Cu', 'Zn', 'Ga', 'Ge', 'As', 'Se','Br', 'Kr', 'Rb', 'Sr', 'Y', 'Zr', 'Nb', 'Mo','Tc', 'Ru', 'Rh', 'Pd', 'Ag', 'Cd', 'In', 'Sn','Sb', 'Te', 'I', 'Xe', 'Cs', 'Ba', 'La', 'Ce','Pr', 'Nd', 'Pm', 'Sm', 'Eu', 'Gd', 'Tb', 'Dy','Ho', 'Er', 'Tm', 'Yb', 'Lu', 'Hf', 'Ta', 'W','Re', 'Os', 'Ir', 'Pt', 'Au', 'Hg', 'Tl', 'Pb','Bi', 'Po', 'At', 'Rn', 'Fr', 'Ra', 'Ac', 'Th','Pa', 'U', 'Np', 'Pu', 'Am', 'Cm', 'Bk', 'Cf','Es', 'Fm', 'Md', 'No', 'Lr', 'Rf', 'Db','Sg', 'Bh', 'Hs', 'Mt', 'Ds', 'Rg', 'Cn','Nh', 'Fl', 'Mc', 'Lv', 'Ts', 'Og',"1","2","3","4","5","6","7","Nhóm","Ckỳ","IA","IIA","IIIB","IVB","VB","VIB","VIIB","VIIB","VIIB","VIIB","IB","IIB","IIIA","IVA","VA","VIA","VIIA","VIIIA",""]
mau = [0,"#4EEE94","#63B8FF","#FF00FF","#E8E8E8","#20B2AA","pink"]
for i in range(12):
    tdx = 55
    for j in range(21):
        if ban_tuan_hoan[i][j] != 0 :
            if  ban_tuan_hoan[i][j] not in range(119,146):
                Label(tk,bg=mau[mbth(ban_tuan_hoan[i][j])],text=f"{bth[ban_tuan_hoan[i][j]-1]}",font=("Arial Bold",15),width=2).place(x=tdx,y=tdy)
            else:
                Label(tk, bg=mau[mbth(ban_tuan_hoan[i][j])], text=f"{bth[ban_tuan_hoan[i][j] - 1]}",font=("Arial Bold", 7), width=4,height=2).place(x=tdx, y=tdy)
        tdx += 35
    tdy += 35
rsx = 0
rsy = 0
rsi = 0
rsj = 0

def su_ly():
    Canvas(tk,bg="white",width=483,height=300,highlightbackground="white", highlightthickness=2).place(x=265,y=435)
    global rsx,rsy,rsi,rsj
    if rsx != 0:
        Label(tk,bg=mau[mbth(ban_tuan_hoan[rsi][rsj])], text=f"{bth[ban_tuan_hoan[rsi][rsj] - 1]}", font=("Arial Bold", 15), width=2).place(x=rsx, y=rsy)
    tdy = 440
    x_text = 260
    if dulieu.get().isalpha():
        if len(dulieu.get()) == 2:
            dlmain = dulieu.get()[0].upper()+dulieu.get()[-1].lower()
        elif len(dulieu.get()) == 1:
            dlmain = dulieu.get()[0].upper()
        else:
            dlmain = "not in"
        if dlmain in bth:
            value = str(bth.index(dlmain)+1)
        else:
            value = dulieu.get()
    else:
        value = dulieu.get()
    xyz = main(value)
    for i in range(7):
        i = 7-i-1
        Label(tk,bg="white",text=f"{xyz[i]}",font=("Arial Bold",10,"bold")).place(x=x_text,y=tdy)
        if i ==3:
            x_text += 220
            tdy = 420
        tdy += 20
    tym = 20
    for i in range(12):
        txm = 55
        for j in range(21):
            if value.isalpha() == False and int(value) <= 118:
                if ban_tuan_hoan[i][j] != 0 and ban_tuan_hoan[i][j] == int(value):
                    Label(tk,bg="red", text=f"{bth[ban_tuan_hoan[i][j] - 1]}", font=("Arial Bold", 15), width=2).place(x=txm, y=tym)
                    rsx = txm
                    rsy = tym
                    rsi = i
                    rsj = j
                    break
                txm += 35
        tym += 35
Entry(tk, bg="#009ACD", fg="#E0FFFF", font=("Arial Bold",25,"bold"),width=5,textvariable=dulieu).place(x=90,y=380)
Button(tk,text = "Tìm Kiếm",fg="#E0FFFF",font=("Arial Bold",11,"bold"), bg="#009ACD",width=8,command = su_ly).place(x=95,y=425)

tk.mainloop()