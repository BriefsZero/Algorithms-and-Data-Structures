class TrieNode(object):
    def __init__(self, type):
        """
        Initializer for TrieNode
        Time complexity: Best: O(1)
        Worst: O(1)
        Space complexity: Best: O(10)
        Worst: O(26)
        Error handle: N/A
        Return: N/A
        Parameter: type of input
        Precondition: N/A
        """
        if type is int:
            self.children = [None] * 10
        else:
            self.children = [None] * 26
        self.data = []
        self.isEndOfWord = False

class SuffixTrieNode(object):
    def __init__(self, letter):
        """
        Initializer for SuffixTrieNode
        Time complexity: Best: O(1)
        Worst: O(1)
        Space complexity: Best: O(1)
        Worst: O(1)
        Error handle: N/A
        Return: N/A
        Parameter: letter for node
        Precondition: N/A
        """
        self.letter = letter
        self.children = []
        self.end_of_word = False
        self.counter = 1


class Trie(object):
    def __init__(self, type):
        """
        Initializer for SuffixTrieNode
        Time complexity: Best: O(1)
        Worst: O(1)
        Space complexity: Best: O(1)
        Worst: O(1)
        Error handle: N/A
        Return: N/A
        Parameter: Type of input
        Precondition: N/A
        """
        self.type = type
        self.root = self.getNode()
        self.count = 0

    def getNode(self):
        """
        Grabs a instance of TrieNode
        Time complexity: Best: O(1)
        Worst: O(1)
        Space complexity: Best: O(1)
        Worst: O(1)
        Error handle: N/A
        Return: TrieNode object
        Parameter: N/A
        Precondition N/A
        """
        return TrieNode(self.type)

    def _charToIndex(self, ch):
        """
        Converts the given character to a number if its a letter
        Time complexity: Best: O(1)
        Worst: O(1)
        Space complexity: Best: O(1)
        Worst: O(1)
        Error handle: Checks to see if int or letter and then returns considering the two
        Return: The number associate with the value given
        Parameter: The value to be converted
        Precondition: A valid number or letter
        """
        try:
            ch = int(ch)
        except ValueError:
            return ord(ch.lower()) - ord('a')
        else:
            return ch

    def insert(self, key, data):
        """
        Insert the given key into the Trie with the data attached
        Time complexity: Best: O(n), where n is the length of the key
        Worst: O(n), where n is the length of the key
        Space complexity: Best: O(key + data), where T is the Trie and nm is the length of the input
        Worst: (key + data), where T is the Trie and nm is the length of the input
        Error handle: Handles if given incorrect data through other functions
        Return: N/A
        Parameter: Key - The key for which to be inserted into the tree
                   Data - The data associated with that key
        Precondition: A valid key to insert into Trie
        """
        pCrawl = self.root
        length = len(key)
        for level in range(length):
            index = self._charToIndex(key[level])

            if not pCrawl.children[index]:
                pCrawl.children[index] = self.getNode()
            pCrawl = pCrawl.children[index]

        pCrawl.isEndOfWord = True
        pCrawl.data.append(data)

    def search(self, key):
        """
        Given a prefix key, will search trie and return the keys associated with key
        Time complexity: Best: O(1), where first character is not in trie
        Worst: O(n), n being length of key
        Space complexity: Best: O(1), where no results are found
        Worst: O(T) where every result in trie
        Error handle: checks to see if key is valid
        Return: List of valid keys according to search
        Parameter: The key of which to search the trie
        Precondition: A valid key to search, doesnt have to exist in trie
        """
        pCrawl = self.root
        length = len(key)
        flag = False
        lists = []
        for level in range(length):
            index = self._charToIndex(key[level])
            if not pCrawl.children[index] and flag is False:
                return lists
            elif not pCrawl.children[index] and flag is True:
                return lists
            pCrawl = pCrawl.children[index]
            flag = True

        if flag is True:
            return self.displayTrie(pCrawl,lists)


    def displayTrie(self, node, lists):
        """
        A function for pulling out all the records from the given key prefix
        Time complexity: Best: O(1), being one node to pull
        Worst: O(n*m) n being the number of keys and m being max length of a key
        Space complexity: Best: O(1), 1 or no lists
        Worst: O(T) the whole trie
        Error handle: If nothing returns nothing
        Return: Returns the keys associated with your search
        Parameter: The node at which to start pulling keys from and the list to fill
        Precondition: A valid node
        """
        lists = self.displayTrieAux(node, lists)
        return lists


    def displayTrieAux(self, node, lists):
        """
        The recurssive function that pulls the keys from the trie
        Time complexity: Best: O(1), being one node to pull
        Worst: O(n*m) n being the number of keys and m being max length of a key
        Space complexity: Best: O(1), 1 or no lists
        Worst: O(T) the whole trie
        Error handle: If nothing returns nothing
        Return: Returns the keys associated with your search
        Parameter: The node at which to start pulling keys from and the list to fill
        Precondition: A valid node
        """
        if node.isEndOfWord is True:
            for lines in node.data:
                lists.append(lines)
                self.count += 1

        if self.type is int:
            num = 10
        else:
            num = 26
        for i in range(num):
            if node.children[i]:
                self.displayTrie(node.children[i], lists)
        return lists


def readData(filename):
    """
    Given a filename, returns a list full of data from the file
    Time complexity: Best: O(n*m) being the number of lines in the file and m being the max characters in a file
    Worst: O(n*m)
    Space complexity: Best: O(n*m)
    Worst: O(n*m)
    Error handle: If not a valid filename, prints and error and returns nothing
    Return: Returns a list full of data from file
    Parameter: The filename of the file to be read
    Precondition: A valid filename
    """
    datab = []
    try:
        data = open(filename, 'r')
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return None
    else:
        for line in data:
            line = line.split(" ")
            datab.append(line)
    return datab

def readString(filename):
    """
    Given a filename, returns a list full of data from the file
    Time complexity: Best: O(n) being the number of characters in the file
    Worst: O(n)
    Space complexity: Best: O(n)
    Worst: O(n)
    Error handle: If not a valid filename, prints and error and returns nothing
    Return: Returns a list full of data from file
    Parameter: The filename of the file to be read
    Precondition: A valid filename
    """
    string = ""
    try:
        data = open(filename, 'r')
    except FileNotFoundError as fnf_error:
        print(fnf_error)
        return None
    else:
        for line in data:
            string = line
    return string

def createTrie(data, query):
    """
    Given a set of data and the query type, will build a Trie
    Time complexity: Best: O(T) - where T is the number of characters in all identication numbers and all last names
    Worst: O(T)
    Space complexity: Best: O(T + NM)
    Worst: O(T + NM)
    Error handle: If not a valid query will print an error
    Return: The Trie full of data
    Parameter: The data to be inserted and the query to be searched
    Precondition
    """
    try:
        int(query)
    except ValueError:
        num = 3
        database = Trie(str)
    else:
        num = 1
        database = Trie(int)
    for line in data:
        database.insert(line[num], line)
    return database


def query(filename, id_prefix, last_name_prefix):
    """
    Functionality of the function
    Time complexity: Best: O(k + l + nk + nl) - k is length of id_prefix, l is length of last_name_prefix, nk is number of records matching
id_prefix, nl number  records matching last_name_prefix
    Worst: O(k + l + nk + nl) - k is length of id_prefix, l is length of last_name_prefix, nk is number of records matching
id_prefix, nl number  records matching last_name_prefix
    Space complexity: Best: O(n), n being the number of results
    Worst: O(n), n being the number of results
    Error handle: Not a valid query, will handle errors
    Return: The results from the query
    Parameter: Filename of the data to be read, id and last name to be searched
    Precondition: A valid filename, id and lastname
    """
    data = readData(filename)
    idTrie = createTrie(data, id_prefix)
    idRes = idTrie.search(id_prefix)
    if len(idRes) == 0:
        return []
    data = idRes
    LastTrie = createTrie(data, last_name_prefix)
    data = LastTrie.search(last_name_prefix)
    res = []
    for person in data:
        res.append(person[0])
    return res

def add(root, word):
    """
    Adds a node to the Suffix Trie
    Time complexity: Best: O(k^2) K is the total number of characters in the input string
    Worst: O(k^2) K is the total number of characters in the input string
    Space complexity: Best: O(k^2)
    Worst:O(k^2)
    Error handle: No root given, will fail
    Return: N/A
    Parameter: Root being the root of the suffix trie, word to be added to the trie
    Precondition: A valid root and word
    """
    node = root
    node.children = [None] * len(word)
    x = 0
    wordNum = 0
    while x < len(word):
        node = root
        found = False
        y = 0
        z = x
        while y < len(node.children) and z < len(word):
            if not node.children[y]:
                new = SuffixTrieNode(word[z])
                new.children = [None] * len(word)
                node.children[y] = new
                node = node.children[y]
                z += 1
                x = z
                break
            elif node.children[y] and node.children[y].letter == word[z]:
                node = node.children[y]
                y = 0
                z += 1
                continue
            y += 1

        temp = word[x:]
        y = 0
        w = 0
        while y < len(node.children) and w < len(temp):
            if node.children[y] is None:
                new = SuffixTrieNode(temp[w])
                new.children = [None] * len(word)
                node.children[y] = new
                node = new
                y = 0
                w += 1
                continue
            else:
                y += 1
        node = root
        wordNum += 1
        x = wordNum


def search(root, string):
    """
    Searches the suffix trie for a given substring
    Time complexity: Best: O(n) being the length of the string
    Worst: O(n) being the length of the string
    Space complexity: Best: O(1)
    Worst: O(1)
    Error handle: N/A
    Return: True or false depending on given string
    Parameter: The root of the suffix trie and the string to be searched
    Precondition: A valid root and string
    """
    node = root
    y = 0
    x = 0
    while x < len(node.children):
        if node.children[x]:
            if node.children[x].letter == string[y]:
                node = node.children[x]
                found = True
                y += 1
                x = 0
            else:
                x += 1
        else:
            return False
        if y == len(string):
            return True

    return False

def reverse(s):
    """
    Reverses a string
    Time complexity: Best: O(n) - n being length of string
    Worst: - n being length of string
    Space complexity: Best: O(1)
    Worst: O(1)
    Error handle: N/A
    Return: A reversed string
    Parameter: A string to be reversed
    Precondition: A valid string
    """
    return s[::-1]

def reverseSubstrings(filename):
    """
    Given a file with a string, finds what substrings are found in the reversed order of the string
    Time complexity: Best: O(K^2 + P) - K total number of characters in string, P total length of substrings whose
    reverse appears in the string
    Worst: O(K^2 + P)
    Space complexity: Best: O(K^2 + P)
    Worst: O(K^2 + P)
    Error handle: Invalid file will raise error and given nothing
    Return: Results of which substrings are in the reversed string
    Parameter: A file to be read
    Precondition: A valid filename
    """
    data = readString(filename)
    root = SuffixTrieNode('*')
    word = reverse(data)
    subStringList = []
    results = []
    add(root, word)
    for x in range(0, len(data)):
        for y in range(x + 2, len(data) + 1):
            if len(data[x:y]) != len(data):
                subStringList.append([data[x:y], x])

    failed = None
    x = 0
    while x < len(subStringList):
        if failed != subStringList[x][1]:
            if search(root, subStringList[x][0]):
                results.append(subStringList[x])
            else:
                failed = subStringList[x][1]
        x += 1
    return results


def task1(lines):
    print("TASK-1:")
    print(lines)
    file = input("Enter the file name of the query database : ")
    id = input("Enter the prefix of the identification number : ")
    last = input("Enter the prefix of the last name : ")
    print(lines)
    query_results = query(file, id, last)
    print(len(query_results), "record/s found")
    for item in query_results:
        print("Index number :", item)
    print(lines)

def task2(lines):
    print("TASK-2:")
    print(lines)
    file = input("Enter the file name for searching reverse substring: ")
    print(lines)
    print(reverseSubstrings(file))
    print(lines)

def main():
    LINES = "---------------------------------------------------------------------"
    task1(LINES)
    task2(LINES)



if __name__ == '__main__':
    main()



#