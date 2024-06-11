# week09

# Authentication and Data Integrity

## Attacks on Information Transfer

#### 1. Disclosure attack: Encryption

In this attack attacker attains unlawful access to useful data such as key, private key, plaintext or any other data. 

we can assume it as data leakage.

   
#### 2. Traffic analysis attack: Encryption

In this attacker analyze the patterns of the communication between the sender and receiver, size and length of files or packets, timing, behaviour, content of encrypted 
messages etc. and try to find the original information.

#### 3. Masquerade Attack: Message authentication

The best example I can give for this attack is **(Man-In-The-Middle attack)** 

As we saw in the **week06** that the user-A is sending the public-key, prime p, generator g, to user-B.

And the attacker is the **Man-In-The-Middle** attacker knows this parameters, they intercepts when user-A is sharing any information to user-B and when user-B is sending some information to user-A.

Attacker intercepts everytime and user-A thinks that the message they got is sent by user-B and user-B think that the message they got is sent by user-A.

#### 4. Content modification: Message modification

As we saw in the **week06** that the user-A is sending the public-key, prime p, generator g, to user-B.

And the attacker is the **Man-In-The-Middle** attacker knows this parameters and they use this to modify the message and send it to user-A.

#### 5. Sequence modification attack: Message authentication

In this attack attacker modifies the sequence of messages and try to disturb the normal flow of communication between sender and receiver.

Attacker can modify message, drop message, delay the sending of message, or delete the message.

#### 6. Timing modification attack: Message authentication

#### 7. Source repudiation: Digital signatures

In this the receiver may get a response from the sender that, sender has not send that message. 

#### 8. Destination repudiation: Digital signatures

As the name suggest destination the sender may get the response from the receiver that, the receiver did not get received any message.


## Aim of Authentication:

### defination:
When receiver receives the information and the inspection of the modification and the originality of the sender(sender is real or he/she is an attacker) is known as authentication.

### There are different ways to achieve the authentication

#### 1. Symmetric key encryption
#### 2. Hash Functions
#### 3. Message Authentication Codes (MACs)
#### 4. Public Key Encryption (digital signatures)


## Symmetric Encryption for Authentication

![diag auth symmetrice key encryption final](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/162ddf80-da7d-489b-ab93-928c87312b7d)

as we all know and the diagram itself shows.

On the **left side** of the diagram. sender uses the **"message M"** and **"shared secret key K"** to **encrypt** the message and send the **"ciphertext C"** to the receiver.

When receiver receives the message, they use **"shared secret key K"** and a **"received criphetext C"** to decrypt the message.

When the receiver receives the message and **if they are able to produce the plaintext** then it is ok.

But if the receiver produce the plaintext and **it has no meaning** then either the **receiver has used a wrong key** or there has been an **modification while sharing** the ciphertext.

By this we can assume that the symmetric key provides an encryption.

### what we can add to improve authentication 

In this we can also add the error detecting code to the message, this will help the decryptor to detect if it is correct or not.

We can also use other forms of authentication which do not depend only on symmetric key authentication; Such as, MAC.


## Authentication using Hash

![Diag auth using Hash](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/2a2946ad-2d4e-439b-9e6a-b15aec79ea89)

In the above given diagram 

**M** ----------> message

**H()** --------> Hash function

**||** ---------> Concatination

**KAB** --------> Key

**E()** --------> Encrypted message

**D()** --------> Decryption

**compare** ----> compare the output and input

**same** -------> if the decrepted message is same as input then the decreptiion is **pass**

**diff** -------> If the decrepted message is not same as input then the decryption is **fail**


### How it Works?

suppose sender gives the input **"message M"** and and the **"hash H()"** function is applied. 

Then the message will **"concatinate ||"**. In simple words the concatination joins the message and the hash of the message.

Then using the **"key K"** the message is encrypted and sent to the receiver.

Receiver, then use the **"key K"** and apply the **"hash H()"** function to decrypt the encrypted message. 

After decrypting hash will **compare** if the decrypted message is **same** as input then the decryption is **pass.**

If the decrypted message is **"different diff"** from input then the decryption will be **fail**. 

Receiver then reject that message.

As we have studied at the **start of week08** about the **one-way protocol.** 

It is impossible for the attacker to use the encrypted message tto find the input message. Since, it is the one-way attacker cannot revert the process.



![diag auth using hash 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/cf64e52c-bf6a-4470-afad-93db4f1a50f9)


Above given figure is different from the the diagram that we saw before 

This diagram shows that the messages is **not encrypted** but the **hash message is authenticated** 

This is used when the sender and receiver **both do not care** about of **confidentiality**.


## Authantication using MACs

![diag auth MAC 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/7c125a27-7d1d-4b0b-b4a4-189886c9d965)


As we saw all the notations in the previous example.

So, are familiar with the notations in the diagram except **MAC()**.

**MAC()** -----> This is a MAC function.

### How it Works?

Sender gives the **"message M"** and applies the **"MAC function MAC()"**. 

**MAC()** takes the **"key K"** as an input with the **message M** and concatinate them and send 

**"M || MAC(KAB,M)"** to the receiver.

Receiver then, use the **"Key K"** and **"encrypted message M"** and applies the **"MAC()"** to decrypt the encrypted message. 

The function will then **compare** the decrypted message with the input is if they both are **similar** then it is ok.

But if both are **"not similar diff"** then the the decryption **fails**.

The receiver then **rejects** the message.


#### MAC has advantage over hashes in that if encryption is defeted, then MAC still provides integrity

#### To make this more secure we can use the approach known as 

### Encrypt-then-MAC

In this the **sender encrypts** the message using **symmetric key encryption.** 

Then applies **MAC()** on the **ciphertext.**

The **ciphertext and tag** are then sent in the following way.

### E(K1, M) || MAC(K2, E(K1, M))

#### E(K1, M) ------> Encrypted message "ciphertext"

#### MAC(K2, E(K1, M)) -----> "Tag" which is output from the "MAC()"

In the above given equation **2 independent keys** are use **"K1" and "K2"**

### MAC-then-Encrypt

The sender applies the MAC() on the plaintext, appends the result to the plaintext, and then encrypt both, the ciphertext is sent, in a following manner.

### E(K1, M || MAC(K2, M))

In this,

**MAC(K2, M)** ------> This is **Tag** which is output of MAC.

**K1, M** -------> Key and the message.

**||** -------> this concatinates MAC(K2, M) and K1, M and forms **(K1, M || MAC(K2, M))**

**E** -------> This indicates after concatination **"(K1, M || MAC(K2, M))"** this value is encrypted and the equation forms **"E(K1, M || MAC(K2, M))"**.


## Digital Signatures

Assume user-A has own public key and private key (PUA, PRA)

### Signing

User-A sings a message by encrypting **hash of message** with own private key PRA

we can make an equation by following the above given line:

### S = E(PRA, H(M)) ------> Hash of the input message **"H(M)"** and the private key **PRA** are encrypted to make a signature.

Here,

**S** ----> Signature

**E** ----> Encrypted

**PRA** ---->private key of user-A

**H(M)** ----> Hash of the message 

#### user-A will attach the signature this signature with the message and send to the user-B.

### verification

Here **user-B decrypt** the signature and **verify** the message with the **user-A public key**.

### h = D(PUA, S)

Then user-B will compare the hash of the received message, **H(M)** and decrypted message **"h"**

If they both are similar then it is verified. otherwise it is not verified.

#### Here is the example of digital signature.
![example of digital signature](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/f72443bd-840d-4248-8074-1912c6455e39)


#### Here is an example od signed certificate in wireshark.

![wireshark tls server 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/3ba6b02a-2b19-4af9-ac22-1c5f05dbda22)


## Example of Authentication

![example authentication](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/a42aff57-4d0e-4037-a63a-add6110da056)

#### Solution:

we have

**M** = original message 

**M2**= modified message (M2 will be different from M)

Assume that Attacker has intercepted **M || E(KAB, H(M))** ---> M = 0101010101...0111101011

Attacker changes **M to M2**, assuming **H(M2) = = H(M)** ----> Collision

#### Trial 1. 

Attacker sends M2 to B: **M2||E(KCB, H(M2))**

**Receiver  Authenticates:**

1. receiver will Decrypt: **D(KAB, E(KCB, H(M2)))** ------> output hrx will be random but will not be H(M2)
2. Receiver will Calculate hash: **H(M2)**
3. Receiver will compare H(M2) with hrx. and it is not same
4. Different valuse so the authentication is fail.


#### Trial 2:

Attacker sends M2 to B: M2||E(KAB, H(M2)) 

Attacker will not struggle to re-encrypt. he/she will simply compy the encrypted hash from intercepted message.

Now, receiver will authenticat

1. receiver will Decrypt: D(KAB, E(KAB, H(M))).------> output hrx will be H(M)
2. receiver will calculate hash: H(M2)
3. receiver will compare H(M) with H(M2) and receiver finds H(M) = = H(M2)
4. Authentication is passed.

This means Receiver thinks that the message he/she got is sent by user-A but it is send by attacker.  










