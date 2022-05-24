#SID: 2007102
import random 
#allows me to generate random numbers 


def interpolationSearch(array, element): #function for interpolation search
    print("This is interpolation Search") #users benefit

    interpForm = 0
    start = 0
    end = len(array) -1 #python index starts from 0
    #these variables are used in interpolation search formula
    NumOfComparison = 0
    #setting number of comparison counter = 0 

    while (start <= end): #this runs until array is empty 

        interpForm = start + ((end - start) // (array[end] - array[start]) *
                    (element - array[start])) #formula for interpolation search is used and saved to variable 'interpForm' 
        
        NumOfComparison = NumOfComparison +1 #counter to note down number of comparisons used

        if element == array[interpForm]: # checks is element has been correctly
           return NumOfComparison #number of comparison occured is returned if search target has been found 
          

        if element < array[interpForm]: #checks which side is no longer needeed 
            NumOfComparison = NumOfComparison +1
            end = interpForm - 1 #removes side not needed 
        else:
            NumOfComparison = NumOfComparison +1
            start = interpForm + 1 #removes side not needed

    print("Number of comparisons {}".format(NumOfComparison))
    return -1 #'-1' is returned if search is unnsuccesful



def binarySearch(array, element): #function for binary search
    print("This is Binary Search")
    mid = 0
    start = 0
    end = len(array) -1
    #these variables are used in binary search formula
    NumOfComparison = 0
    #setting number of comparison counter = 0 

    while (start <= end):

        mid = (start + end) // 2  #formula to find the middle element 
       
        NumOfComparison = NumOfComparison +1 #counter to note down number of comparisons
        if element == array[mid]:# checks whether array is in middle element 
            return NumOfComparison #Search ends when search target is found

        if element < array[mid]:#checks which side is no longer needed and can be removed 
            NumOfComparison = NumOfComparison +1
            end = mid - 1 #removes half which is not of interest 
        else:  #checks which side is no longer needed and can be removed 
            NumOfComparison = NumOfComparison +1 
            start = mid + 1 #removes half which is not of interest

    return -1 #'-1' is returned to indicate an unnsuccesful search 

#####################################Hybrid Search#########################################

def interpolationBinarySearch(array, element): #function for hybrid search
    print("This is hybrid Search which includes a combination of interpolation and binary search")

    interpForm = 0
    start = 0
    end = len(array) -1
    NumOfComparison = 0
    mid = 0 
    #these variables are used in hybrid search formula

    while (start <= end):
    
        interpForm = start + ((end - start) // (array[end] - array[start]) *
                    (element - array[start])) #formula for interpolation search is used and saved to variable 'interpForm'

        NumOfComparison = NumOfComparison +1 #counter to note down number of comparisons used
        if element == array[interpForm]: # checks whether prediction is correct 

            return NumOfComparison
         
        if element < array[interpForm]:

            if round((end-start+1)/4)<=end-interpForm+1: #checks whether the prediction is a 'bad' prediction. 
                                                         #A bad prediction is defined as: more than 3/4 of the remaining array is left after a prediction
                NumOfComparison = NumOfComparison +1
                end = interpForm - 1
           
            else: # if remaining array is more than 3/4
                # A binary search is used when the predicted key leaves 3/4 of the array left
               
                 mid = start + ((end - start) // 2) #formula to find the middle element 
           
                 print("Number of comparisons {}".format(NumOfComparison))
                 
                 NumOfComparison = NumOfComparison +1 #counter to note down number of comparisons used NEW
                 if element == array[mid]: #checks whether middle element is search target 
             
                     return NumOfComparison #search target is found in middle element
                 
                 if element < array[mid]:
                     NumOfComparison = NumOfComparison +1
                     end = mid - 1
                 else:
                     NumOfComparison = NumOfComparison +1
                     start = mid + 1
        else:
            
            start + ((end - start) // 2)
            
            if round((end-start+1)/4)<=interpForm - start + 1: #checks whether the prediction is a 'bad' prediction.
                NumOfComparison = NumOfComparison +1
                start = interpForm + 1
          
            else: 

                 mid = start + ((end - start) // 2)

                 NumOfComparison = NumOfComparison +1
                 if element == array[mid]:
                     return NumOfComparison

                 if element < array[mid]:
                     NumOfComparison = NumOfComparison +1
                     end = mid - 1
                     
                 else:
                     NumOfComparison = NumOfComparison +1
                     start = mid + 1
    return -1

def randomArrayGenerator(arraylen):#function to generate a random array with the array length as a parameter 
    array = []
    for x in range (arraylen): 
        array.append(random.randint(1,arraylen)) #generate random numbers between 1 and 'arraylen' which is given as a parameter when function is called
        array.sort() #sorts array as binary and interpolation search only works with sorted arrays 
    return array

array = randomArrayGenerator(100) #calling function with the parameter being the desired array length

element = random.choice(array) # The search target is randomised and is chosen from the randomly generated array

print(interpolationSearch(array, element)) #calls interpolation search function
print(binarySearch(array, element)) #calls binary search function
print(interpolationBinarySearch(array, element)) #calls hybrid search function
