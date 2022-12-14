def linearSearch(arr,size,key):
    for i in range(size):
       if arr[i]==key:
        return 1
    return 0
if __name__ =="__main__":
    page_number = 20,30,40,50,60
    key = input("Enter your input to be searched70")
    if linearSearch(page_number,len(page_number),key) ==1:
        print("search found")
    else:
        print("search not found")