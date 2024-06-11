# Week 2

[Return to contents](./README.md)


# This week consist of:
1) Various ways of encrypting and decrypting data using caesar cipher
2) Monoalphabetic (substitution) cipher - (Encryption and decryption)
3) Playfair Cipher (Encryption and Decryption)
4) Polyalphabetic Ciphers
   
    Vigenere Cipher
   
6) Transposition Techniques
   
    Rail Fence Cipher
   

## Caesar Cipher (Brute force)
In the earlier given examples in week 1 we have a secret key by which we can decrypt the message.

But what if we do not know the key? In such cases we need to try all possible keys that is "key 1 to 26", we can do it manually by hand which can consume a lot of time. instead of doing it manually by hand we can use a software to decrypt message using a simple command.

### Decrypting messege if we dont know the key, In this case we need to perform brute force attack
### In this case we don't know what key is 
![encryption and decryption using python(forloop) caesar](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/b53b5aba-58c8-4679-8cbf-08afcaab64d8)

After running this code we come to know that the key is "25" and the plain text is "caesar".

### text_to_num
In caesar cipher we can encrypt the data into numbers using python (text_to_num)

![Week 2 caesar cipher 1](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/a782f93f-54f3-4aff-9eea-41988139da06)

A) In the above given code, there is a encrypt() function which takes 2 parameters (key, plaintext) key which will be used to encrypt and plaintext which needs to be encrypt.
B) By passing argument plaintext, englishcipher.text_to_num function is called. this function encrypt the plaintext to the number according to the position of the alphabet from 0 to 25 

(example: starting from 0 "C" is on 2nd position, so numerical value of "c" is "2"

 "a" is on 0 position , so numerical value of "a" is "0"
 
 "e" is on 4th position , so numerical value of "e" is "4"
 
 "s" is on 18th position , so numerical value of "s" is "18"
 
 "a" is on 0 position , so numerical value of "a" is "0"
 
 "r" is on 17 position , so numerical value of "r" is "17").
 
C) print(plaintext_list) give output as a list of numbers (encrypted plaintext).

see the output below:

![week 2 caesar cipher 2](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/f2cff0d4-6696-4571-aa42-4d212058fe15)


We can also print the same output but in list by using the same code but by adding couple of line into it.

![Week 2 ceaesar cipher 3](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/25d9b53c-0b05-40a3-a6b6-a488d899f54f)

for p in plaintext_list:

    print(p) 

Above given lines are added in the python code and what these lines do is , the first line ( for p in plaintext_list) is a for-loop for iteration, it iterates over every charaters in provided plaintext(caesar) and for each and in every iteration each alphabets in the plaintext is assigned to variable (p), so the print(p) will print out every value of the plaintext one by one.

![week 2 caesar cipher 4](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/f345984d-b37a-49dd-a427-f951e1fc72d9)


also by using the logic 

(p + key) % 26 

we can encrypt the data 

![Week 2 caesar cipher 5](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/2b6c1e71-c7c1-465a-b532-649e46da327e)

ouptut:

![Week 2 caesar cipher 6](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/c8de155b-94a8-4c59-b110-176da76d6304)


### num_to_text

![image](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/6d208ca4-d717-4886-8e31-5836511d279f)


This script converts the numbers in the plaintext and converts plaintect into ciphertext. 

By using "num_to_text" from "englishcipher" the code can convert the numberical value into alphabets(ciphertext).

 


## Monoalphabetic (Substitution) Cipher.

In monoalphabetic cipher is a form of symmetryc encryption because the key which is used to encrypt the messege, the same key will be used to decrypt message.

### Encryption

To encrypt data, First we need to write the alphabets in order in a horizontal line and below that we need to randomly place the alphabets which should not be in order each letter should be used only once. (see below example)

### a - b - c - d - e - f - g - h - i - j - k - l - m - n - o - p - q - r - s - t - u - v - w - x - y - z     <----- Alphabet 
### y - v - g - j - c - a - l - p - r - b - f - d - h - t - w - z - x - m - o - k - n - q - s - u - e - i     <----- Key


Line 2(key) is a unique key which is a symmetric key. It is used to encrypt and decrypt the data. Key can be generated or made by randomly arranging the alphabet letters and each letter is used once.

lets take an example and encrypt and decrypt a key.

suppose we need to encrypt a message "caesar"

A) lets find the first letter "c" in the first line (Alphabet), now look which letter is placed below the letter "c". The letter placed below letter "c" is "g"

                            c = g

B) lets find the second letter "a" in the first line (Alphabet), now look which letter is placed below the letter "a". The letter placed below letter "a" is "y"

                            a = y

C) lets find the third letter "e" in the first line (Alphabet), now look which letter is placed below the letter "e". The letter placed below letter "e" is "c"

                            e = c

D) lets find the fourth letter "s" in the first line (Alphabet), now look which letter is placed below the letter "s". The letter placed below letter "s" is "o"

                           s = o

E) lets find the Fifth letter "a" in the first line (Alphabet), now look which letter is placed below the letter "a". The letter placed below letter "a" is "y"

                           a = y

F) lets find the sixth letter "r" in the first line (Alphabet), now look which letter is placed below the letter "r". The letter placed below letter "r" is "m"

                           r = m


So, after following these steps we get the encrepytd text "gycoym"


### Decryption
to decryption the messege "gycoym" we need to follow the same steps but in opposite direction (we need to find the alphabets in the second line (key) and look which letter is present in above that letter in the first line (Alphabet).

### a - b - c - d - e - f - g - h - i - j - k - l - m - n - o - p - q - r - s - t - u - v - w - x - y - z     <----- Alphabet 
### y - v - g - j - c - a - l - p - r - b - f - d - h - t - w - z - x - m - o - k - n - q - s - u - e - i     <----- Key


let's decrypt "gycoym".

A) lets find the first letter "g" in the second line (key), now look which letter is placed above the letter "g". The letter placed above the letter "g" is "c".

                           g = c

B) lets find the second letter "y" in the second line (key), now look which letter is placed above the letter "y". The letter placed above the letter "y" is "a".

                           y = a

C) lets find the third letter "c" in the second line (key), now look which letter is placed above the letter "c". The letter placed above the letter "c" is "e".

                           c = e

D) lets find the fourth letter "o" in the second line (key), now look which letter is placed above the letter "o". The letter placed above the letter "o" is "s".

                           o = s

E) lets find the fifth letter "y" in the second line (key), now look which letter is placed above the letter "y". The letter placed above the letter "y" is "a".

                           y = a

F) lets find the sixth letter "m" in the second line (key), now look which letter is placed above the letter "m". The letter placed above the letter "m" is "r".

                           m = r


## Playfair Cipher 
5x5 matrix is created using a keyword, this encrypts couple of letters. characters "i" and "J" both are treated similar. in this matrix letter "x" is used to place where the letters are in pair or repeated. Such as, hello ------>  helxlo 

There are some rules to encrypt the message using playfair cipher.
1) Split the plaintext into pairs of letters (input pairs)
2) Separate by special letter (e.g. 'x') if letters in pair are same
3) pad with special letter (e.g. 'x') at end
4) If input pair are on same row, shift right to get output pair
5) If input pair are on same column, shift down to get output pair
6) otherwise, ouput letter is on same row as input letter and same column as paired letter

   


### Encryption
lets take an example, to encrypt my name "Harshil" using playfair cipher.

![WhatsApp Image 2024-04-07 at 2 42 02 PM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/a8fe89b0-cf6d-4fee-8ac2-bdb4fcca2a84)


according to the rules given above we have to divide the all the letters into a pair and my name has 7 letters, and there will be 3 pairs "HA  -  RS  -  HI" and the last letter "l" will be alone, and the above given rules says that the x will be added to the last letter it it is nit in pair so the pairs will be.

[HA  -  RS  -  HI  -  LX]

let's solve it step by step.

### Step 1 and Step 2

![WhatsApp Image 2024-04-07 at 2 39 10 PM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/f856f9e6-ab55-4e74-b602-59da3e938255)


1) For "HA" find "H" and "A" in the matrix, and trace the row and column and replace the letter "E and T" with "HA"
2) For "RS" find "R" and "s" in the matrix, and trace the row and column and replace the letter "A and T" with "RS"

### Step 3:

![WhatsApp Image 2024-04-07 at 2 39 11 PM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/f36a5cad-9da7-43fb-a32c-36cf1c8a1360)

For "HI" find "H" and "I" in the matrix, trace the row and column and replace the letter "F and C" with "HI"


### Step 4:

![WhatsApp Image 2024-04-07 at 2 39 11 PM (1)](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/0f759e13-22d7-49cc-ac8f-1177f7e19933)

For "LX" find "L" and "X" in the matrix, trace the row and column and replace the letter "B and V" with "LX"


### Final solution
![WhatsApp Image 2024-04-07 at 3 15 00 PM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/775bbb69-d304-4aed-af96-1b1e1834ff4c)



 ## Decryption
 To decrypt my name "Harshil" simply reverse the method we used to encrypt.

 ![WhatsApp Image 2024-04-07 at 3 29 25 PM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/74d9e83d-29d8-4a7f-bf33-5a96336ce82c)

### steps:

![WhatsApp Image 2024-04-07 at 3 31 31 PM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/84c73b2b-48e5-46b8-b440-b60be15bde2d)


![WhatsApp Image 2024-04-07 at 3 33 03 PM](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/560d4161-240a-4868-ae8a-538fb7af05f4)


### Final Solution

![WhatsApp Image 2024-04-07 at 3 34 50 PM (1)](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/71171a78-a1d3-4fa7-8f93-0f07b57dec22)


### Polyalphabetic Ciphers
### Vigenere:
To encrypt the data using this cipher we need a "keyword" and we need to use each letter of the keyword to encrypt each letter of the "plaintext". suppose we have a keyword "KEY" and we have to encrypt a message "VIGENERE", to encrypt this messege we have to encrypt every letter by letter. 

For example:-

1) First word of "VIGENERE" "V" will be encrypted by using first word "K" of  keyword key.
2) Second word of "VIGENERE" "I" will be encrypted by using second word "E" of  keyword key.
3) Third word of "VIGENERE" "G" will be encrypted by using third word "y" of  keyword key.
 now the y is the last letter of keyword key and we need continue encrypting the rest of the word using the keyword "key" again and again until the wjhole word is encrypted.

lets take an example
we have to encrypt a sentence "man under a tree" using a key "under"

![VIGENERE CIPHER EXAMPLE](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/83b9c0fb-9a08-483e-b09f-15968133cf7f)

encrypting all the letters one by one is very leanthy and time cinsuming process, to save our time we can simply use a software to encrypt all the words one by one.

simply use python3 on the linux system and import pycipher module.

>>> import pycipher

>>> pycipher.Caesar(20).encipher("m")

'G'

>>> pycipher.Caesar(13).encipher("a")

'N'

>>> pycipher.Caesar(3).encipher("n")

'Q'

>>> pycipher.Caesar(4).encipher("u")

'Y'

>>> pycipher.Caesar(17).encipher("n")

'E'

>>> pycipher.Caesar(20).encipher("d")

'X'

>>> pycipher.Caesar(13).encipher("e")

'R'

>>> pycipher.Caesar(3).encipher("r")

'U'

>>> pycipher.Caesar(4).encipher("a")

'E'

>>> pycipher.Caesar(17).encipher("t")

'K'

>>> pycipher.Caesar(20).encipher("r")

'L'

>>> pycipher.Caesar(13).encipher("e")

'R'

>>> pycipher.Caesar(3).encipher("e")

'H'

after completing this steps your ciphertext will be 

![image](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/bb8eda66-1c71-4d89-8317-e44b8d479387)


## Transposition Techniques
## Rail Fence Cipher
To encrypt the message using the rail fence cipher we have to first select the depth and writh the message in zig-zag manner according to the depth.

Suppose we have a "depth = 4" and we are encrypting a message "Rail Fence Cipher"

![image](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/94163a79-6fea-4e11-8a1f-1e4a7ed57b9c)

as shown in the picture the depth 4 means "4 letters going down in slant direction and starting from 4th letter 4 letters are going up we have to write each letter 1 by 1 in cross line 

after writing in zig-zig manner we have to encrypt it by writing the letters row-wise

For example in the above given picture, 
start writing letters without giving a space,

from 1st row in the picture, first row has "RNH"
Second row has letters "AECPE"
third row has letters  "IFEIR"
fourth row has letters "LC"

combine althogether in one line without giving space 
"RNHAECPEIFEIRLC"

![image](https://github.com/cquict/coit13240y24t1-journal-harshilkumar691/assets/128027207/0167f47c-f63b-42ab-8b25-d9bf42447857)







