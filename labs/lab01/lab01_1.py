import json

class Calculator:
    def __init__(self):
        pass

    def add(self, op1, op2):
        res = op1 + op2
        print(res)

        new_op = {"operation":"add","operand1":op1,"operand2":op2,"result":res}
        f = json.load(open("lab01_1.json"))
        f["calculator_history"].append(new_op)
        json.dump(f, open("lab01_1.json", "w"))
    
    def sub(self, op1, op2):
        res = op1 - op2
        print(res)

        new_op = {"operation":"sub","operand1":op1,"operand2":op2,"result":res}
        f = json.load(open("lab01_1.json"))
        f["calculator_history"].append(new_op)
        json.dump(f, open("lab01_1.json", "w"))

    def mul(self, op1, op2):
        res = op1 * op2
        print(res)

        new_op = {"operation":"mul","operand1":op1,"operand2":op2,"result":res}
        f = json.load(open("lab01_1.json"))
        f["calculator_history"].append(new_op)
        json.dump(f, open("lab01_1.json", "w"))
    
    def div(self, op1, op2):
        if op2==0:
            print("Errore: divisione per zero")
            new_op = {"operation":"div","operand1":op1,"operand2":op2,"result":"Error: division by 0"}
            f = json.load(open("lab01_1.json"))
            f["calculator_history"].append(new_op)
            json.dump(f, open("lab01_1.json", "w"))
        else:
            res = op1 / op2
            print(res)

            new_op = {"operation":"div","operand1":op1,"operand2":op2,"result":res}
            f = json.load(open("lab01_1.json"))
            f["calculator_history"].append(new_op)
            json.dump(f, open("lab01_1.json", "w"))

if __name__=="__main__":
    calculator = Calculator()

    while True:
        operation = input('New operation. Choose one in [add, sub, mul, div, exit]: ')
        if ((operation != "add") & (operation != "sub") & (operation != "mul") & (operation != "div") & (operation != "exit")):
            print('Inserire operazione valida!')
        else: 
            if operation == "exit":
                break

            operand1 = input('First number: ')
            operand2 = input('Second number: ')

            try: operand1 = int(operand1)
            except: 
                print("Operands must be numbers!")
            else:
                try: operand2 = int(operand2)
                except: 
                    print("Operands must be numbers!")
                else: 
                    if operation=="add":
                        calculator.add(operand1, operand2)
                    elif operation=="sub":
                        calculator.sub(operand1, operand2)
                    elif operation=="mul":
                        calculator.mul(operand1, operand2)
                    elif operation=="div":
                        calculator.div(operand1, operand2)
    
