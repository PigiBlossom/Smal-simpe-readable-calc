val, run = "", "0"
while val != "x":
    try:
        val = input("Välj räknesätt:\nAddition (+)\nSubtraktion (-)\nMultiplikation (*)\nDivision(/)\nPotens (^)\nExit (x)\n\n")
        if val != "x":
            if run != "1":
                tal1 = float(input("Skriv tal 1:"))
            tal2 = float(input("Skriv tal 2:"))
        if val == "+":
            tal1 = (lambda x: print(f"{tal1} {val} {tal2} = {x}\n") or x)(tal1 + tal2)
        elif val == "-":
            tal1 = (lambda x: print(f"{tal1} {val} {tal2} = {x}\n") or x)(tal1 - tal2)
        elif val == "*":
            tal1 = (lambda x: print(f"{tal1} {val} {tal2} = {x}\n") or x)(tal1 * tal2)
        elif val == "/":
            tal1 = (lambda x: print(f"{tal1} {val} {tal2} = {x}\n") or x)(tal1 / tal2)
        elif val == "^":
            tal1 = (lambda x: print(f"{tal1} {val} {tal2} = {x}\n") or x)(tal1 ** tal2)
        else:
            break
        run = "1"
    except:
        print("\nerror\n")