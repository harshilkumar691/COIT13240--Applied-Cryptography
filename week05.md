# Week05
# 1. Public key crypto and RSA

let us first understand the difference between public key ans symmetric key 

### Symmetric Key Encryption
In symmetric key encryption same key is used to encrypt and decrypt. This key can be generated randomly. the several problem arises by using this approach is, how so receiver get this key safely, and the surety that no one intercepts this key.

If the user A is going to use the particular key then he/she needs to share this key to the User B securely. Now, in this case securely means in encryptrd form. If this key is encrypted using symmetric key then one moire key is generated; So, the same problem arose again. 

If we do not encrypt it and send it using online coomunication then the attackers can entercept it and detect the message or key.
 
### Public key encryption
In public key encryption there are 2 different keys
#### One key (public) --> For encryption
#### Another key (Private) --> For decryption
both the keys are mathematically related

key exchange is not a problem because public key is encrypted

The problem in this is this encryption technique is much slower as comered to symmetric key encryption.


Every user has their own pair of keys i.e.

PU --> Public key

PR --> Private Key

These keys are not generated randomly like we do in symmetric key.

These keys are generated by using the algorithm which comes with ciphers.

#### As the name defines --> Public key(PU)
It is publically available for example: Email signatures, messages, on websites, etc.

#### As the name defines --> Private key(PR)
This is a secret key which only owner knows, asscess to this file is restricted on the computer. 


## 2. Confidentiality with public key Crypto
![Screenshot 2024-05-05 123703](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/e2ffcb56-18ac-4274-b17a-5cc039b2cfea)

the above given figure indicates confidentiality with public key crypto
where, 
#### left side User-A is sender and right side B is receiver
#### It encrypts using Public Key (PUB)
#### It decrypts using Private Key (PRB)
#### only User-B has a Private key(PRB), therefore only user-B can successfully decrypt
This is a confidentiality in Public key crypto.

In this User-A is sender

User-B is receiver

User-A will encrypt a message using the receiver's public key and generate a ciphertext, If the attacker intercepts they will get to see ciphertext.

After generating the ciphertext User-B will decrypt the ciphertext using the their private key. 


## 3. RSA Alogorithm

## 3.1 RSA Key Generation Algorithm

In this first we have to choose prime numbers

(Note:- Prime number is a number which is divisible by itself and 1. Example = 14, it is divisible by 14 and 1.)


## Example 1
### Calculating manually.
Let's take an example for RSA Key Generation 
#### Assume user A chose the primes p=13 and q=19. 

There are 5 steps.

We have to find Find 

#### 𝑑 ≡ 𝑒 ^ -1 (𝑚𝑜𝑑𝜙(𝑛))

#### n = ?
#### 𝜙(𝑛) = ?
#### e = ?
#### d =?

### Step 1:-

select 2 prime numbers

![RSA step 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/4d10e63a-095a-48f3-83c9-18be0f6af9b1)


### Step 2:-

Calculate "n"

To calculate "n" we have to multiply "p x q"

![RSA step 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/3b83c8cc-0146-45b0-9668-6fdc8f5058cc)


### Step 3:-

To calculate 𝜙(𝑛) we will use shortcuts 
first deduct 1 from the p and q 

𝜙(13) = 13 - 1 = 12
𝜙(19) = 19 - 1 = 18

Then 𝜙(𝑛) = 𝜙(p x q) = 𝜙(p) x 𝜙(q)

![RSA step 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/072765b2-6107-4bde-a7c6-5057e6f95cfc)


### Step 4:-

To find "e" we have to find greatest common divisor. 

![RSA step 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/95c19318-a33d-454f-932c-f0e4525a33fa)


Step 5:-

In this step we have to select the numbers which are divided by "n", and after dividing it's output should not be in decimal(float) it should be in integer. And when done the calculation

"e x d mod (𝜙(𝑛))" the output should be 1.

![RSA step 5 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/46cef7d4-697c-4df9-9f2e-d222b72233c9)

![RSA step 5 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/1ad461c7-6759-48fc-abe1-b9edf531c315)

### Public key of A (PUA) = {e = 5, n = 247}
### Private Key of A (PRA) = {d = 173, n = 247}

### p = 13, q = 19, 𝜙(𝑛) = 216, d = 173. all this information are private. 



## RSA Encryption and Decryption

### Encryption= 𝐶 = 𝑀^𝑒 mod 𝑛
### Decryption= 𝑀 = 𝐶^𝑑 mod 𝑛
Given above are the algorithms for encryption and decryption.

## Encryption using manual calculation
let's use encryption algorithm using  "𝐶 = 𝑀^𝑒 mod 𝑛"

where M is a plaintext and c is ciphertext which we are finding, in this case lets assume our plaintext as "M = 10"
#### M = 10.
#### 𝐶 = 𝑀^𝑒 mod 𝑛  -----> Insert all the values we have in this algorithm.
#### 𝐶 = 10^5 mod 247   --------> Put this equation in calculator.
#### 𝐶 = 212
#### So, our ciphertext is "C = 212"

## Decryption using manual calculation

Let's use decryption algorithm using "𝑀 = 𝐶^𝑑 mod 𝑛"

where M is plaintext which we will find now, and C is our ciphertext.

#### 𝑀 = 𝐶^𝑑 mod 𝑛  ------> Insert all the values we have.
#### 𝑀 = 212^173 mod 247  -------> Put this equation in calculator.
#### 𝑀 = 10

so here we have decrypted the ciphertext using algorithms.


## 3.2 Using Python
## Example 2
### Key generation using python
so lets take another example with "p and q" 4 digits long number.

To select a long prime number we can use the chart given below which has a list of prime numbers. 

![Prime numbers list](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/9a12e723-6034-4118-9789-3fab0dacbefb)

link to wikipedia:-

https://en.wikipedia.org/wiki/List_of_prime_numbers


let's take
### p = 1009 and q = 1021

### Step 1:
#### n = 1030189

![RSA py 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/71091aba-5582-4a10-ac65-20280ba1284c)

### Step 2:
#### 𝜙(1030189) = p = 1009 - 1 = 1008
#### q = 1021 - 1 = 1020

![RSA py 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/0a49f852-df9e-4363-8360-c47ffe18fa7d)

### Step 3:
#### 𝜙(1030189) = 1008 * 1020 = 1028160

![RSA py 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/e563149b-5b8f-48b7-9964-8eb947e9991b)

### Step 4:
#### select a prime number that is not a divisor of 𝜙(n).

For This 

we will start try number, we will divide 1028160 by 2 

1028160 / 2 = 514080.0  -----> divisible by 2, we will not use this.

1028160 / 3 = 342720.0 -------> divisible by 3, we will not use this.

1028160 / 4 = 257040.0  -------> divisible by 4, we will not use this.

1028160 / 5 = 205632.0  -------> divisible by 5, we will not use this.

1028160 / 6 = 171360.0  --------> divisible by 6, we will not use this.

1028160 / 7 = 146880.0  --------> divisible by 7, we will not use this.

1028160 / 8 = 128520.0  --------> divisible by 8, we will not use this.

1028160 / 9 = 114240.0  --------> divisible by 9, we will not use this.

1028160 / 10 = 102816.0 --------> divisible by 10, we will not use this.

1028160 / 11 = 93469.09090909091 ------> 1028160 is not divisible by 11, we will use 11  

#### e = 11

![RSA py 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/e642713f-da7a-4d5c-a565-a01f19ba8e88)

### Step 5:
use python to enter the values

#### pow(e, -1, 𝜙(n))

![RSA py 5](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/71de412e-372a-473f-ad22-1f711c172112)

#### we got an output 
#### d = 934691

### Now we have our values to encrypt and decrypt.
#### n = 1030189
#### e = 11
#### d = 934691


## Encryption using python
As we learned before that we have to use receivers public key to encrypt 
#### i.e. {e, n) are available publically.

so let's assume the keys {e, n} which we have is the receivers public key.

And we have to add the Plaintext "M" form our side because we are encrypting palintext.

we can encrypt the message by using the python
#### let's assume plaintext M = 1000

use "pow" to encrypt.
#### pow(M, e, n)


![RSA py enc](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/7669c1c1-a74b-4caf-aa9e-962d914cce9c)

### Ciphertext C = 47155


## Decryption using python 

As we learned before that after sender share the ciphertext to the receiver, receiver will decrypt it using their private key.

suppose sender shared us the ciphertext.
#### Ciphertext C = 47155

And the receiver will use their private keys {d, n, c). where C means ciphertext.

receiver can decrypt ciphertext by using "pow(C, d, n)"

![RSA py dec](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/e0507e5b-f651-4d2f-9e04-f239396fba92)


#### (Note:- attacker knows (e, n, c, C = M^e mod n, M = C^d mod n. 
#### Attacker don't know "p and q", to find "p and q" they need to factor n into its primes.
#### Attacker don't know d and 𝜙(n), to find this they need to find d by finding 𝜙(n) by calculating manually, which is practically impossible with larger numbers.)



## 4. RSA key generation in OpenSSL

we can generate the private key using genpkey. User must keep their private key with themselves (private)  

### Command to generate a private key:-

#### openssl genpkey -algorithm RSA -pkeyopt rsa_keygen_bits:2048 -pkeyopt rsa_keygen_pubexp:3 -out rsa-private-enc.pem

![Private key gen step 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/3d702adf-05fb-4fb4-bbca-0fe590206748)

![Private key gen step 1 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/8451c9a6-fcb9-41a4-a8a9-cb508d5e279a)

![Private key gen step 1 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/5519803e-b18d-424a-bfaf-5b10dd39a38b)


#### This private key is encoded with base64. We can view values this file using

#### openssl pkey -in rsa-private-enc.pem -text

![Private key gen step 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/954ba660-a5c5-4ba0-ae7f-a21f48316923)

![Private key gen step 2 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/9e894ce6-6894-4f3e-88e7-181763ae004e)

![Private key gen step 2 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/ee50bfe3-c37f-49dc-9e6f-bbca8cd3b906)


### Command to generate a public key is 

### openssl pkey -in rsa-private-enc.pem -out rsa-public-enc.pem -pubout

#### the File "rsa-public-enc.pem" includes only the public key values within it.

#### we can see the values of the public key by 

### openssl pkey -in rsa-public-enc.pem -pubin -text

![Public key gen step 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/e615fb35-53b4-4367-bc06-e9ec7d18ee3a)

![Public key gen step 1 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/032324ed-7199-4be4-b07c-ee6dd79a8680)

![Public key gen step 1 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/4c9eef0b-76f2-44ec-b581-14182ce23697)

![Public key gen step 1 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/9d8321c9-6924-4b03-b9ad-3d963dd44d38)


## 4.1 RSA Signing in OpenSSL (Sender)

Now we have our public and private key so lets make a text file which has message to send receiver.

#### echo "Hello I am Harshilkumar Patel." > message-pt.txt

![RSA signing step 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/eef2bca6-1383-4b61-9ccc-d9645a9db441)

we need to calculate its hash after that we need to encrypt that hash using private key, to sign the message. To create a hash message we can use command.

![RSA signing step 1 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/ac51df93-f906-450b-95b8-433f7b96f6f8)


Openssl also has an option to calculate the hash and then we can sign it using private key. then we will get an output containing a private key.

#### openssl dgst -sha1 -sign rsa-private-enc.pem -out sign.bin message-pt.txt

![RSA signing step 1 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/660af428-f8c8-4378-af6c-9e1fdcecb8cf)

![RSA signing step 1 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/680b306b-5b50-4092-94a9-43550bcbc3a1)


## 4.2 RSA Encryption

To encrypt message we can use. in this i am using the key i made on my computed but we can use receivers public key. 

#### openssl pkeyutl -encrypt -in message-pt.txt -pubin -inkey rsa-public-enc.pem -out ciphertext-msg.bin

![RSA encryption step 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/cfdb99ed-d2ce-48d8-ac72-2f9df6f9eed4)

## 4.3 RSA Decryption

when the receiver receives both the files form the sender, they need to decrypt the ciphertext and verify the signature

#### openssl pkeyutl -decrypt -in ciphertext-msg.bin -inkey rsa-private-enc.pem -out received-decrypted.txt

![RSA decryption step 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/5822dd51-8ab2-4fbb-85a2-e615d5aeb5a2)


### [NOTE:- In this case I have used public and private keys which i have made to encrypt and decrypt. But while doing encryption we need to use the public key of the receiver. and to decrypt the ciphertext receiver needs their(receiver) private key.] 

















