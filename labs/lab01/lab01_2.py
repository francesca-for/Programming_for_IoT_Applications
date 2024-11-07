import json

class Calculator:
    def __init__(self):
        pass

    def add(self, ops):
        res = 0
        for x in ops:
            res += x
        print(res)
        new_op = {"operation":"add","operands":ops,"result":res}
        f = json.load(open("lab01_2.json"))
        f["calculator_history"].append(new_op)
        json.dump(f, open("lab01_2.json", "w"))
    
    def sub(self, ops):
        res = ops[0]
        for i in range(1,len(ops)):
            res -= ops[i]
        print(res)
        new_op = {"operation":"sub","operands":ops,"result":res}
        f = json.load(open("lab01_2.json"))
        f["calculator_history"].append(new_op)
        json.dump(f, open("lab01_2.json", "w"))

    def mul(self, ops):
        res = 1
        for x in ops:
            res = res * x
        print(res)
        new_op = {"operation":"mul","operands":ops,"result":res}
        f = json.load(open("lab01_2.json"))
        f["calculator_history"].append(new_op)
        json.dump(f, open("lab01_2.json", "w"))
    
    def div(self, ops):
        res = ops[0]
        for i in range(1,len(ops)):
            if ops[i]==0:
                print("Errore: divisione per zero. Partial res: "+str(res))
                new_op = {"operation":"div","operands":ops,"result":"Division by 0 error. Partial res: "+str(res)}
                f = json.load(open("lab01_2.json"))
                f["calculator_history"].append(new_op)
                json.dump(f, open("lab01_2.json", "w"))
                return
            else:
                res = res / ops[i]
        print(res)

        new_op = {"operation":"div","operands":ops,"result":res}
        f = json.load(open("lab01_2.json"))
        f["calculator_history"].append(new_op)
        json.dump(f, open("lab01_2.json", "w"))
    
    def del_h(self):
        f = json.load(open("lab01_2.json"))
        f["calculator_history"] = []
        json.dump(f, open("lab01_2.json", "w"))


if __name__=="__main__":
    calculator = Calculator()

    while True:
        operation = input('New operation. Choose one in [add, sub, mul, div, exit, del_h]: ')
        if ((operation != "add") & (operation != "sub") & (operation != "mul") & (operation != "div") & (operation != "exit") & (operation != "del_h")):
            print('Inserire operazione valida!')
        else: 
            if operation == "exit":
                break
            if operation=="del_h":
                calculator.del_h()
            else:
                operands_s = input('Operand list [n1 n2 n3 ... ]: ')
                operands_l = operands_s.split(' ')
                operands = []

                for i in range(len(operands_l)):
                    try: operands.append(int(operands_l[i]))
                    except: pass
                    
                if operation=="add":
                    calculator.add(operands)
                elif operation=="sub":
                    calculator.sub(operands)
                elif operation=="mul":
                    calculator.mul(operands)
                elif operation=="div":
                    calculator.div(operands)
        
