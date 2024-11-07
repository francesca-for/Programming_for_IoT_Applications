import json
import datetime

class Catalog:
    def __init__(self):
        pass

    def searchByName(self, devices_list, name):
        res_index_list = []
        for i in range(len(devices_list)):
            if (devices_list[i])["deviceName"] == "name":
                res_index_list.append(i)
        return res_index_list

    def searchByID(self, devices_list, id):
        res_index_list = []
        for i in range(len(devices_list)):
            if (devices_list[i])["deviceID"] == id:
                res_index_list.append(i)
                break
        return res_index_list

    def searchByService(self, devices_list, service):
        res_index_list = []
        for i in range(len(devices_list)):
            for s in (devices_list[i])["availableServices"]:
                # print(s+" - "+service)
                if s == service:
                    res_index_list.append(i)
                    break
            #try: d["availableServices"].index("service")   # Perchè non posso cercare direttamente se elemento esiste
            #except: pass    # print("--- no ---")
            #else: print(d+"\n")
        return res_index_list

    def searchByMeasureType(self, devices_list, measType):
        res_index_list = []
        for i in range(len(devices_list)):
            for mt in (devices_list[i])["measureType"]:
                if mt == measType:
                    res_index_list.append(i)
                    break
        return res_index_list

    def insertDevice(self, devices_list, new_id):
        new_name = input("Name: ")
        
        new_meas_type_str = input("Measure type/s (type1 type2 ...): ")
        new_meas_type_list = new_meas_type_str.split(' ')
        new_serv_str = input("Available services (serv1 serv2 ...): ")
        new_serv_list = new_serv_str.split(' ')
        new_serv_det_l = []
        # TODO: finire di implementare

        new_dev = {"deviceID":new_id, "deviceName":new_name, "measureType":new_meas_type_list, "availableServices":new_serv_list,
                "servicesDetails":new_serv_det_l, "lastUpdate": str(datetime.date)}
        
        res = c.searchByID(devices_list, new_id)
        if res == []:
            devices_list.append(new_dev)
        else: devices_list[res[0]] = new_dev

        return devices_list
    
    def printDevices(self, devices_list, res, errorMessage):
        if res == []:
            print(errorMessage)
        else: 
            for x in res: print(devices_list[x])


if __name__=="__main__":
    c = Catalog()
    catalog_dict = json.load(open("lab01_3_catalog.json"))
    devices_list = catalog_dict["devicesList"]
    print("Welcome to your catalog\n")

    while True:
        action = input("Select an action (number 1 to 7):\n1) searchByName\n2) searchByID\n3) searchByService\n4) searchByMeasureType\n5) insertDevice\n6) printAll\n7) exit\n")
        res = []
        try: act_num = int(action)
        except: print("Input not valid")
        else: 
            if act_num==1: # searchByName
                name = input("Name: ")
                res = c.searchByName(devices_list, name)
                c.printDevices(devices_list, res, "Unable to find any device with name = "+name)

            elif act_num==2: # searchByID
                try: id = int(input("ID: "))
                except: print("ID has to be a numerical")
                else:
                    res = c.searchByID(devices_list, id)
                    c.printDevices(devices_list, res, "Unable to find any device with name = "+name)
           
            elif act_num==3: #searchByService
                serv = input("Service: ")
                res = c.searchByService(devices_list, serv)
                c.printDevices(devices_list, res, "Unable to find any device for "+serv+" service")
           
            elif act_num==4: # searchByMeasureType
                measType = input("Type of measure: ")
                res = c.searchByMeasureType(devices_list, measType)
                c.printDevices(devices_list, res, "Unable to find any device for "+measType+" measure")
           
            elif act_num==5: # insertDevice
                try: new_id = int(input("ID of the new device: "))
                except: print("ID has to be a numerical")
                else: 
                    devices_list = c.insertDevice(devices_list, new_id)
                    catalog_dict["devicesList"] = devices_list
                    modified = True
         
            elif act_num==6: # printAll
                print("Full catalog:\n"+catalog_dict)
          
            elif act_num==7: # exit
                if modified == True:
                    json.dump(catalog_dict, open("lab01_3_catalog.json", "w"))
                break
          
            else: print("The selected action does not exist") 