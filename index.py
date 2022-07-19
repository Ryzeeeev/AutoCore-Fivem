import glob
import os
import shutil


directory = "AllVehicle"
NewDirector = "CoreCreation"

def createFolder(directory):
    try:
        if not os.path.exists(directory):
            os.makedirs(directory)
            print("Create folder ("+directory+")")
    except OSError:
        print ('Error: Creating directory. ' +  directory)
        

def main():
    os.system('cls')
    print("[Auto Core Fivem]")
    print("\n\n")
    print("[1] Show all véhicles and create Core")
    option = int(input("Choose the option? "))

    if option == 1:
        os.system('cls')

        roption = input("Mettre en core (Y/N) ? ")
        if roption == "Y":
            os.system('cls')
            createFolder('CoreCreation/')
            createFolder('CoreCreation/stream/')
            createFolder('CoreCreation/data/')

            file = open('CoreCreation/fxmanifest.lua','a+')
            file.write("""
    -- Ryze Creation Core
    fx_version('bodacious')
    game('gta5')

    files({
        'data/**/carcols.meta',
        'data/**/carvariations.meta',
        'data/**/contentunlocks.meta',
        'data/**/handling.meta',
        'data/**/vehiclelayouts.meta',
        'data/**/vehicles.meta'
    })

    data_file('CONTENT_UNLOCKING_META_FILE')('data/**/contentunlocks.meta')
    data_file('HANDLING_FILE')('data/**/handling.meta')
    data_file('VEHICLE_METADATA_FILE')('data/**/vehicles.meta')
    data_file('CARCOLS_FILE')('data/**/carcols.meta')
    data_file('VEHICLE_VARIATION_FILE')('data/**/carvariations.meta')
    data_file('VEHICLE_LAYOUTS_FILE')('data/**/vehiclelayouts.meta')
                    """)
            file.close()
            roptionContinuer = input("Are you sure ? (Y/N) ? ")
            if roptionContinuer == "Y":
                    for filename in os.scandir(directory):
                        createFolder('CoreCreation/stream/'+filename.name)
                        createFolder('CoreCreation/data/'+filename.name)
                        for ryzeFileName in os.listdir(directory+"/"+filename.name):
                            if ryzeFileName.endswith(".meta") or ryzeFileName.endswith(".xml") :
                                shutil.copy(directory+"/"+filename.name+"/"+ryzeFileName, NewDirector+"/data/"+filename.name+"/"+ryzeFileName)
                                os.scandir(directory).close() 
                                os.scandir(directory+"/"+filename.name).close() 

                    for filename in os.scandir(directory):
                        for ryzeFileName in os.listdir(directory+"/"+filename.name+"/stream/"):
                                shutil.copy(directory+"/"+filename.name+"/stream/"+ryzeFileName, NewDirector+"/stream/"+filename.name+"/")
                                os.scandir(directory).close() 
                                os.scandir(directory+"/"+filename.name+"/stream/").close() 
                    print("[Auto core FiveM by Ryze] All is finish")

if __name__ == "__main__":
        main()
