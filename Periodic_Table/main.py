number = {1:"I",2:"II",3:"III",4:"IV",5:"V",6:"VI",7:"VII",8:"VIII"}
dictionary = {1: "¹", 2: "²", 3: "³", 4: "⁴", 5: "⁵", 6: "⁶", 7: "⁷", 8: "⁸", 9: "⁹", 10: "¹⁰", 11: "¹¹", 12: "¹²", 13: "¹³", 14: "¹⁴"}
dicte = {"⁰": 0, "¹": 1, "²": 2, "³": 3, "⁴": 4, "⁵": 5, "⁶": 6, "⁷": 7, "⁸": 8, "⁹": 9, "¹⁰": 10, "¹¹": 11, "¹²": 12, "¹³": 13, "¹⁴": 14}
periodic = {
    1: "H", 2: "He", 3: "Li", 4: "Be", 5: "B", 6: "C", 7: "N", 8: "O", 9: "F", 10: "Ne", 11: "Na", 12: "Mg", 13: "Al", 14: "Si", 15: "P",
    16: "S", 17: "Cl", 18: "Ar", 19: "K", 20: "Ca", 21: "Sc", 22: "Ti", 23: "V", 24: "Cr", 25: "Mn", 26: "Fe", 27: "Co", 28: "Ni", 29: "Cu",
    30: "Zn", 31: "Ga", 32: "Ge", 33: "As", 34: "Se", 35: "Br", 36: "Kr", 37: "Rb", 38: "Sr", 39: "Y", 40: "Zr", 41: "Nb", 42: "Mo", 43: "Tc",
    44: "Ru", 45: "Rh", 46: "Pd", 47: "Ag", 48: "Cd", 49: "In", 50: "Sn", 51: "Sb", 52: "Te", 53: "I", 54: "Xe", 55: "Cs", 56: "Ba", 57: "La",
    58: "Ce", 59: "Pr", 60: "Nd", 61: "Pm", 62: "Sm", 63: "Eu", 64: "Gd", 65: "Tb", 66: "Dy", 67: "Ho", 68: "Er", 69: "Tm", 70: "Yb", 71: "Lu",
    72: "Hf", 73: "Ta", 74: "W", 75: "Re", 76: "Os", 77: "Ir", 78: "Pt", 79: "Au", 80: "Hg", 81: "Tl", 82: "Pb", 83: "Bi", 84: "Po", 85: "At",
    86: "Rn", 87: "Fr", 88: "Ra", 89: "Ac", 90: "Th", 91: "Pa", 92: "U", 93: "Np", 94: "Pu", 95: "Am", 96: "Cm", 97: "Bk", 98: "Cf", 99: "Es",
    100: "Fm",101:"Md",102:"No",103:"Lr",104:"Rf",105:"Db",106:"Sg",107:"Bh",108:"Hs",109:"Mt",110:"DS",111:"Rg",112:"Cn",113:"Nh",114:"Fl",
    115:"Mc",116:"Lv",117:"Ts",118:"Og"
        }
periodic_elements = [
    "Hydrogen", "Helium", "Lithium", "Beryllium", "Boron", "Carbon", "Nitrogen", "Oxygen", "Fluorine", "Neon",
    "Sodium", "Magnesium", "Aluminum", "Silicon", "Phosphorus", "Sulfur", "Chlorine", "Argon", "Potassium", "Calcium",
    "Scandium", "Titanium", "Vanadium", "Chromium", "Manganese", "Iron", "Cobalt", "Nickel", "Copper", "Zinc",
    "Gallium", "Germanium", "Arsenic", "Selenium", "Bromine", "Krypton", "Rubidium", "Strontium", "Yttrium", "Zirconium",
    "Niobium", "Molybdenum", "Technetium", "Ruthenium", "Rhodium", "Palladium", "Silver", "Cadmium", "Indium", "Tin",
    "Antimony", "Tellurium", "Iodine", "Xenon", "Cesium", "Barium", "Lanthanum", "Cerium", "Praseodymium", "Neodymium",
    "Promethium", "Samarium", "Europium", "Gadolinium", "Terbium", "Dysprosium", "Holmium", "Erbium", "Thulium", "Ytterbium",
    "Lutetium", "Hafnium", "Tantalum", "Tungsten", "Rhenium", "Osmium", "Iridium", "Platinum", "Gold", "Mercury",
    "Thallium", "Lead", "Bismuth", "Polonium", "Astatine", "Radon", "Francium", "Radium", "Actinium", "Thorium",
    "Protactinium", "Uranium", "Neptunium", "Plutonium", "Americium", "Curium", "Berkelium", "Californium", "Einsteinium", "Fermium",
    "Mendelevium", "Nobelium", "Lawrencium", "Rutherfordium", "Dubnium", "Seaborgium", "Bohrium", "Hassium", "Meitnerium", "Darmstadtium",
    "Roentgenium", "Copernicium", "Nihonium", "Flerovium", "Moscovium", "Livermorium", "Tennessine", "Oganesson"
]

def function(y, x,Z):
    I = 0
    if Z > 0:
        for i in range(x):
            if Z > 0:
                Z -= 1
                I += 1
        return y + dictionary[I]
    else:
        return []

def sulydulieu(Z):
        accept = False
        E = Z
        if Z == 24:
            lst_main = ['1S²', '2S²', '2P⁶', '3S²', '3P⁶', '3D⁵', '4S¹']
            X = 1
        elif Z == 29:
            lst_main = ["1S²", "2S²", "2P⁶", "3S²", "3P⁶", "3D¹⁰", "4S¹"]
            X = 1
        else:
            danh_sach = []
            classes = [[] for _ in range(8)]
            # dãy mức năng lượng
            danh_sach.append(function("1S", 2,Z))  # s1
            danh_sach.append(function("2S", 2,Z-2))  # s2
            danh_sach.append(function("2P", 6,Z-4))  # p2
            danh_sach.append(function("3S", 2,Z-10))  # s3
            danh_sach.append(function("3P", 6,Z-12))  # p3
            danh_sach.append(function("4S", 2,Z-18))  # s4
            danh_sach.append(function("3D", 10,Z-20))  # d3
            danh_sach.append(function("4P", 6,Z-30))  # p4
            danh_sach.append(function("5S", 2,Z-36))  # s5
            danh_sach.append(function("4D", 10,Z-38))  # d4
            danh_sach.append(function("5P", 6,Z-48))  # p5
            danh_sach.append(function("6S", 2,Z-54))  # s6
            danh_sach.append(function("4F", 14,Z-56))  # f4
            danh_sach.append(function("5D", 10,Z-70))  # d5
            danh_sach.append(function("6P", 6,Z-80))  # p6
            danh_sach.append(function("7S", 2,Z-86))  # s7
            danh_sach.append(function("5F", 14,Z-88))  # f5
            danh_sach.append(function("6D", 10,Z-102))  # d6
            danh_sach.append(function("7P", 6,Z-112))  # p7
            danh_sach.append(function("8S", 2,Z-118))  # s8
            danh_sach.append(function("6F", 14,Z-120))  # f6

            for i in danh_sach:
                for j in range(8):
                    if str(j + 1) in i:
                        classes[j].append(i)

            lst_main = [item for sublist in classes for item in sublist]
            data = classes[int(lst_main[-1][0]) - 1]
            X = sum([dicte[i[-1]] for i in data])
            for i in range(6):
                if [] in classes:
                    classes.remove([])
            accept = True

        str_main = "".join(lst_main)
        Exg = "+ CHe: " + str_main
        if len(lst_main) >= 2:
            W = [lst_main[i] for i in range(-2, 0)]
            if "D" in W[0] and "S" in W[1]:
                total = sum([dicte[i[-1]] for i in W])
            else:
                if W[0][0] == W[1][0]:
                    total = sum([dicte[i[-1]] for i in W])
                else:
                    total = dicte[W[1][-1]]
        list_main = lst_main
        if E <= 2:
            Eg = "+ Không có"
        if E > 2 and E <= 10:
            for i in ["1S²"]:
                total_str = ""
                list_main.remove(i)
                for i in list_main:
                    total_str += i
                collapse = f"[He]{total_str}"
        elif E > 10 and E <= 18:
            for i in ['1S²', '2S²', '2P⁶']:
                total_str = ""
                list_main.remove(i)
                for i in list_main:
                    total_str += i
                collapse = f"[Ne]{total_str}"
        elif E > 18 and E <= 36:
            for i in ['1S²', '2S²', '2P⁶', '3S²', '3P⁶']:
                total_str = ""
                list_main.remove(i)
                for i in list_main:
                    total_str += i
                collapse = f"[Ar]{total_str}"
        elif E > 36 and E <= 54:
            for i in ['1S²', '2S²', '2P⁶', '3S²', '3P⁶', '3D¹⁰', '4S²', '4P⁶']:
                total_str = ""
                list_main.remove(i)
                for i in list_main:
                    total_str += i
                collapse = f"[Kr]{total_str}"
        elif E > 54 and E <= 86:
            for i in ['1S²', '2S²', '2P⁶', '3S²', '3P⁶', '3D¹⁰', '4S²', '4P⁶', '4D¹⁰', '5S²', '5P⁶']:
                total_str = ""
                list_main.remove(i)
                for i in list_main:
                    total_str += i
                collapse = f"[Xe]{total_str}"
        elif E > 86 and E <= 118:
            for i in ['1S²', '2S²', '2P⁶', '3S²', '3P⁶', '3D¹⁰', '4S²', '4P⁶', '4D¹⁰', '4F¹⁴', '5S²', '5P⁶', '5D¹⁰',
                      '6S²', '6P⁶']:
                total_str = ""
                list_main.remove(i)
                for i in list_main:
                    total_str += i
                collapse = f"[Rn]{total_str}"
        if E > 2:
            Eg = f"+ CHe thu gọn : {collapse}"
        if E in range(109,119):
            kpk = "+ không xác định"
        elif X in [1, 2, 3]:
            if E in [1, 2]:
                kpk = "+ nguyên tố là phi kim"
            elif E == 14:
                kpk = "+ nguyên tố là á kim"
            else:
                kpk = "+ nguyên tố là kim loại"
        elif X == 4:
            if E in [32, 50, 82]:
                if E == 32:
                    kpk = "+ nguyên tố là á kim"
                else:
                    kpk = "+ nguyên tố là kim loại"
            elif E in [6, 14]:
                if E == 6:
                    kpk = "+ nguyên tố là phi kim"
                elif E == 14:
                    kpk = "+ nguyên tố là á kim"
        elif X in [5, 6, 7]:
            if E in [33,51,52,85]:
                kpk = "+ nguyên tố là á kim"
            else:
                kpk = "+ nguyên tố là phi kim"
        elif X == 8:
            kpk = "+ nguyên tố là khí hiếm"
        vt = f"+ nguyên tố ở ô {E}"
        if accept:
            if E < 3:
                cl = len(classes)-1
            else:
                cl = len(classes)
            nck = f"+ nguyên tố thuộc chu kỳ {cl}"
        elif Z in [24, 29]:
            nck = "+ nguyên tố thuộc chu kỳ 4"
        if E in range(57,72) or E in range(89,104):
            nn = "+ không xác định"
        elif E > 2:
            if "D" in W[0] and "S" in W[1]:
                if total == 9:
                    nn = f"+ nguyên tố thuộc nhóm VIIIB cột 2"
                elif total == 10:
                    nn = f"+ nguyên tố thuộc nhóm VIIIB cột 3"
                else:
                    if E == 111:
                        nn = "+ nguyên tố thuộc nhóm IB"
                    else:
                        nn = f"+ nguyên tố thuộc nhóm {number[total]}B"
            else:
                nn = f"+ nguyên tố thuộc nhóm {number[total]}A"
        else:
            if E == 1:
                nn = "+ nguyên tố thuộc nhóm IA"
            elif E == 2:
                nn = "+ nguyên tố thuộc nhóm VIIIA"
        nt = f"+ nguyên tố {periodic_elements[E-1]}"
        return [nck,vt,kpk,Exg,Eg,nn,nt]

def mbth(Z):
    accept = False
    E = Z
    if Z == 24:
        lst_main = ['1S²', '2S²', '2P⁶', '3S²', '3P⁶', '3D⁵', '4S¹']
        X = 1
    elif Z == 29:
        lst_main = ["1S²", "2S²", "2P⁶", "3S²", "3P⁶", "3D¹⁰", "4S¹"]
        X = 1
    else:
        danh_sach = []
        classes = [[] for _ in range(8)]
        # dãy mức năng lượng
        danh_sach.append(function("1S", 2, Z))  # s1
        danh_sach.append(function("2S", 2, Z - 2))  # s2
        danh_sach.append(function("2P", 6, Z - 4))  # p2
        danh_sach.append(function("3S", 2, Z - 10))  # s3
        danh_sach.append(function("3P", 6, Z - 12))  # p3
        danh_sach.append(function("4S", 2, Z - 18))  # s4
        danh_sach.append(function("3D", 10, Z - 20))  # d3
        danh_sach.append(function("4P", 6, Z - 30))  # p4
        danh_sach.append(function("5S", 2, Z - 36))  # s5
        danh_sach.append(function("4D", 10, Z - 38))  # d4
        danh_sach.append(function("5P", 6, Z - 48))  # p5
        danh_sach.append(function("6S", 2, Z - 54))  # s6
        danh_sach.append(function("4F", 14, Z - 56))  # f4
        danh_sach.append(function("5D", 10, Z - 70))  # d5
        danh_sach.append(function("6P", 6, Z - 80))  # p6
        danh_sach.append(function("7S", 2, Z - 86))  # s7
        danh_sach.append(function("5F", 14, Z - 88))  # f5
        danh_sach.append(function("6D", 10, Z - 102))  # d6
        danh_sach.append(function("7P", 6, Z - 112))  # p7
        danh_sach.append(function("8S", 2, Z - 118))  # s8
        danh_sach.append(function("6F", 14, Z - 120))  # f6

        for i in danh_sach:
            for j in range(8):
                if str(j + 1) in i:
                    classes[j].append(i)

        lst_main = [item for sublist in classes for item in sublist]
        outer_class = lst_main[-1]
        data = classes[int(outer_class[0]) - 1]
        X = sum([dicte[i[-1]] for i in data])
    if E in range(109, 119):
        z = 4
    elif X in [1, 2, 3]:
        if E in [1, 2]:
            z = 1
        else:
            if E == 5:
                z = 5
            else:
                z = 2
    elif X == 4:
        if E in [32, 50, 82]:
            if E == 32:
                z = 5
            else:
                z = 2
        elif E in [6, 14]:
            if E == 14:
                z = 5
            else:
                z = 1
        elif E == 114:
            z = 4
    elif X in [5, 6, 7]:
        if E in [33,51,52,85]:
            z = 5
        else:
            z = 1
    elif X == 8:
        z = 3
    if E <= 118:
        return z
    else:
        return 6

def main(dulieu):
    if dulieu.isalpha() or int(dulieu) not in range(1, 119):
        return ["","nhập sai dữ liệu","","","","",""]
    else:
        return sulydulieu(int(dulieu))
    
