Ages = [19,22,19,24,20,25,26,24,25,24]
Ages.sort()
print(Ages)
print("Max = ",max(Ages), "\nMin = ",min(Ages))

#Adding the min age and the max age again to the list
Ages.append(min(Ages))
Ages.append(max(Ages))
print(Ages)
l= len(Ages)

#logic for Median Age
if(len(Ages)%2==0):
  Median1 = Ages[l//2] 
  Median2 = Ages[l//2-1]
  Median = (Median1+Median2)//2
else:
  Median =  Ages[l//2]
print("Median = ",Median)

print("Average = ", sum(Ages)/l)
print("Range = ",max(Ages)-min(Ages))
