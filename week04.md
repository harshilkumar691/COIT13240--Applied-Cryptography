# week04


## Ciphertext Only Attack
In most of the attack the attacker knows the algorithm values, so that they can intercept the ciphertext, so if there is a ciphertext only attack then it means that  this cipher is only defeated if the attacker only knows the information

Therefore, this is known as the hardest attack where attacker only knows the algorithm. 

## Known Plaintext Attack
in this type usually attacker knows the algorithms as we earlier saw in ciphertext only attack. Additionally, attacker also knows some other information like plaintext factors (one or more plaintext or ciphertext pairs that are formed with secret key.)

They want to find the the key.

 Overall attacker knows

 1) E(), D() (the cipher)
 2) C0       (ciphertext)
 3) one or more than one plaintext-ciphertext pairs:

        3.1) (P1, C1)          where C1 = E(K, P1)
        3.2) (P2, C2)          where C1 = E(K, P1)
        3.2) (P3, C3)          where C1 = E(K, P1)

Suppose user-A is sending ciphertext to user-B and C1, C2, C3 has a location of a event.

And lets say that 5 days ago "user-A" sent "ciphertext-C1" to "user-B" and attacker intercepted C1, But they did not know P1, One day later P1 was reviewed because it was time sensitive 

## General measures of security

In this week we learned about general security measures in which we come to know that One-time pad is the only unconditionally secure cipher. But, it ois very impracticle because, of it needs very long keys, random keys, and not efficient in exchanging those keys.

And second is Computationally secure:

Suppose there is $15,000 in my bank account and my passowrd for the account is encrypted. now, attacker have an access to that encrypted passord. All he/she need to do is decrypt the file and, get $15,000.

To decrypt the file, he needs 25 computers which costs $18,000, then he can complete the task with time.

According to me this would be the best example to explain the computationally security. 


## Common Metrix for Attacks

Time is measured as number of opersations to decrypt the data of file

### example:
1) In the worst-case of brute-force, K-bit key consumes 2^k decrypt operations

2) if we use 4-bit key it takes 2^4 = 16 decrypt operations

3) if we use 64-bit key it takes 2^64 decrypt operations.

To do this attack attacker needs temporary memory.

## Cryptanalysis of triple-DES and AES
In this week we came across some analysis of triple AES and DES in whcich we came tho know about different ciphers, their methods, their keyspace and time, memory and data required,  to decrypt file or information using the particular method.

For example attacker wants to decrypt a file using DES and he is going to do brute force attack so in this case according to the cryptanalysis the key would be of 56-bits and the time required will be of 2^56 operations 


![3DES and AES analysis](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/b821bdac-985e-4567-ba0f-08523a863505)


During this lecture we came to know that MIMT is 2^57 times faster than brute force attack


### S-AES and AES-128

If we compare S-AES and AES then we can say that simplified AES works on smaller size plaintext/ciphertext like 16 bit key, plaintext. On the other hand, AES can work on not only small but also on 128 bit keys and plaintext. principles of both operations are same. 


## Rows columns and Caesar Question:
### The ciphertext C=lhszlplyueshadlletip was obtained by encrypting the original plaintext P with a Rows/Column Transposition cipher using a 5 digit key K1, followed by encrypting ### the output of the Rows/Columns with a general Caesar cipher with key K2. You can assume the most frequency letter in the plaintext P is 'e'. You also know the first word in the ### plaintext is four letters long. What is the original plaintext P?


### Solution: 
In this question we got a ciphertext "C=lhszlplyueshadlletip" 

The information we got is "there is is a letter "e" in a plaintext which has a most frequency"

If we analyze "C=lhszlplyueshadlletip" cipherext, The most frequent letter we can see is letter "l"

### A - B - C - D - E - F - G - H - I - J - K - L - M - N - O - P - Q - R - S - T - U - V - W - X - Y = Z

we have to now spot the letter "e" and count on what position the "l" is.

"e" is on the 4th position and "l" is on 11th position

11 - 4 = 7

This means the key for caesar cipher is 7 <---- K2 = 7

"C=lhszlplyueshadlletip"

let's decrypt this ciphertext using caesar cipher by shifting the letters on 7 steps left.

x = ealseiernxlatweexmbi

now we have another hint that, to decrypt this "x = ealseiernxlatweexmbi" by rows and column transposition cipher we have 5 digit key.
lets assume K1 = 1,2,3,4,5

divide  "x = ealseiernxlatweexmbi" into pair of 4: 

eals

eier

nxla

twee

xmbi


![WhatsApp Image 2024-04-08 at 4 28 06 AM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/51a15080-308b-4466-90e1-9ef71275e2af)



## Exculsive OR
In XOR, if the inputs are similar then the output will be "0"

If inputs will be different then the output will be "1" 

have alook on picture given below :

![XOR](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/b769d733-5348-49b0-b3ca-fab86556f4d0)


For example:

![XOR 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/b35090d8-3898-448f-b115-8d5e63cba3d4)



### simple block cipher

![Block cipher table](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/a8e244ad-f31e-476d-b460-a3bea29324a2)

look on the above given table

And now, just to understand how the encryption and decryption work in here we will take an example.  

### Encryption
(key = 010, plaintext = 01000) ----> ciphertext = 10011

Find the key "010" in the row and search for plaintext "01000" in the column "p" then match both rows and columns where they meets the cell in which tey meet is the ciphertext.

### Decryption
(key = 010, Ciphertext = 10011) -------> Plaintext = 01000

Find the key "010" in the row and search for ciphertext 10011 in the column of "010" then match it with column " the number "P" the number found will be the plain text.



## CBC Mode of Operation

![CBC mode operation diagram](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/46ec3a16-da7d-42f7-993d-1e7f90029768)

In this method we can see there are 15-bits plaintext and 15-bits ciphertext and a 5-bits Initialization vector(IV)

To perform encryption using this medthod we have to make use of the table given below

![Block cipher table](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/a8e244ad-f31e-476d-b460-a3bea29324a2)

lets take a plaintext(P), IV, and and a key 

P = 00010 00011 00110
K = 001 ----------------> key is 7 bit
IV = 01010

To make encryption easier divide "P" into 3 parts
P1 = 00010

P2 = 00011

P3 = 00110

### Step 1
now lets take P1 and perform XOR with IV 

P1 = 00010

IV = 01010

XOR= 01000

encrypt the solution of "XOR = 01000" in the above given table.

key = 001 
### ciphertext (C1) = 11011

### step 2
P2 = 00011

C1 = 11011

XOR= 11000

key = 001
### Ciphertext (C2) = 01011

### Step 3
P3 = 00110

C2 = 01011

XOR= 01101

key = 001
### Ciphertext (C3) = 00111


### ciphertext is = 11011 01011 00111


## CTR Mode of Operation

![CTR mode of operation](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/e0c7ecb6-8bda-41b9-8e9a-e99296aea3d3)


This mode of operation is something similar to the example we solve before but "we need to create "CTR" for each P1, P2, and P3

to solve this example we need the table given below.

![Block cipher table](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/4a66cbaf-04e3-4449-845f-50a6f5f3460c)


Follow the steps given below:

![WhatsApp Image 2024-04-08 at 6 10 47 AM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/8106b1d8-1354-420f-a1f5-3ce745eaee69)


![WhatsApp Image 2024-04-08 at 6 11 30 AM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/3d789989-cef4-4c60-a93a-b860565a1f33)






 




