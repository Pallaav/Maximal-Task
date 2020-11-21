r = 256                                                                         #r =no of character 

# max dist. char in a string 
def mdc(s, n):                                                                  # mdc = max distinct char.
	c = [0] * r                                                             #set count of each char to 0
	for p in range(n):                                    
		c[ord(s[p])]+= 1                                                #if the char is found again then increase the count
	md = 0
	for p in range(r):                                                      #Set maxiumum distinct char to 0 initially
		if (c[p] != 0): 
			md = md + 1	
	return md

def ssdc(s):                                                                     #smallest substring with distinct character = ssdc
	n = len(s)	                                                         # len is used to cal size of string  
	md = mdc(s, n) 
	f = n	

	for i in range(n):                                                      #finding all such substring
		for m in range(n): 
			sub = s[i:m] 
			t = len(sub)                                            #lenght of substring 
			sub_dist = mdc(sub,t)
			if (t < f and md == sub_dist): 
				f = t 
	return f 

s = input("")
l = ssdc(s)
print(l)
