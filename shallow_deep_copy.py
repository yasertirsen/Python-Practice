l1 = [1,2,3]
l2 = l1 #ref or shallow copy
copy_l1 = l1[:] # deep copy
print('orginal ', l1)
print('copy ', copy_l1)
copy_l1[0] = 'q'
print(l1)
print(copy_l1)
print('ref', l2)