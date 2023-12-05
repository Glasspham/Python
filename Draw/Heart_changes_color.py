import time
import os
import random
import subprocess

list1=["    **       **   ","  *      *      * "," *               *","  *             * ","   *           *  ","     *       *    ","       *   *      ","         *        "]
list2=["                  ","      **   **     ","    *    *    *   ","    *         *   ","      *     *     ","         *        ","                  ","                  "]

while True:
    try:
        os.system("cls")
        subprocess.run(f"color {random.choice(['a','b','c','d','e','f'])}", shell=True)
        for i in list1:
            for j in range(random.randint(1,4)):
                num=random.randint(0, len(i)-1)
                while i[num]!=" ":
                    num=random.randint(0, len(i)-1)
            i=i[:num]+"."+i[num+1:]
            print(i)
        time.sleep(0.25)
        os.system("cls")
        subprocess.run(f"color {random.choice(['a','b','c','d','e','f'])}", shell=True)
        for i in list2:
            for j in range(random.randint(0,2)):
                num=random.randint(0, len(i)-1)
                while i[num]!=" ":
                    num=random.randint(0, len(i)-1)
            i=i[:num]+"."+i[num+1:]
            print(i)
        time.sleep(0.25)
    except Exception as ex:
        print(ex)