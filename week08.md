# week08

# Hash Functions and MACs

## Hash Function

1. Hash function is a function that **takes a single input** which is **message** and gives an output as a **short distinct random-looking number.**

2. **Different** inputs provides **different** outputs.

3. This is **Modification Detection Code (MDC)**
   
4. After giving the input we get output, the output that we get is known as **Hash**

5. Hash can be written as

    
### h = H (M)

6. Another name of the output we get from hash function is digital fingerprint, imprint, message digest.

Mathematically we have to use Hash as a **H()**

Input will be the variable-length of data indicated as **M**. this can be of any size. 

Output is also called as digest. It has the fixed length, hash value is denoted as h.

#### Lets take an example:
possible hash values would be :**000, 001, 010, 011, 100, 101, 110, 111.**

suppose I am choosing random input

**H(M1 = 01010011) -----> output h1 = 011**
**H(M1 = 01010011) -----> output h1 = 011**

#### This says that if we are giving the **same input** it will give the **simillar output**. But if I choose **different input** values then we will get **different output** but the output we will gwt will be among **000, 001, 010, 011, 100, 101, 110, 111.** one of these.



### Selected Cryptographic Hash Functions

![selected cryptographic hash functions](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/dcf5be63-5546-4e12-ab67-86d495f5d4b1)

In today's time SHA -2 and SHA-3 are used. But, SHA-2 is more secure so SHA-2 is used widely.


## Hash Function in Powershell

![HASH powershell 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/dd88bbca-8dae-4162-a3da-3b3b4255ca16)

In the above given example I have 3 files. **(file 1.txt, file 2.txt, file 3.txt)**

As we can see that **file 1.txt and file 2.txt** has **same contents "My name is Harshil"** so the hash values both the files are exactly similar.

But, the content in **file 3.txt** is** different** to file 1.txt and file 2.txt **"My name is Harshilkumar Ashish Patel"**. So, the Hash value for file 3.txt is different from file 1 and 2.txt.



#### We will try to employ MD5, SHA1, SHA256 algorithm

![SHA powershell 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/1876f772-a083-440f-8069-7747eb182799)

#### MD5 Produces the 128 bit output i.e. 32 digits.

#### SHA1 produces the 160 bits output.

#### SHA256 produces the 256 bits output.

#### SHA512 produces the 512 bits output.

While running this functions I tried to use the commands that my professer tought us but In my pc it was not Working. I was getting an syntax error

**PS C:\Users\harsh\pong> Get-FileHash .\file 2.txt**

**Get-FileHash : A positional parameter cannot be found that accepts**

**argument '2.txt'.**

**At line:1 char:1**

**+ Get-FileHash .\file 2.txt**

**+ ~~~~~~~~~~~~~~~~~~~~~~~~~**

    **+ CategoryInfo          : InvalidArgument: (:) [Get-FileHash], ParameterBindingException**
    **+ FullyQualifiedErrorId : PositionalParameterNotFound,Get-FileHash**

#### By online surfing i came to know that we can add " " and the filename between this  i.e. Get-FileHash .\"file 2.txt"


## Hash Function in Linux

Let's employ MD5, SHA1, SHA256 on file 1.txt

![HASH linux 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/493ccc1d-f4db-4da8-829c-554bcaa8aab9)
![HASH linux 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/ca130adf-2232-4972-8d0b-70b88f33bbbd)


## MAC1

1. As we all are familiar with the MAC because we have studied in previous units. We k now that this is MAc address. But here it is not a MAC address, MAC1 indicats the **Message Authentication Code**.

2. This is commonly used for authenticating messages.

3.  MAC takes 2 imputs (Message and a secret key) and gives an output as short, distinct and random-looking output.

4.  MAC is also known as a keyed hash function

5.  Output of the MAC is also called as tag (t).

6.  MAC is written as written

### t = MAC (K,M) 

7. MAC function is also called as HASH function therefore, it is also known as HMAC.

### h = H(K,M)


### Commmonly Required Security Properties

We use this below given properties to achieve the certain security.

If we want to authenticate our message then Hash and MAC needs this properties.

#### 1. Pre-image resistance ----> also known as **One-way**

As the name suggests one-way we cannot revert it. We give an input and we get back an output. Now we cannot revert it, we cannot find the input using output.

Best example to understand this is the "One Way Highway". Assume **point-1 as an input** and **point-2 as an output**, Suppose I want to go from **point-1 to point-2** using the **one way highway** I can go. But I **cannot use the same highway** to **go back from point-2 to point-1**.

#### 2. Second pre-image resistance ----> also known as **Weak collision resistance**

As the name suggests collision, It means two different inputs collide on the same output.

Suppose we have a message(input) and we know the has value of the message, in this case it is easy for us to calculate the hash of message. 

But it is practically impossible for an attacker to go and find another message that is different from the original one that produces the same hash value. that is to find the collision.

#### 3. Collision resistance ----> Also known as **Strong Collision Resistance**

As the name suggests **Strong Collision Resistance** it is practically impossible for the attacker to be able to choose any two messages, which, when we apply on our hash function or our Mac function, it will produce the same output.


#### There is a minor difference between **Weak collision resistance** and **Strong Collision Resistance**. in weak collision if we have given a messgae it is hard for the attacker to find another message that produces collision property. whereas, in Strong Collision Resistance if attacker chooses any 2 messages it is hard for them to be able to choose any two messages that produce a collision.


### Security Properties for Selected Applications

This is used for computer and network security such as Digital signature, Message authentication with symmmetric key and hash, Message authentication with MAC only, Message authentication using hash only, storing Password with hash. Depending upon the prupose different properties must be required. 

#### Digital Signature ---> Public key crypto + Hash(One-way, weak collision, strong collision resistnce).

#### Message authentication with symmetric key encryption and hash

#### Message usthentication with MAC only ---> (One way, weak collision, strong collision)

#### Message authentication using hash only ---> 2nd preimage resistant

#### Password storage with hash ---> preimage resistant.

The above given indicates the properties required for security.

### How MAC1  function work is. 

Sender and Receiver Share the key "K"

Even the input message is large the length of output tag is fixed and large.  

[symmetric key encryption and MAC1 function is almost simillar]


### Every one have a threat of an attacker of doing one possible attack i.e. Brute force attack.

Suppose we have MAC1, MAC2, MAC3

We have to find which one is more secure.

#### MAC1: key 80bits, tag 100 bits  ----> Attacker: **2^80 attempts to find key**, **2^100 attempts to find tag**

#### MAC2: kay 90 bits, tag 100 bits  ----> Attacker: **2^90 attempts to find key**, **2^100 attempts to find tag**

#### MAC3: key 110 bits, tag 70 bits  ----> Attacker: **2^100 attempts to find key**, **2^70 attempts to find tag**

As we all know the **main goal** of the attacker is to find the **output**.

In the above given MAC1, MAC2, MAC3. we can see that attacker have to do the **maximum number** of bruteforce attack in **MAC1 to find tag**.


## Lets solve a Question regarding the Hash and MAC.

### why should a hash function used for a password file be pre-image resistant, but does not have to be collision resistant?

#### Solution:

#### suppose we have a my username dtabase and( my password --> Hash) of myself stored in data base.

MySQL database : username, H(password)

Now, assume attacker has gained an access to the username database and got the hash value

Harshilkumar, 78k6jbybkjdys09lsjzjxhd  

As we have studied earlier about the "one-way" in which even if attacker knows the hash value he/she cannot revert the process(cannot find the original password). 

#### Therefore collision resistant is not used and

### Pre-image resistant (one-way) is secure.


### 2. Use Python to calculate the hash of an input

#### Solution:

![Hash in python code final ](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/c8328524-6d87-4e70-8afb-172d50d2da20)
![hash in python 1 final sol](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/a40be85b-5d0e-4b65-b33e-3ebad3ad7e60)

In the above given output. 

If we see the first letter "b" Bytes.

\x indicates that the next 2 digits are hex value

#### suppose we just have hex values and we want ot convert it to bytes. here we can use 

h1_bytes = bytes.fromhex(h1_hex)

print(h1_bytes)

#### instead of using this code we can also use command 

![hash in python 2 ](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/d570a1c8-fee7-4198-87dc-5c5ad884d246)

we can see that the output we got by command and by python code both are same.


### 3. Use Python to caculate the MAC of an input

#### Solution:

![HMAC python code](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/4e32af6b-d785-4a98-ab7d-ffd1786a893f)
![HMAC python sol final](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/53d22577-730f-41b4-9dae-f6c8e2d5c50c)

In the above solution we can see the difference between the difference between the "Hash" and "HMAC"

**As we saw before "Hash" gives the same output when given the same input again and again.**

**But, In "HMAC" we can see that we are giving the same input and when we run the python code agin and again with the same input, we get different "key and tag" everytime.**

In the output given below we can see that, we got 2 lines with a random numbers and letters.

#### The first line is "Key"

#### Second line is "Tag"




