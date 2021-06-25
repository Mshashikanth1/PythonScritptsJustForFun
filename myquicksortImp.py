#key job is to partition the elements in an array so that
#thr partitioning will be done such that all the elements less than the pivot element will be one side and all the elements grater than will 
#be other side
# and partitioning on every element of the list will make the array sorted

def quicksort(arr,l,h):
    if l<h:
      part_ind=partition(arr,l,h)
      quicksort(arr,l,part_ind-1)  #partition arrount the smaller sub-partition arryay
      quicksort(arr,part_ind+1,h)   #partition arround the bigger subpartioin array
def partition(arr,l,h):
  pivot_ele=arr[h]
  i=l  #i and incresses only when the elements less than pivot will be swapped
  j=i+1
  while j<h:
        if arr[j]<pivot_ele:
           arr[i],arr[j]=arr[j],arr[i]
           i+=1
        j+=1
  arr[i],arr[h]=arr[h],arr[i]
  return i
