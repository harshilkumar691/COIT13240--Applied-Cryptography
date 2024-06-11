# week07

# Crypto In Practice

### In the first part of week07 we will run two python codes **client.py** and **server.py** 

**we can make an virtual machine in azure but here I already 2 virtual machines ** 

The one which I have it's host name is **"Server"**

Another virtual machine that i have it's name is **"Router"**

So, we will run the **server.py** in **Server**

And we will assume **Router** as **Client** and run **client.py** in **Router**.

I got these 2 codes from the lecture notes repository in github created by my professer.

### Given below is the code for client.py

![client code 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/f6824f37-787d-4ba3-b151-49d714c5907c)
![client code 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/77fedeae-5659-4423-b85f-e6a4f377e84a)
![client code 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/07397583-7ccb-4142-8453-ddc145ae38bb)

### Given below is the code for server.py

![Server code 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/3493f27e-7bfc-4085-8f07-855710d9cee9)
![Server code 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/69a79728-58b8-4931-a379-b6747a635f52)
![server code 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/8a34077b-c8a9-4dc6-9a8b-4591a2964de6)

#### I know that protocol is working and we will now inspect it at the network level and we will document it.

We will use one **program to capture** and **save the captured packets** in the .pcap file and then open that **pacp file in wireshark.**

#### we can use program called T-shark this comes with the wireshark when we install it.

#### we can also use tcpdump which is available in linux. we will use tcpdump

## Packet capturing and inspecting 

### Step 1: As we know that we are using 2 VMs **Server** and **Router acting as Client**. Now, to **capture packets** we have to **start 3rd VM**, for the safe site we should check that the **3rd VM** that we are using can **ping** both **Server** and **Router acting as Client**

### Step 2: First check in which **section your public ip-address is located**, in my case it is **enp0s3**. 

![ip addr ](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/983a1925-0597-4faf-b38b-3fecbaabcd0d)

### Step 3: use this command to capture packets **"sudo tcpdump -i enp0s3 -n -w client-server-1.pcap"**. press **Enter**, Right after pressing enter **it will ask for password** and after entering password it will **wait for packets to capture**.

### Step 4: Immideately run the python code **server.py** in **Server VM** and **client.py** in **RouterVM acting as Client VM**.

Use **"python3 server.py 12346"** to run python code **server.py**

In this **python3**  -----> used to run python code

**server.py**  -----> File name

**12346**  ------> port number to which the client.py will listen to.


Use **"python3 client.py 172.16.2.22 12346"** to run the python code **client.py** 

In this **python3**  -----> used to run python code

**server.py**  -----> File name

**172.16.2.22**  ------> Ip address of the "Server VM"

**12346**  ------> port number.

[Note: First run the code in **server VM** and then in **Router VM acting as client VM**]

![capture step 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/36987904-f146-4ddd-99f4-78d04d751ab0)


![packets captured](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/f412aea7-6cc4-49d6-83c3-ffdee9674b2a)

#### In the **above given figure** we can see that there are **7 packets captured**

![7 packets captured](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/3d78eaea-52d4-4617-8f4f-73d41e0b58f0)

[I didnt used client before because it was not able to ping server but with the help of chatgpt it fixed it and then used it to capture packets.]

#### we can see that we have a .pcap file in client VM used for capturing packets.

![file  pcap](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/7f4d4012-9cd1-4f80-a477-59e24af3d02e)

### Challange I faced

#### while capturing the packets i was trying to run the server.py file but it was showing the error "modulenotfound error" 

Traceback (most recent call last):

  File "server.py", line 5, in <module>
  
  from tcpclientserver import TCPServer
    
ModuleNotFoundError: No module named 'tcpclientserver'

#### To solve this I have installed "snapd" and then installed tcp-client-server-client-tool in my VM machine. then I tried to do run the server.py file but still i was getting the same error.

#### Then I tried to search some sources and files in the github unit repository there I found tcpclientserver.py file, I downloaded that file and added it to my repository where I have saved client.py and server.py and the tried to run those files. and I was able to run those files. 


### Step 5: Use FileZilla to transfer file from VM to our host pc.

### Step 6: open file client-server-1.pcap in wireshark.

![wireshark ss](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/bf5ddf65-85ec-4fa3-bf75-aab75c97e5cf)

**This shows the time when the packets are captuerd**

**Sources of packets "Ip address" and destination "ip address"**

### Example:

![inspect 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/4863950d-4414-4e80-a5d1-90abe5451954)

#### In the above given figure it shows the time and date the packets are captured and country

![inspect 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/d773d167-0489-423c-a472-c07e55363c9b)

#### above given shows the source and destination.

![inspect 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/34f92cb4-9394-423f-a167-310b58317197)

#### above given shows the source port and destination port.


### Further we will see another example of inspecting .pcap file in wireshark.

Before that we will see what are the components of secure web browser

**HTTP, SSL/TLS, HTTPS ,TCP, IP** ----->these are some of the components of the secure web browser.

### 1. HTTP (Hypertext Transfer Protocol):
In this By describing the structure and the transmission method for messages, HTTP allows web servers and clients to communicate with each other. This enables the retrival of possible resources like HTML documents.   

### 2. SSL/TLS (SecureSockets Layer/Transport Layer Security):
This layer guarantees the privacy and integrity of important information in connections over HTTPS by providing encryption as well as securing data transmission over internet.

### 3. HTTPS (Hypertext Transfer Protocol Secure): 
This is the most important difference between the secure web browser and the regular/insecure web browser. while, HTTPS is a component of a secure web browser. SSl/TLS, HTTP, TCP and IP are found in the ordinary/insecure web browser. HTTPS is the combination of HTTP and SSl/TLS. This combination avoids tampering during data exchange, and helps in creating a secure connection between client and servers.

### 4. TCP (Transmission Control Protocol):
This guarantees precise information is sent over the networks by controlling reliable data transmission through connection creation, packet sequencing, error fixing, and detection.

### 5. IP (Internet Protocol):
This allows interaction between different internet connected quipment, offers data packets across networks, gives devices unique address, and making sure that the data packets are reaching to their destinations.

we are provided a .pcap file we have to inspect it. there are so many inforamtion given in in but we will only focus on TLS messages.

![wireshark  tls](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/ee954de4-c35f-4195-a69e-19a7f81e6c1d)

In the above given figure we can see all the packets in there. But, as we discussed before thta we will only focus on TLS packets.

So, we have to just apply a display filter as **"tls"**. Then all and only TLS packes will be displayed.

We will take an example:

![wireshark tls 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/43266a1f-3982-4a84-8e7e-14e6ed88e256)

as we all know that the packets we are capturing are the web browsers.

In the above given figure we can see the some section 

**Time**

**Source** 

**Destination** 

**Protocol**

**length**

**Info**

**Source** section which indicates some **ip-addresses is the web-browser.**

**Destination** section which indicates some **ip-addresses is the web-server.**

In the Protocol section we can see **TLSv1.2**. This indicates the protocol used.

As we are focusing on the **TLS** we will examine the **Transport layer security** in the pane given below.

**TLS has two different phases,**

**1. Negotiation between client and server** -----> This means the negotiation of usage of keys, ciphers, algorithms, etc.

**2. Data transfer files** -----> This data are the data that are encrypted after negotiation and sent and received back.

**Double-click on the first packet, and the details for the first packet will be opened.**

![wireshark tls 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/78f8200c-7032-4373-b036-9d37ea8b86bb)

In the above given figure we can see dates and time under Transport layer security.

As it says client hello, this means that it is client.

**Transport layer Security --> TLSv1.2 --> Handshake Protocol --> Random.**

![wireshark tls 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/bad8fb94-dc55-4f8d-bf81-c13e551e6cde)


This time and date is called as **timestamp.**

**Below timestamp** we can see the **session id** with random letters and numbers.

With TLS when we **make a connection** and transfer a data and that connection is called as session and that connection has an ID.


### After the Session ID we can see Cipher suites.

![wireshark tls 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/364dfcc7-035d-44ff-bcc5-4bd3974a0069)

In the above given figure we can see the **cipher Suites (29 suites)**.

**Transport layer Security --> TLSv1.2 --> Handshake Protocol --> Random --> Cipher Suites (29 suites)**.

In this we can see different types ciphers if we see it carefully we are familar with some of the ciphers and algorithm.

This section says that it can use these 29 types of ciphers and algorithm.


### After the Cipher suites we can see **Compression methods**.

![Wireshark tls 5](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/b9872e42-0f8e-4a85-825e-f37e60502df1)

**Transport layer Security --> TLSv1.2 --> Handshake Protocol --> Random --> Cipher Suites (29 suites) --> Compression Methods.**.

In cryptography **compression might be used** to compress the data. But, here it says that it **do not do** compressions. the **value null (0)** indicates that **no compressions** are made and it is not going to do any compression.


Now, lets move onto next packet

![wireshark tls server 0](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/787ec1e7-441a-4f21-b053-88478eed6cf9)

![wireshark tls server 0 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/6559dcf7-d9bc-4e0c-8d6b-5dca9666a8a5)

In the above given picture we can see that, this packet contains 2 messages 

1. Server Hello
2. Certificate

#### We will first focus on **Server Hello**

![wireshark tls server 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/cdc124fe-34b4-4421-934c-af8e705f0ddf)

in the above given picture we can identify all the parameters. Such as version, session ID, compression Method.

Here we can specifically see in the cipher suite that which which cipher is used here.

**TLS_DHE_RSA_WITH_AES_256_GCM_SHA384 (0x009f)**

**TLS_DHE_RSA** -----> this indicates the key exchange algorithm **Diffie-Hellman Ephemeral (DHE)** and **RSA** for authentication.

**WITH** -----> WITH **separates** the authentication and key exchange algorithm with **the cipher**.

**AES_256_GCM** -----> AES with the **key length of 256 bits** using **Galois/Counter Mode (GCM)** mode of operation

#### This is crucial part of communication when we agree upon the crypto algorithms to use.

### As we have discussed before we will now **focus** on message **certificate.**

![wireshark tls server 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/360d6084-2d7a-4b3a-9fc5-fd28cad4ff42)

In the above given figure we can understand that the RSA encryption method is used.

We can see the  truncated public key there.

![wireshark tls server 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/91e8a740-b874-41ab-9dce-ebda3e6d0e26)

as we all know the modulud means the public key.

In the above given figure I have highlighted a line indicating the modulus with the yellow colour.

The line including the random numbers and letters are the public key.

we can also see some section where it is written **"signed certificate"**. This indicates that the term which **we think** that it is a **public key**, it is not just a public key. This public key is **sent** as a **signed certificate.**


![WhatsApp Image 2024-05-12 at 23 26 18_78ea1917](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/65f56a8a-4f44-485b-acf4-ce715529ffe9)

#### Above picture shows the communication that we saw in first 2 packets.

## Activity 

We will now solve 4 questions based on what we did.

### 1. what size DH key (Prime p) is used?

### Solution

![Wireshark Q1 ans](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/991c4c39-a003-4699-b270-1819dfb650f0)

In the figure i have highlighted an answer but i have highlighted 2 lines 

1. p length
2. p [truncated]

The p length indicates the length of the prime p.

p [truncated] which has a line of randomly placed letters and numbers are the value of p.

[**Recall:** we all know that if the value of "prime P" is larger than the attacker cannot find out the private key and secret key using descrite logarithm]

### How i found it.
#### We all Know that sender need to **exchange key (Public key)** and share the **prime p** and **generator g** to the receiver. I saw term Server key exchange in the 3rd packet so I tried to find this answer in the third packet. while inspecting in transport layer security. I noticed the term Diffie-Hellman Params.

### 2. what DH Key sizes is the client willing to use? [**Hint:** Normal DH is also called Finite Field DH (As opposed to elliptic curve DH)

### Solution

![wireshark Q2 answer](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/35c3fc5d-4734-4eef-9e50-de8e9a12f287)

### How did I found it?
#### As we all know the the hint was **Finite Field DH** and we also learned before about 2048 bits in DHKE. I was not sure where it is located. So, I started from the firstb packet and whicle inspecting I noticed FFDHE and 2048. There I got a a short-form of Finite Field DH but i was not sure about 2048 so i took help of Chat gpt to understand the term 

#### ffdhe2048
#### ffdhe3072
#### ffdhe4096
#### ffdhe6144
#### ffdhe8192

### After that I am confident about this answer.



### 3. What size RSA key is used in the certificate

### Solution

![wireshark Q3 answer](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/64318f29-ca44-4084-a2c7-a50a8f93784d)

### How did i found it?
#### My professor have tought me that "RSA key inside a certificate is signed by a trusted authority". As we saw before where the  public key is sent as the signed certificate. which means I need to find the Actual public key. While inspecting I saw a modulus and modulus is public key.
#### It is 257 bits, Ofcourse it is encrypted but if we multiply 

**257 * 8 = 2056**

#### RSA supports 

#### 2048 bits

#### 3072 bits

#### 4096 bits

#### 6144 bits

#### 8192 bits

#### 2056 comes between 2048 to 3072. 

#### Therefore, answer is 2048

### 4. If the round-tripitime (RTT) between web browser and webserver is 50ms, what is the delay from when a user clicks on a https link, until when the first web page is received by the browser.

### Soultion

As we can see the name "application data" we can start inspecting with the packet 12.

![wireshark Q4 ans 4 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/78f593fe-a5cb-4512-a2f4-1940959c7955)

in the figure given above. As we can see the packet 12 is encrypted we cannot see the data.


![wireshark Q4 final answer](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/b31c24b2-fda9-423a-aa91-3e436953de81)

let's assume that packet 12 **ip- 192.168.1.12** sent a request for a web page to **ip- 103.3.63.107**. and **ip- 103.3.63.107** sent back the reply to **ip- 192.168.1.12** in the packet 13. we can assume that the **packet 13** is the **web page**. 

There is a possibility that the web pgae is big enough that it took 3 packets to receive i.e. packet NOs: 13, 17, 18.

we will make assumtion that full web page is received after the packet 18. 

We can see the **time** colunm in the given picture we need to locate the time delay from the user clicks till he/she receives the webpage. 

We just assumed that user received the complete webpage in packet 18. 

Now locate the time of Packet 18. 

It is 0.556383

### Answer is "0.556383"








