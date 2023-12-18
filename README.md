**Designing Password Cracking Strategy**

This project focuses on decrypting SHA-1 hashed passwords stored in "password_sha1_SJ.txt." Starting with the verification of User 1's password, "123456" [here](sha1-online.com) the objective extends to strategically cracking a significant portion of the password file. Leveraging common password-setting practices, including simple digits, English words, and combinations, the project employs Python and Hashcat to design an effective cracking system.

The project delves into decrypting SHA-1 hashed passwords in "password_sha1_SJ.txt." The file format is [User ID] [SHA-1 Hash], challenging us to unveil obscured hashes. The goal is to strategically crack as many passwords as possible, utilizing insights into common but regrettable password creation practices. In our current "password_sha1_SJ.txt" file we have 20 SHA1 hashed password stored which are composed of numbers or words or combination of both. Here, words are stored in a file named "dictionary.txt" and is used to crack single word, double word and triple word passwords. The project can be divided into 5 components based on the password type.

Before performing the cracking, we need to install hashcat locally on the machine. If using ubuntu, hashcat can be installed by using command "sudo apt install hashcat" or if using windows we can install hashcat binaries by visiting website [here (https://hashcat.net/hashcat/). In my case I have used windows as it had more processing power to crack the required number of hashes. In windows ZIP file will be installed which has to be extracted. The path where hashcat commands have to be executed is "..\hashcat-6.2.6\hashcat-6.2.6". For detailed understanding of hashcat and its working, visit [here](https://hashcat.net/wiki/). Now, lets look at each component individually- 

**Component-1 (Cracking Single Word Passwords)**

1. Utilized Hashcat with a dictionary attack.
2. Command: hashcat –m100 –a 0 "path of password_sha1_SJ.txt" "path of dictionary.txt"
3. Result: Successfully cracked 2 passwords.

**Component-2 (Cracking Double Word Passwords)**

1. Employed Hashcat with a combinator attack.
2. Command: hashcat –m100 –a 1 "path of password_sha1_SJ.txt" "path of dictionary.txt" "path of dictionary.txt"
3. Result: Successfully cracked 4 passwords.


**Component-3 (Cracking Single Word and Numbers Passwords)**

1. Utilized Python and Hashcat with a combinatory attack.
2. Generated a numbers file with number_generator.py. (Range = 9-9999)
3. Command: hashcat –m100 –a 1 "path of password_sha1_SJ.txt" "path of dictionary.txt" "path of numbers1.txt"
4. Result: Successfully cracked 4 passwords.

**Component-4 (Cracking All Numbers Passwords)**

1. Utilized Python and Hashcat with a dictionary attack.
2. Generated a numbers file with number_generator.py. (Range = 999-99999999)
3. Command: hashcat –m100 –a 0 "path of password_sha1_SJ.txt" "path of numbers.txt"
4. Result: Successfully cracked 6 passwords.

**Component-5 (Cracking Triple Word Passwords)**

1. Utilized Python and Hashcat with a combinator attack.
2. Generated double word combinations with generate_double_words.py.
3. Command: hashcat –m100 –a 1 "path of password_sha1_SJ.txt" "path of dictionary.txt" "path of double_words_dictionary.txt"
4. Result: Successfully cracked 4 passwords.

After utilizing python along with hashcat password cracker we were able to crack all the 20 hashes stored in password_sha1_SJ.txt". The "cracked_hashes.txt" file contains hashes and corresponding passwords in order.
 
