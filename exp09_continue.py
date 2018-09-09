# continue will skip the loop and go to the beginning of the next iteration . 
# break on the other hand breaks the loop all together .
numbersTake=[2,5,9,21]

print("Here are the numbers that are still available");

for n in range(1,25):
    if n in numbersTake:
        continue
    print(n)        