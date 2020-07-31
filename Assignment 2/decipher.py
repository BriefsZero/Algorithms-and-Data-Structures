class Decipher:
    def __init__(self):
        self.message = ""

    def messageFind(self, encrypted_file):
        """
        This function takes the name of the encrypted file, then runs it into a function that returns a list with
        the data in it. This function then runs a DP algorithm that makes a table with the length of the longest
        string. From here a while loop will run at from the end of the word / DP table and backtrack through the table
        and find the string.
        Time complexity: O(nm)
        Space complexity: O(nm)
        Error handle: If no file is given, returns error, if no data in file, returns message with no data in file
        Return: None
        Parameter: encrypted_file - The data for the the function to find the encrypted message
        Pre - requisite: Data file to be read and fed into the program
        """
        encrypted_text = self.fileToData(encrypted_file)
        if type(encrypted_text) != list:
            print("No data in file")
            return
        else:
            first_word = encrypted_text[0]
            second_word = encrypted_text[1]
            n = len(first_word)
            m = len(second_word)
            dp = []
            for _ in range(n + 1):
                dp.append([None] * (m + 1))

            for x in range(n + 1):
                for y in range(m + 1):
                    if x == 0 or y == 0:
                        dp[x][y] = 0
                    elif first_word[x - 1] == second_word[y - 1]:
                        dp[x][y] = dp[x - 1][y - 1] + 1
                    else:
                        dp[x][y] = max(dp[x - 1][y], dp[x][y - 1])

            idx = dp[n][m]

            longest_seq = [''] * (idx+1)

            while n > 0 and m > 0:
                if first_word[n-1] == second_word[m-1]:
                    longest_seq[idx-1] = first_word[n-1]
                    n -= 1
                    m -= 1
                    idx -= 1
                elif dp[n-1][m] > dp[n][m-1]:
                    n -= 1
                else:
                    m -= 1
            self.message = ''.join(longest_seq)

    def fileToData(self, file):
        """
        Takes a file name, then reads the file and enters each character into a list, each index being a line
        Time complexity: If n is the number of lines and m is the max length of a line then its O(nm)
        Space complexity: O(nm)
        Error handle: If incorrect file name given, prints and the error and returns nothing
        Return: If correct file name given, returns list with data from the file
        Parameter: The filename
        Pre - requisite: A valid file and filename
        """
        try:
            data = open(file, 'r')
        except FileNotFoundError as fnf_error:
            print(fnf_error)
            return None
        else:
            data.seek(0)
            first_char = data.read(1)
            if not first_char:
                return None
            data.seek(0)
            data_list = []
            word = ''
            for line in data:
                for letter in line:
                    if letter != '\n':
                        word += letter
                    else:
                        data_list.append(word)
                        word = ''
            data_list.append(word)
            return data_list

    def lookup(self, substring, dictionary_data):
        """
        Take a string and a list full of words, then checks if a word is in the dictionary
        if so returns true, else false
        Time complexity: O(NM), N being the length of the word and M being the length of dictionary
        Space complexity: O(1)
        Error handle: If no list is given, returns false
        Return: True or False
        Parameter: Substring - The word to be checked, dictionary_data - list of the words to check
        Pre - requisite: A dictionary including words
        """

        size_num = len(dictionary_data)
        if type(dictionary_data) != list:
            return False
        for x in range(size_num):
            if dictionary_data[x] == substring:
                return True
        return False

    def maxx(self, dictionary):
        """
        Finds the longest word in the dictionary and returns the length
        Time complexity: O(M) M being the size of the dictionary
        Space complexity: O(1)
        Error handle: If no list is given, returns false
        Return: Length of longest word
        Parameter: A list full of words
        Pre - requisite: A list full of words
        """
        if type(dictionary) != list:
            return 0
        max_val = dictionary[0]
        for x in range(1, len(dictionary)):
            if len(dictionary[x]) > len(max_val):
                max_val = dictionary[x]
        return len(max_val)

    def wordBreak(self, dict):
        """
        This function breaks a string into words, based on the words in a given dictionary. It does this by starting
        at the end of a string and incrementing towards the start, and checking string[i:] and string[i:j]. The
        algorithm implements DP by remembering words that it has checked. It does this by checking the DP table at j
        and if its in the table at that index it will add that to the current index. After it has gone through the whole
        string, it will loop through that table and take the first element at the DP index and then increase i depending
        on the length of that word, if there isn't a value at the DP[index] there it will at the index of the string to
        the word and continue until DP{index] has a value.
        Time complexity: O(kM * NM) where N be the number of words in dictionary, M be the maximal size of the words,
        k is the size of input string
        Space complexity: O(kM + NM) where N be the number of words in dictionary, M be the maximal size of the words,
        k is the size of input string
        Error handle: If there is no string, returns nothing, if there is no dictionary, exits function
        Return: Nothing
        Parameter: Dictionary full of words
        Pre - requisite: A string
        """
        string = self.message
        if string == "":
            return
        dict = self.fileToData(dict)
        if len(dict) == 0 or not dict:
            return
        table = [None] * len(string)
        max_word = self.maxx(dict)
        curr = None

        for i in range(len(string) - 1, -1, -1):
            temp = [""]
            if len(string[i:]) > max_word:
                pass
            else:
                if self.lookup(string[i:], dict):
                    table[i] = [string[i:]]
                    curr = i
                    continue
            for j in range(i + 1, len(string)):
                if len(string[i:j]) > max_word:
                    break
                else:
                    flag = self.lookup(string[i:j], dict)
                    if curr is not None and table[curr]:
                        if curr in range(i,j):
                            if len(table[curr][0]) > len(string[i:j]):
                                continue
                            if table[j] and flag:
                                table[i] = [string[i:j]] + table[j]
                                curr = i
                                continue
                            if flag:
                                if len(string[i:j]) >= len(temp):
                                    table[i] = [string[i:j]]
                                    curr = i
                        else:
                            if table[j] and flag:
                                table[i] = [string[i:j]] + table[j]
                                curr = i
                                continue
                            if flag:
                                if len(string[i:j]) >= len(temp):
                                    table[i] = [string[i:j]]
                                    curr = i

        i = 0
        temp = ""
        while i < len(string):
            if table[i]:
                temp += str(table[i][0])
                i += len(str(table[i][0]))
            else:
                while not table[i]:
                    temp += string[i:i + 1]
                    i += 1
            if i < len(string)-1:
                temp += " "

        self.message = temp

    def getMessage(self):
        """
        Functionality of the function
        Time complexity: O(1)
        Space complexity: O(0)
        Error handle: Nothing
        Return: The string/ message
        Parameter: None
        Pre - requisite: None
        """

        return self.message


if __name__ == "__main__":
    lines = "---------------------------------------------------------------------"
    decipher = Decipher()
    enc_file = input("The name of the file, contains two encrypted texts : ")
    decipher.messageFind(enc_file)
    dict_file = input("The name of the dictionary file : ")
    print(lines)
    print("Deciphered Message is", decipher.getMessage())
    decipher.wordBreak(dict_file)
    print("True Message is", decipher.getMessage())
    print(lines)
    print("Program end")


