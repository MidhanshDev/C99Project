import os
import shutil
import time
path = 'E:/Mithu WhiteHatJr/DummyFolder'
days = 10
seconds = time.time()
seconds = seconds-(days*24*60*60)
print(seconds)
deletedFoldersCount = 0
if os.path.exists(path):
    print('The path exists')
    # rootFolder,folder,files = os.walk(path)
    print(os.walk(path))
    for root_folder,folders,files in os.walk(path):
        # if not shutil.rmtree(path):
        #     print('Path is removed sucessfully')
        # else:
        #     print('Unable to delete the path')
        # deletedFoldersCount = deletedFoldersCount+1
        for file in files:
            # filePath = os.path.join(root_folder,file)
            filePath = 'E:/Mithu WhiteHatJr/DummyFolder/test2.txt'
            print(filePath)
            if not os.remove(path):
                print("The file is sucesfully removed")
            else:
                print("The file is not removed sucessfully")
else:
    print('The path does not exist')
