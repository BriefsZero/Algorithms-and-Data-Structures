class SuffixTrieNode(object):
    def __init__(self, letter):
        self.letter = letter
        self.children = []
        self.end_of_word = False
        self.counter = 1

def add(root, word):
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
            elif z == 11:
                print("")
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
        # if node.children[x] is None:
        #     new = SuffixTrieNode(word[y])
        #     new.children = [None] * len(word)
        #     node.children[x] = new
        # if node.children[x].letter == word[y]:
        #     temp = word[y+1:]
        #     node.counter = len(word)
        #     node = node.children[x]
        #     for y in range(len(temp)):
        #         new = SuffixTrieNode(temp[y])
        #         new.children = [None] * len(word)
        #         node.children[x] = new
        #         node.counter = len(temp)-y
        #         node = new
        # x = z
        # x += 1
        # node.end_of_word = True

def search(root, string):
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
    return s[::-1]

root = SuffixTrieNode('*')
word = reverse("cabcdbadccc")
data = "cabcdbadccc"
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
        if search(root,subStringList[x][0]):
            results.append(subStringList[x])
        else:
            failed = subStringList[x][1]
    x += 1
print(results)