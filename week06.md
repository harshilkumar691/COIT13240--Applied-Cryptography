# week06
Before starting the concept of Diffie-Hellman key we will first recall some basic mathematics.
## 1. Exponentiation and Logarithms

10^5 we all know that it is 100,000 
2^3 is 8

Above given operations are called exponentiation. 


The inverse operations is called logarithm.
Example:- 

log10 (100,000) = 5

log2 (8) = 3

Just a simple way to understand and remember this is.

### Exponentiation
"x" raised to "a" 
#### x^a = n  -------> x = 10, a = 3, and "n" means answer n = 100,000.
#### 10^5 = 100,000

### Logarithm
Log "n" to the base "x" = answer. 
#### logx(n) = answer ------> logx= log10, (n) = 100,000, answer = 5
#### log10(100,000) = 5


## Modular Exponentiation and Discrete Logarithm

7^5 mod 6 = 1 -----> 7 raised to 5 mod 6

Above given operation is modular exponention

The inverse of this is known as discrete logarithm.

Example:

dlog (1) to the base 7,6 = answer 

dlog7,6 (1) = 5 -------->  dlog7,6 = 7,6 is the in the base then (1) 

If the modulus and base are related the Discrete logarithm only returns unique values.

This states that the base is a primitive root of modulus.

If we talk about a large numbers then Discrete logarithm is really a challenging problem.


## 2. Public key crypto encryption (RSA)

1. Suppose user-A has its Public key(PUA), Private key(PRA), and Public key of user-B(PUB).

   User-A has a public key of User-B because, User-A needs the public key of user-B to encrypt the message.

2. Suppose user-B has its Public key(PUB), Private key(PRB), and Public key of user-A(PUA)

3. Suppose user-A has randomly generated a secret key(KAB) and want to share it to user-B.

So all we have is.

#### user-A = KAB, PUA, PRA, PUB.
#### user-B = PUB, PRB, PRA.

How can we share KAB from user-A to user-B?

We will encrypt it (C).

we will encrypt it using RSA (ERSA).

We will use user-B's public key(PUB) to share message KAB secretly.

#### i.e. C = ERSA(PUB, KAB)  --------> PUB = Public key of B, KAB = message in this case, ERSA = encrypted using RSA, C = ciphertext.

when the message is sent to the user-B. user-B will decrypt the ciphertext using their private key(PRB).

#### i.e. D = (PRB, C) --> KAB

In the above given example D = decryption, PRB = private key of B, C = ciphertext and, KAB = plaintext that is decrypted.


## Diffie-Hellmam Key Exchange (DHKE)

## Analysis
1. It is easy to calculate public key(PU), and K.
2. Attacker knows 3 public values i.e. Public key(PUA), generator(g), and a prime(p).
3. Private key of user-A(PRA), Private key of User-B(PRB), KA, KB must be private.

### In the "point number 2" i said that attacker knows 3 public values all three valuse comes up together and make an modular exponential algorithm.

![Modular exponentation](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/b6327a64-cc6d-46e2-a9be-f604ca165b04)

In this Private key of user-a(PRA) is confidential attacker dont know this. 

If attacker wants to find "PRA", they need to use discrete logarithm by inverting this equation and find PRA, which is impossible with larger numbers.

### Assume we have intercepted PUA = 15 from the DHKE exercise, how would you perform a brute force attack to find PRA? How could such a successfull bruteforce attack be prevented in practice.

### Answer 
Attacker will try the different values of PRA and calculate the shared secret using intercepted value of PUA and parameters of DHKE (p and g).
we can prevent this successful brute force attack by increasing a length of keys.  


## Implementations of DHKE
### selecting parameters "p and g"
"g" stands for generator and "p" stands for prime.
1. In this we have to select a prime number for "p"
2. For "g" we have to find the primitive root of modulo of "p".
3. Defination of Primitive root is "If we take "g" and raise it to the power of "1, 2, 3, 4.....p-1" and mod by p the answer should be distinct (the 
   answers we get should not be repetative).
5. we can find "g" by using 
### "g^x mod p"
   
For Example: 
### suppose we have selected p = 17. So, now we have to find "g"
we have, p = 17 and we will try g = 2

we will use
#### g^x mod p
#### 2^1 mod 17 = 2  ----> we are tryping "g = 2" to check weather it is primitive of p or not, we will increase x starting from "1" till "p-1", p = 17.
#### 2^2 mod 17 = 4
#### 2^3 mod 17 = 8
#### 2^4 mod 17 = 16
#### 2^5 mod 17 = 15
#### 2^6 mod 17 = 13
#### 2^7 mod 17 = 9
#### 2^8 mod 17 = 1
#### 2^9 mod 17 = 2
### So, here as we can see the answer 2 is repetative when we try g = 2 so this is not primitive root of p


### we will try g = 3

#### 3^1 mod 17 = 3 
#### 3^2 mod 17 = 9
#### 3^3 mod 17 = 10
#### 3^4 mod 17 = 13
#### 3^5 mod 17 = 5
#### 3^6 mod 17 = 15
#### 3^7 mod 17 = 11
#### 3^8 mod 17 = 16
#### 3^9 mod 17 = 14
#### 2^10 mod 17 = 8
#### 2^11 mod 17 = 7
#### 2^12 mod 17 = 4
#### 2^13 mod 17 = 12
#### 2^14 mod 17 = 2
#### 2^15 mod 17 = 6
#### 2^16 mod 17 = 1
### As we can see here all the answers are distinct (all are non-repetative). So, g = 3 is the primitive of p = 17

## OR

### we can use the chart given below to find the primitive roots. tis chart contains the primitive roots of modulo from 1 to 31.

![Primitive roots chart](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/8bca4953-727f-4c68-a0fe-2870f286372d)

link to wikipedia:

https://en.wikipedia.org/wiki/Primitive_root_modulo_n

#### I usually preffer to use charts but i make sure to check the answers bu using way i solved the example i solved above.


## Example of DHKE
### Assume user-A and user-B are using DHKE. Select prime number "p = ?" find "g = ?". Randomly choose private key for user-A and user-B and find the shared secret key.

In this we will select p = 17 and use g = 3 as we have solved in the previous example. 

### Step 1 & 2: We have to first select prime "P" and then find generator "g".

![DHKE step 1,2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/433af70a-6efa-41dd-ae44-605ab4b6248c)

[Note: To understand how we got "g = 3" go back to "selecting parameters "p and g"" i have solved the example their for p = 17 and "g = 3"]

### Step 3: 
#### 1. In step 3 user-A have to choose their value of private key(PRA) randomly. But, the value of private key(PRA) should be less then "p".

#### 2. Find public key (PUA) using "PUA = g^PRA mod p".

#### 3. Share the public key (PUA), p = 17 and, g = 3 to the user-B. And the user-B will also follow the same steps(step 3 only)

![DHKE step 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/c87ec614-1f9e-4515-8f46-7386feba6043)


### Step 4:
#### 1. After finding public key of user-B (PUB). Share it to the user-A.

#### 2. user-A will use the public key of user-B (PUB) to find the secret key (KA).

#### 3. User-B will use the public key of user-A (PUA) to find the secret key (KB).

#### 4. At The end the secret key of (KA and KB) should be the same. 

![DHKE step 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/188913d9-26db-4134-9c7b-8ecf72b2f47c)

#### In the above given picture we can see that both KA and KB have the same value 1. i.e. KA = 1 and KB = 1. It means we have got the correct key.


## 3. Man-in-the-Middle attack on DHKE

in the previous example of DHKE we saw that the flow of finding the KA and KB was. 

#### user-A find the public key(PUA) and "share p,g, and PUA" to to user-B.
#### user-B find the public key(PUB) and "share PUB" to user-A and then both of them "user-A and user-B" find the KA and KB

So, above given was the flow of the DHKE.

Now, what attacker (man-in-the-middle) do is they intercept when the data is being shared.for example, let's take the above given flow.


#### user-A find the public key(PUA) and

#### "share p,g, and PUA" to to user-B. ----> When user-A sends the data to user-B attacker intercepts and modify this message and try to trick user-B.

#### Then user user-B gets the modified message and by using that modified message user-B find the public key(PUB) and 

#### "share PUB" to user-A ---> when user-B sends the information to user-A, attacker intercepts and again modify the message and try to trick user-A.  

#### When user-A receives the modified message; Then, both of them "user-A and user-B" find the KA and KB and side by side attacker will use its private key PRC to find the secret key of user-A and user user-B.

[note: If attacker (Man-in-the-Middle) is successful to intercept and modify the message and user-A and user-B cannot detect that the message is modified. It means that the attacker is successful in doing their work.]


### Let's take an example:

![Man-in-the-middle attack](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/98ce7beb-fb3c-4e3a-8cfe-170e148b6d84)


### Above given picture is the example of Man-in-the-middle attack

### In the above given example we didn't expalined one step due to lack of space.

![man-in-the-middle attack 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/ac126e9f-cfa6-479c-93ac-c60bcc051dc2)


In this step we can see that I have written.

#### PRC2 = 10, PUC2 = 8, -----> we can calculate it using the same steps we did in the above to find "PUC" but as we only want to intercept and change the value we can asume it same as above.

#### In the next step I have calculated secret keys------> attacker use "public key of user" and "private key of itself" and mod p to calculate find secret key.

#### If attacker want to find secret key of user-A they will use "public key of user-A PUA" and "private key of itself PRC1" amd mod p.

#### If attacker want to find secret key of user-B they will use "public key of user-B PUB" and "private key of itself PRC2" and mod p.

#### After user a and b have their keys they can now encrypt and decrypt he messages they send to eachother. But, the attacker has the keys as well and attacker will again interept 

### lets take an example.

#### now user user-A and B both has their secret key
#### user-A = 1
#### user-B = 13
#### attacker also has the same keys.

**1. user-A encrypt a message "I am in troulbe" by using a key "1" and sends to user-B**

**2. Attacker intercepts again and they has the key and they will use that key "1" to decrypt and modify the message as "I am ok", encrypts it using the key "13" and sends it to user-B, pretending as user-A**

**3. User-B then receives a encrypted message, they decrypt it using key "13". They think that user-A sent this message.**

**By doing this attacker has broken the confidentiality between the user-A ansd user-B.**

## How attacker can find the private key.
Attacker can also find the private key by solving the equation 

**PR = dlog g,p (PU)** -------> PR = private key, dlog = discrite log, g = generator, p = prime, PU = public key

This equation is the **inverse** of the equation that we use to find Public key.

**PUA = g^PRA mod p**

#### suppose we want to find the private key of user-A (PRA)

we can use  

![Screenshot 2024-05-08 153509](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/e6640706-b9cb-4734-a1c7-2dec0fcfe403)


#### I found this equation very confusing and difficult even i am solving it with small numbers. 

#### So I tried to use the equation that we use to find public key

![pub eq](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/1cf5fa64-d75f-439a-86dd-eb86cce07978)

**I used this equation by just entering values in PRA (values starting from 1 to until we find the answer similar to public key)**

**I have used this because. As we all know that attacker knows 3 parameters**

**(p, g, and Public key)**

**if i want to find the private key i can simply use**

**"g^PRA mod p"**

All I need to do is **first start entering the value starting from "1" in PRA**

Let's take an example from the study notes to **find the private key.**


![Example of discrete log](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/af35d607-462d-4504-a7b3-9bf1bb50ad75)


![Screenshot 2024-05-08 154627](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/97425321-ef3e-4bc9-b94e-683f52f4b926)


In this example we will find the **private value of user-A (PRA).**

As an attacker We know **p = 19, g = 10, and PUA = 15**

Now, I will use equation **"g^PRA mod p"** to find **PRA.**

**g^PRA mod p** -------> Insert all the values we have in this equation. Insert values starting from 1 in "PRA" until we get the answer similar to PUA.

**10^1 mod 19 = 10** ----> we can use scientific calculator -->type 10^1 --> then press "=" --> press mod --> type 19 --> press "=".

**10^2 mod 19 = 5** ---> 5 is not equal to PUA = 15

**10^3 mod 19 = 12** ---> 12 is not equal to PUA = 15

**10^4 mod 19 = 6 **---> 6 is not equal to PUA = 15

**10^5 mod 19 = 3** ---> 3 is not equal to PUA = 15

**10^6 mod 19 = 11** ---> 11 is not equal to PUA = 15

#### 10^7 mod 19 = 15 ---> 15 is equal to PUA = 15
#### So, here we have found the private key of user-A 
#### PRA = 7

we can see in the below question that indicates that the private key used by "user-A is 7"
this means our answer is correct.

![Screenshot 2024-05-08 160418](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/0f83d084-e678-497b-88e0-3e7d316e5a75)

I found this method very simple and effective here I have used scientific calculator to solve but we can also use the websites in which we can simple put an equation and website will give an answer.


## Diffie-Hellman key generation using python

for this we have to use a **python code**. 

First make a file with **extention .py** in linux server and write this code given below.

I have used "nano DHKE-example.py" command to make file and wrote this code in it. 

Press Ctrl^x and then y and then enter to save.

### Python code.

![DHKE code 1 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/7f22e352-f5bc-4687-bd68-fdf6edb8b0af)

![DHKE code 1 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/e3e70df3-cf42-4262-84ad-7b924aa990b9)

After saving this file run the file.

### Step 1:

![DHKE py step 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/901cd730-a98a-4959-99ed-756a3ed4afb4)

When you get the output just check that you will **get output in 2 lines and both the lines should be identical**. if the lines are **not identical then it is an error
**
### Step 2:

After getting the expected output check that the files are created and saved.

![files made py step 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/fd986001-3000-4134-becf-1f1e70bfef7d)

### step 3:

The file "dh-parameters.pem contains the parameters such as**prime p, generator g.**

![parameters p,g py step 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/a3ef9fcf-2acd-4006-bd6c-99a627d2d4ec)


### step 4:

The file dh-private-apple.pem containes the all the values **public, private, prime p, generator, g.**

Same goes with dh-private-banana.pem


![private, public, prime, generator py step 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/729bbc56-7c26-47f4-b36f-d207915dcae7)

![private,public,prime,generator py step 4 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/ab4d74e0-a6b5-49b5-8b76-841ba5291dfd)


### step 5:

The file dh-public-apple.pem contains just public parameters such i.e. public key, p, g.

same goes with dh-public-banana.pem

![public, p, g step 5](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/561e61b0-ae44-437e-8770-aaf9334eeaab)


### Step 6:

After checking all the files we can then use openssl for encryption and decryption.

first we need to load the **parameters** by using the command 

openssl dhparam -in dh-parameters.pem -noout -check

![openssl 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/0f01a53e-263c-4822-8b20-73057925938d)


### Step 7:

we have to now load **private key of apple** and **public key of banana**. Because apple will encrypt the message.

and as we all know if apple is **A** and banana is **B*. If **A wants to encrypt** the message then it will use **its(A) private key** and **public key of B**

openssl pkey -in dh-private-apple.pem -text

openssl pkey -pubin -in dh-public-banana.pem -text

this will gave the **output same as step 4 and step 5.**

### Step 7:

We will derive a shared secret key using **-derive**

openssl pkeyutl -derive -inkey dh-private-apple.pem -peerkey dh-public-banana.pem -out shared_secret.bin

![openssl 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/162314af-9803-4478-9ac1-86508af93a50)

in this:

**-inkey dh-private-apple.pem** -----> specifies the input private key file which belongs to apple.

**-peerkey dh-public-banana.pem** -----> specifies public key file belonging to banana.

**-out shared_secret.bin**  -------> specifices the output file **shared_secret.bin** containing shared secret key.

![openssl 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/4218f6c7-0df4-428f-a545-ce44c9478613)


### Step 8:

We will now encrypt the message using **aes-256-cbc**

For this we will first make a **file containing a message (plaintext)** with extension .txt. I have named it plaintext.txt users can give another name.

we will use 

openssl enc -aes-256-cbc -pbkdf2 -in plaintext.txt -out ciphertext.bin -pass file:shared_secret.bin

![openssl 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/17dcda6c-5122-49d8-834b-26b06098d082)

This will **output the file ciphertext.bin** containing the **ciphertext within it.**

In this:

**-aes-256-cbc** -----> aes-256-cbc uses 256-bit key and operates in cipher block chaining mode(CBC) mode.

**-pbkdf2**  -----> this is Password Based Key Derivation Function 2 (pbkdf2). This specifies that it should be used for key derivation

**-pass file:shared_secret.bin**  -----> This specifies that the **encryption key should be read from file shared-secret.bin** containing shared secret key.


### step 9:

**Apple A** will now share the ciphertext to **banana B**

### Step 9:

no as we know that if **apple A** send the ciphertext to **banana B** then, **apple A** needs private key of itself and public key of **banana B** for encryption 

Now **banana B** has received the ciphertext from **apple A** and, if **banana B** wants to **decrypt** the ciphertext then banana B needs **private key of itself** and **public key of apple A** to decrypt the ciphertext.

We will now **load the private key of banana B** and **public key of apple A**.

openssl pkey -in dh-private-banana.pem -text

openssl pkey -pubin -in dh-public-apple.pem -text

output will be the as we saw in **step 4 and step 5**

### Step 10.

In this step **Banana B will make a shared secret key** by using the **private key of itself** and **public key of apple A**

openssl pkeyutl -derive -inkey dh-private-banana.pem -peerkey dh-public-apple.pem -out shared_secret.bin


![openssl 5](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/9e3870de-73aa-4611-b91d-61d0e06c991e)


### Step 11:

Decrypt the ciphertext 

![openssl 6](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/2d00855e-6dd3-4017-aa0b-57e4248cba36)


In this :

**-d** -----> indicates decryption mode.

**-aes-256-cbc** -----> aes-256-cbc uses 256-bit key and operates in cipher block chaining mode(CBC) mode.

**-pbkdf2**  -----> this is Password Based Key Derivation Function 2 (pbkdf2). This specifies that it should be used for key derivation

**-pass file:shared_secret.bin**  -----> This specifies that the **encryption key should be read from file shared-secret.bin** containing shared secret key.


This will **decrypt the ciphertext** and give an **output** with the **specified file name (decrypted.txt) containing the plaintext in it.**

















