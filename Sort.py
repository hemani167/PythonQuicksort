partition(a,beg,end):
	left=beg
	loc=beg
	right=end
	flag=0
	while not flag:
		while(a[loc]<a[right] and loc!=right):
			right=right - 1
		if(loc==right):
			flag=1
		elif(a[loc]>a[right]):
			temp=a[right]
			a[right]=a[loc]
			a[loc]=temp
			loc=right
		while(a[loc]>a[left] and loc!=left):
			left= left + 1
		if(loc==left):
			flag=1
		elif(a[loc]<a[left]):
			temp=a[loc]
			a[loc]=a[left]
			a[left]=a[temp]
			loc=left
	return loc
def quick_sort(a,beg,end):
	if(beg<end):
		loc=partition(a,beg,end)
		quick_sort(a,beg,loc-1)
		quick_sort(a,loc+1,end)




arr = [3,5,1,66,55,23]
print "Before sorting"
print arr
print "After sorting"
quick_sort(arr,0,5)
print arr
