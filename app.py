test_str = "ABCDCDC"
  
# initializing substring 
test_sub = "CDC" 
  
# printing original string  
print("The original string is : " + test_str) 
  
# printing substring 
print("The original substring : " + test_sub) 
  
# using count() 
# Frequency of substring in string 
res = test_str.count(test_sub) 
  
# printing result  
print("The frequency of substring in string is " + str(res)) 