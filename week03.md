# Week03

In week03 we learned aims and knowledge of the attacker and what attackers knows and what attackers do such as they can intercept and modify the data. also what are the users perspective is for instance confidentiality and authenticity

### Confidentiality: 
Suppose "user1" is sending a message to "user2" between these two the attacher cannot decrypt or attacker cannot come to know what the data is.

### Authentication: 
Suppose "user1" is sending the information "user2" so user2 can come to know that the information is sent by the "user1" and user2 can also know about any modification made after sending and before receiving.

In this week we learned about the brute force attempts that how much attempts do the attacker needs to make for different cases (worst cas, average case, best case) for different bits.

For example:  If we talk about 3 bits the possible keys are (000, 001, 010, 011, 100, 101, 110, 111) in this case worst case attempts attacker need to make will be "8" and around half of it will be the avergae case attempts. best case attempts will be 1 or 2 attempts


Using "openssl" we learned that how we can see that how much our computer is in decrypting the messages by running a simple command 

openssl speed aes-128-cbc

We did this using "aes 128 bit key", And we found that our computer did many decryption in a 3secs at a time. After the command stoped working at the end we come to know that our computer decrypted 18,527,749 messages in just 3 seconds

![image](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/a4c9b2d5-7efa-45a0-b230-3404f892f405)


### Block Cipher
Block ciphers are typically 64 or 128 bits 

If we take a 4 bits of plaintext and the cipher will encrypt it using the K bits as shown in figure below (the key and block size are not similar, sometimes we can see it same but it is co-incidence). The size of ciphertext and plaintext will be the same; For instance, if we have a plaintext of 64 bits so the encrypted ciphertext must be of 64 bits. the key can be of different size.   

### working of block cipher
![block cipher working](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/917c5f34-3485-446b-8eb7-79e454ffaffd)


### Convert english alphabets into binary
Often ASCII needs 7 bits, but we represent in it in 8 bit value and we put 0 in front, because in most cases our system runs on 8 bits value and UTF always put 8 bits in front. 

![table binary](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/d5ccb050-23d3-4df5-93cf-97c34347a710)

In this suppose if we have to convert "H" in ascii value then we can Read "H" as:

H = 1001000 this is a seven bits value but as I mentioned earlier in  ost cases on computer runs on 8 bits and even utf-8 puts 0 at the start of 7 bits to make it 8 bits so the ascii value for "H" will be 

H = 01001000


### example question for brute force attack 

During this week we learned to solve the question of bruteforce attack 

we have intercepted a 1MB encrypted file and want to find the corresponding plaintext. we know the encryption used and you have a computer that can decrypt the file at a rate of 10^11 decrypts per second. the algorithm uses a 80-bit block cipher and 50-bit key. what is the worst case time, t, to find the plantext using a brute-force attack.


options: select right answer

1)  1 hour < t greater then or equal to 1 day
2) i day < t greater then or equal to 1 month
3) 1 month < t greater then or equal to 1 year
4) 1 year < t greater than or equal to 1 century
5) t > 1 century

Ans:-

To solve this we have to first find that how many possible key values are there

There are 50 bits key (if we are using binary values there are 2^n values. So, in this case we have 2^50 possible keys)

This means we have to do 2^50 decryptions.

To find out the time we have no divide quantity by time

time  = 2^50 / 10^11 decrypts per seconds

      = 11,259 secs
      
      = 187.6 mins
      
      = 3.12 hours  approximate answer is (1 hour < t greater then or equal to 1 day)

 where 1 MB file = 1,000,000 bytes  OR  (1,048,576 bytes)
     
     
 80-bit block    = 8,000,000 bits / 80 bits = 1,00,000 blocks
     

### DES in OpenSSL
The key length of des should be 64 bits to encrypt and 56 bits is effective secure key length. 

How to choose a key? 

we can randomly choose key

To encrypt a file using DES using linux machine 

1) create a .txt file (nano des.txt)

2) run (openssl rand 8) this will create a key

![des 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/2a300d8d-816b-4c03-a8ad-1d2cb022248e)
   

![image](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/55c667a5-e862-428c-bdc3-08f8606ca0ce)


3) use (openssl rand -hex 8) this will create random key

     something like this :- f1e3d7ba7d06327a
   

![des 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/9cd30302-2075-40c4-9eea-8e4dcf0bca9a)


4) use given below code to encrypt the file.

   ![des 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/1e9ccf47-cb28-416d-b6cb-101065503f8b)


In the above given code "enc" is used to encrypt. 

"-des" is a program.

"-in des.txt" is in tinput file which we want to encrypt.

"-out des.enc" that we expect to be ncrypted with .enc file.

"-k f1e3d7ba7d06327a" is the key that we got in (step 3) 


after running this code if you don't se anything it means the file is success fully encrypted, if there is any error you can see error on the screen. since we have encrypted file successfully we will now run "ls -la" to see the encrypted file.

5) ![des 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/1d1ddd40-b4ed-413b-8c2d-3ea64d5aa7d4)
   

![des 5](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/f45acba8-1976-433f-96aa-3b98b8cedaf9)


### AES in OpenSSL.

same like des but with a small sifference in a codes and cooands we can encrypt a file using AES

1) ![encryption step 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/4b2afbc8-2d87-4389-8d5c-b07acb4bbc4d)
   

2) ![encryption step 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/37446b2a-b641-46de-8fe4-d420e969b8e2)


3) ![encryption step3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/98345c9f-0549-4106-b164-83733c8098b1)


