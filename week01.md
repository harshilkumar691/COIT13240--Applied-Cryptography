# Week 1 

[Return to contents](./README.md)

# This week consists of 3 concepts and 2 ciphers 
1. Security concepts
2. Cryptography concepts
3. Cryptography notation and terminology
4. Caesar Cipher (encryption and decryption)
5. Monoalphabetic Cipher 

## 1.security concepts:-
   Given below are the six protection methods used for the srcurity of the encrypted data 
   
                  1.1 Confidenttiality:
                  
                  Confidentiality make sure that the only the authorised person/parties can access the confidential data. We can take a Bank as an example, Only i can access the 
                  confidential data pf my bank account. Data like my bank balance, ,my personal profile etc.
                  
                  1.2 Integrity: 
                  
                  Intigrity ensure that no  one can modify the information or message if it is done then the receiver can detect all the modification and also no unauthorised 
                  person/parties can access the confidential information using fake identity. the best example for Integrity would be a bank. Suppose I have a student-account in a 
                  bank and only i can access it whenever I want to. No one can use my fake identity to access my account, Only I am authorised to modify my personal details or make 
                  any transaction. Suppose If bank's server or my account is hacked by someone and if they make changes of my personal data or take out some money. I can 
                  immidiately get a notification on my phone (message or email), so i can see all the modification done by hacker. 
                  
                  1.3 availability: 
                  Availability ensure that data can be accessible by the authorised person whenever they needed. Best example for this is a online shopping websites, If I have 
                  registered on that site and I have my Id and Password it means I am authorised only when I log-in into it and I can see and get access on all my purchased items 
                  and get access on my profile. 
                  
                  1.4 Authentication: 
                  
                  Auhtentication always check the Itedtity of the person (example: id and password) in its log system. 
                                          
                  1.5 Authorisation:
                  
                  Authorisation provides access to the particular information or website after authontication is checked.
                  
                  1.6 Accounting: 
                  Accounting provide logs of the files or server(who used, how many times used, when used, date and time of usage), And provide a summary report for history and 
                  security purpose.  



## 2. Cryptography concepts:
                      2.1 Encryption for confidiality:
                      
                        To make sure that the confidential information is only visible to the authorised person/parties, Message or inforamtion is encrypted by which if 
                        anyone(unotherised person) can see only the encrypted datd, but only the authorised person can se the decrypted data. lets take an example: "6DJ3Q11QBN" 
                        this is an encrypted message anyone(unauthorised) can see this message, But only authorised person can see it as "31chillist" it means "31 Chilli St"

                          Screenshot given below shows the simple diagram shows the encryption for confidentiality.


![Model of Encryption of Confidentiality](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/e9e563a7-2c7c-4d68-aa12-7553c03b4259)  


In the above diagram, User-A and User-B want to send or share a message confidentially. User-A has a plaintext(readable) message, User-A will now encrypt the message using a key thenafter user a will get a ciphertext as an output. It is then sent to User-B. User-C is an attacker and in this case attacker can see only the ciphertext not a plaintext. When User-B receives the ciphertext, User-B decrypts using correct key and algorithm, After doing this User-B can see the plain text.

In the above diagram the aim of the attacker is to identify plaintext or a key (There are 2 types: (A) Symmetric key: Key1 and key2 are identical

                                                                                                   (B) Public key: Key1 is the public key of B and key 2 is the private key of B 
                                                                                                                   (Asymmetric key)).


# There are some cryptographic terms need to understand.
1) Plaintext----->	Original message
2) Ciphertext----> 	Encrypted message 
3) Encryption---->	Convert from plaintext to ciphertext (enciphering)
4) Decryption---->	Restore the plaintext from ciphertext (deciphering)
5) key----------->	Information used in cipher known only to sender/receiver
6) Cipher ------->	A particular algorithm (cryptographic system)
7) Cryptography--> 	Study of algorithms used for encryption
8) Cryptanalysis->	Study of techniques for decryption without knowledge of plaintext
9) cryptology---->	Areas of cryptography and cryptanalysis





## 3. Cryptography notation and terminology: 

 ![image](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/8897fe68-50f3-462f-b861-83c04fc61916)
                     
 


## 4. Caesar cipher
### Encryption
Caesar cipher is used to encrypt a message or information. A key is used to to encrypt and decrypt a message, suppose a Jhon is sender and Bob is receiver. Jhon is sending an encrypted message "caesar" to Bob, And Jhon is using a secret key=3 to encrypt a message. To decrypt the message Bob must know the secret key used to encrypt the message. So Caesar cipher has a symmetric key (The key is similar for bothe Jhon and Bob).

Lets take an example to encrypt a message "caesar"

a  -  b  -  c  -  d  -  e -   f  -  g  -  h  -  i  -  j  -  k  -  l  -  m  -  n  -  o  -  p  -  q  -  r  -  s  -  t  -  u  -  v  -  w  -  x  -  y - z


### Example 1
Plaintext Messege: caesar           
key: 3
Encrypted messege: fdhvdu

steps:
A) To encrypt "caesar" lets focus on the first letter "c". we need to find "c" in the above given alphabets. After finding "c" we need to move 3 steps ahead. we are moving 3 steps ahead because the key is 3, The third step is "f"; So, the encrypted word for "c" is "f".  

                          c = f
                          
B) To encrypt second letter "a". lets find the "a" in the above given alphabets, And move 3 steps ahead. The third step is "d". the enrypted word for "a" is "d"

                          a = d
                          
C) To encrypt third letter "e". lets find the "e" in the above given alphabets, And move 3 steps ahead. The third step is "h". the enrypted word for "e" is "h"

                          e = h
                          
D) To encrypt fourth letter "s". lets find the "s" in the above given alphabets, And move 3 steps ahead. The third step is v. the enrypted word for "s" is "v"

                          s = v
                          
E) To encrypt Fifth letter "a". lets find the "a" in the above given alphabets, And move 3 steps ahead. The third step is d. the enrypted word for "a" is "d"

                          a = d
                          
F) To encrypt sixth letter "r". lets find the "r" in the above given alphabets, And move 3 steps ahead. The third step is u. the enrypted word for "r" is "u"

                          r = u
                          

we can change the key if we want the method will be the same, as shown in the above example. only the change will be the key if we are using key=5 so we need to move 5 steps ahead, if we are using key=2 then we need to move 2 steps ahead. 

### Example 2
a  -  b  -  c  -  d  -  e  -  f  -  g  -  h  -  i  -  j  -  k  -  l  -  m  -  n  -  o  -  p  -  q  -  r  -  s  -  t  -  u  -  v  -  w  -  x  -  y  -  z


lets assume key=25 for messege:"caesar"

encrypted messege: bzdrzq


A) To encrypt first letter "c". lets find the "c" in the above given alphabets, And move 25 steps ahead. The 25th step is b. the cenrypted word for "c" is "b"

like wise when you are countion a larger number like 25. like, in this example 23rd position is "z" and we do not have any alphabet after "z" so we need to start and continue counting from first letter "a", it means 24th letter is "a" and 25th letter is "b".

                             c = b
                             
B) To encrypt second letter "a". lets find the "a" in the above given alphabets, And move 25 steps ahead. The 25th step is z. the enrypted word for "a" is "z"

                             a = z
                             
C) To encrypt third letter "e". lets find the "e" in the above given alphabets, And move 25 steps ahead. The 25th step is d. the enrypted word for "e" is "d" 

                             e = d
                             
D) To encrypt fourth letter "s". lets find the "s" in the above given alphabets, And move 25 steps ahead. The 25th step is r. the enrypted word for "s" is "r" 

                             s = r
                             
E) To encrypt fifth letter "a". lets find the "a" in the above given alphabets, And move 25 steps ahead. The 25th step is z. the enrypted word for "a" is "z" 

                             a = z
                             
F) To encrypt sixth letter "r". lets find the "r" in the above given alphabets, And move 25 steps ahead. The 25th step is q. the cenrypted word for "r" is "q"

                             r = q


Technically we can get messege encrypted using keys 0 to 26, But key=0 and key=26 always give the same messege(plaintext). So we can say thet key=1 to key=25 can give us unique encrypted messege.

When we go beyond 26. example key 27 then we will get the output same as key=1, if we use key=28 then we will get the output similar to key=2. So we key 1 to key 25 can give us the unique encrypted messege.


### Decryption
in the above example we saw how we can encrypt the messege, In this example we will decrypt the messege which we have encrypted using key=3


a  -  b  -  c  -  d  -  e  -  f  -  g  -  h  -  i  -  j  -  k  -  l  -  m  -  n  -  o  -  p  -  q  -  r  -  s  -  t  -  u  -  v  -  w  -  x  -  y  -  z


encrypted messege: fdhvdu

Key=3

plaintext:- caesar

In the encryption example we saw that, if we are using key=3 for encryption then we should move 3 steps to the right. 
In decryption if we are using key=3 then we should shift 3 step to the left.

steps:

A) To decrypt first letter "f". lets find the "f" in the above given alphabets, And move 3 steps left(back). The 3rd step is c. the decrypted word for "f" is "c"

                                 f = c
                                 
B) To decrypt second letter "d". lets find the "d" in the above given alphabets, And move 3 steps left(back). The 3rd step is a. the decrypted word for "d" is "a"

                                 d = a
                                 
C) To decrypt third letter "h". lets find the "h" in the above given alphabets, And move 3 steps left(back) . The 3rd step is e. the decrypted word for "h" is "e"

                                 h = e
                                 
D) To decrypt fourth letter "v". lets find the "v" in the above given alphabets, And move 3 steps left(back) . The 3rd step is s. the decrypted word for "v" is "s"

                                 v = s
                                 
E) To decrypt fifth letter "d". lets find the "d" in the above given alphabets, And move 3 steps left(back). The 3rd step is a. the decrypted word for "d" is "a"

                                 d = a
                                 
F) To decrypt sixth letter "u". lets find the "u" in the above given alphabets, And move 3 steps left(back). The 3rd step is r. the decrypted word for "d" is "r"

                                 u = r


By following these steps we can come to know that the decrypted messege is "caesar"

### in the above given example we can see that we need to do it manually by hand but we can also use a simple commnds to encrypt and decrypt messege.
### In this case we know that the key is "3"
![encryption and decryption in python (Caesar cipher)](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/5078c9f1-3d6c-4922-98a2-4f163179e6d6)

pycipher.Caesar(3).encipher("caesar") ----> This command is used to encrypt a message where "encipher" indicates that we wnat to encrypt, "(3)" indicate the key is 3, "("caesar")" indicates the plaintext which we want to encrypt.


pycipher.Caesar(3).decipher("FDHVDU") ------> This cooman is used to decrypt message where "decipher" is used to decrypt a message, "(3)" indicate the key is 3, "("FDHVDU")" indicates the encrypted text which we want to decrypt.


## Monoalphabetic (Substitution) Cipher.

In monoalphabetic cipher is a form of symmetryc encryption because the key which is used to encrypt the messege, the same key will be used to decrypt messege.

To encrypt data, First we need to write the alphabets in order in a horizontal line and below that we need to randomly place the alphabets which should not be in order each letter should be used only once. (see below example)

### a - b - c - d - e - f - g - h - i - j - k - l - m - n - o - p - q - r - s - t - u - v - w - x - y - z     <----- Alphabet 
### y - v - g - j - c - a - l - p - r - b - f - d - h - t - w - z - x - m - o - k - n - q - s - u - e - i     <----- Key


Line 2(key) is a unique key which is a symmetric key. It is used to encrypt and decrypt the data. Key can be generated or made by randomly arranging the alphabet letters and each letter is used once.














                                 





                  
