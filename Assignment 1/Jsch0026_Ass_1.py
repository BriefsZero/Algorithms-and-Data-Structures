def preprocess(filename):
    """
    Reads file into a list, removes any punctuation, verbs and articles
    and makes each element in the list a word
    @complexity: O(nm), where n is the amount of words and m is the maximum amount of characters in a word
    @precondition: A valid filename
    @postcondition: A list with the words loaded onto the list
    :param filename: the filename of the file to be loaded
    :return: A list with the words loaded onto it
    """
    verbs_and_articles = ('am', 'is', 'are', 'was', 'were', 'has', 'have', 'had', 'been', 'will', 'shall', 'may', 'can',
                        'would', 'should', 'might', 'could', 'a', 'an', 'the')
    punctuation = (',', '.', '?', '!', ':', ';', '"', ' ', '\t', '\n')
    words_list = []
    word = ''
    text_file = open(filename, 'r')
    for line in text_file:
        for letter in line:
            if letter not in punctuation:
                word += letter
            else:
                if word not in verbs_and_articles and not word == '':
                    words_list.append(word)
                    word = ''
                else:
                    word = ''
    return words_list


def wordSort(alist):
    """
    A algorithim for sorting an list full of words. Implements Radix Sort
    @precondition: A list with words that can be sorted in it
    @postcondition: A list sorted in A-Z order
    @complexity: O(nm) as it radix sorts each letter in the word, n being words and m being max letters in a word
    :param alist: A list with words to be sorted
    :return: A sorted list of words
    """
    base = 27
    max_num = len(alist[0])
    for i in range(len(alist)):
        if len(alist[i]) > max_num:
            max_num = len(alist[i])
    max_num -= 1
    for x in range(max_num-1, -1, -1):
        alist = radixSort(alist, x, base)

    return alist


def radixSort(alist, num, base):
    """
    A implementation of radix sort for sorting of strings
    @precondition: A list with words that can be sorted in it
    @postcondition: A list sorted in A-Z order
    @complexity: O(n) as it only cycles through once
    :param alist: A list full of letters/ words in the english language
    :param num: The current index of the word, e.g current letter
    :param base: The highest number of which the words go up to
    :return: returns the list in A-Z order
    """
    count_arr = [0] * base
    n = len(alist)
    for y in range(n):
        count_arr[getDigit(alist[y], num)] += 1

    temp_pos = [0] * base
    temp_pos[0] = 1
    for x in range(base):
        temp_pos[x] = temp_pos[x-1] + count_arr[x-1]

    temp_arr = [0] * n
    for x in range(n):
        temp_arr[temp_pos[getDigit(alist[x], num)]-1] = alist[x]
        temp_pos[getDigit(alist[x], num)] += 1

    for x in range(len(temp_arr)):
        alist[x] = temp_arr[x]

    # work-around need to fix
    alist.insert(0, alist[-1])
    alist.pop(-1)
    return alist


def wordSort2(alist):
    """
    A variation of wordSort for sorting an list full of words at index 0 and numbers at index 1.
    Only sorts into alphabetical order
    @precondition: A list with full of words at index 0 and numbers at index 1
    @postcondition: A list sorted in A-Z order
    @complexity: O(nm) as it radix sorts each letter in the word, n being words and m being max letters in a word
    :param alist: A list with words to be sorted
    :return: A sorted list of words
    """
    base = 27
    max_num = len(alist[0][0])
    for i in range(len(alist)):
        if len(alist[i]) > max_num:
            max_num = len(alist[i][0])
    max_num -= 1
    for x in range(max_num-1, -1, -1):
        alist = radixSort2(alist, x, base)

    return alist


def radixSort2(alist, num, base):
    """
     A variation of radixSort for sorting of strings and numbers at index 1
    @precondition: A list with full of words at index 0 and numbers at index 1
    @postcondition: A list sorted in A-Z order
    @complexity: O(n) as it only cycles through once
    :param alist: A list full of letters/ words in the english language
    :param num: The current index of the word, e.g current letter
    :param base: The highest number of which the words go up to
    :return: returns the list in A-Z order
    """
    count_arr = [0] * base
    n = len(alist)
    for y in range(n):
        count_arr[getDigit(alist[y][0], num)] += 1

    temp_pos = [0] * base
    temp_pos[0] = 1
    for x in range(base):
        temp_pos[x] = temp_pos[x-1] + count_arr[x-1]

    temp_arr = [0] * n
    for x in range(n):
        temp_arr[temp_pos[getDigit(alist[x][0], num)]-1] = alist[x]
        temp_pos[getDigit(alist[x][0], num)] += 1

    for x in range(len(temp_arr)):
        alist[x] = temp_arr[x]

    # work-around need to fix
    alist.insert(0, alist[-1])
    alist.pop(-1)
    return alist


def getDigit(letter, num):
    """
    A function that given a letter returns the number that represents such letter
    @precondition: A letter in the english language
    @postcondition: A number represented for the letter
    @complexity: O(1)
    :param letter: A letter in lowercase in the english alphabet
    :param num: The current index of the word
    :return: The number of the letter
    """
    if len(letter) <= num:
        return 0
    return ord(letter[num]) - 96


def wordCount(alist):
    """
    An algorithim that given a list will return a list with the word and the number of times that word appears
    @precondition: A list with words in it in alphabetical order
    @postcondition: A list with words and occurrences
    @complexity: O(nm) list with words in it
    :param: A list with words in it
    :return: A list with the word then number of occurrences e.g. [word, occurrences]
    """
    current_word = alist[0]
    count = 0
    word_count = [[],]
    word_count[0] = 0

    for x in range(len(alist)):
        if alist[x] == current_word:
            count += 1
        else:
            word_count[0] += count
            word_count.append([current_word, count])
            count = 1
            current_word = alist[x]
    word_count[0] += count
    word_count.append([current_word, count])

    return word_count


def swap(heap, parent, current):
    """
    A simple function for swapping two elements
    @precondition: A list with two words to be swapped
    @postcondition: A list with words that have been swapped
    @complexity: O(1)
    :param heap: A list/heap of the elements being swapped
    :param parent: One of the elements to be swapped
    :param current: One of the other elements to be swapped
    :return: A list/heap with the two elements swapped
    """
    temp = heap[current]
    heap[current] = heap[parent]
    heap[parent] = temp


def countSort(alist, radix):
    """
    A algorithm for sorting a list via its numbers
    @precondition: A list with numbers at index 1
    @postcondition: A list that has been sorted
    @complexity: O(n)
    :param alist: A list with numbers in the 1 index
    :param radix: The max number
    :return: A sorted list
    """
    radix = radix + 1
    clist = [0] * int(radix)
    for i in range(0, len(alist)):
        clist[alist[i][1]] = clist[alist[i][1]] + 1

    clist[0] = clist[0] - 1
    for j in range(1, radix):
        clist[j] = clist[j] + clist[j - 1]

    result = [None] * len(alist)

    count = len(alist)
    rev_list = []
    for i in range(count):
        rev_list.append(alist[count - i - 1])

    for x in range(len(alist)):
        result[clist[alist[x][1]]] = alist[x]
        clist[alist[x][1]] = clist[alist[x][1]] - 1

    rev_list = []
    for i in range(count):
        rev_list.append(result[count - i - 1])

    return rev_list


def siftUp(heap, pos):
    """
    Keeps swapping nodes that are too small with its parent, thus moving it up until smallest element is in position
    @precondition: A legal min-heap
    @postcondition: A list with new element in min-heap
    @complexity: O(log(n))
    :param heap: A built min-heap
    :param pos: the start position to start the siftup
    :return: A valid min-heap
    """
    end = len(heap)
    start = pos
    new_item = heap[pos]
    child_pos = 2*pos + 1
    while child_pos < end:
        right = child_pos + 1
        if right < end and not heap[child_pos][1] < heap[right][1]:
            child_pos = right
        heap[pos] = heap[child_pos]
        pos = child_pos
        child_pos = 2*pos + 1
    heap[pos] = new_item
    siftDown(heap, start, pos)


def siftDown(heap, start, pos):
    """
    Sifts the new item down till it finds a place that fits
    @precondition: A legal min-heap
    @postcondition: A list with new element in min-heap
    @complexity: O(log(n))
    :param heap: A already built min-heap
    :param start: The start position
    :param pos: new item position
    :return: A min-heap with new element in correct place
    """
    new_item = heap[pos]
    while pos > start:
        parent_pos = (pos - 1) >> 1
        parent = heap[parent_pos]
        if new_item[1] < parent[1]:
            heap[pos] = parent
            pos = parent_pos
            continue
        break
    heap[pos] = new_item


def heapPush(heap, item):
    """
    Pushes an item onto the heap and then sifts the heap so that its a min-hep
    @precondition: A legal min-heap
    @postcondition: A list with new element in min-heap
    @complexity: O(log(n))
    :param heap: A already built min-heap
    :param item: new item to be put in the heap
    :return: A min-heap with new element in correct place
    """
    heap.append(item)
    siftDown(heap, 0, len(heap)-1)


def heapPop(heap):
    """
    Pops an item from the root of the heap and then turns it into a min-heap again
    @precondition: A legal min-heap
    @postcondition: A list in min-heap
    @complexity: O(log(n))
    :param heap: A already built min-heap
    :return: A min-heap with every element in its correct place
    """
    pop_el = heap.pop()

    if heap:
        return_item = heap[0]
        heap[0] = pop_el
        siftUp(heap, 0)
    else:
        return_item = pop_el
    return return_item

def extractMax(heap):
    max_index = findMaximumElement(heap, len(heap))
    max_item = heap[max_index]
    if max_index != (len(heap)-1):
        current_item = heap.pop()
        heap[max_index] = current_item
        parent_pos = (max_index - 1) >> 1

        if heap[max_index][1] < heap[parent_pos][1]:
            siftUp(heap, max_index)
        else:
            siftDown(heap, max_index, len(heap) - 1)

    else:
        max_item = heap.pop()
    return max_item

def max(elem1, elem2, idx1, idx2):
    if elem1[1] > elem2[1]:
        return idx1
    elif elem1[1] < elem2[1]:
        return idx2
    return idx1

def findMaximumElement(heap, n):
    maximumElement = heap[n // 2]
    max_index = n // 2
    for i in range(1 + n // 2, n):
        max_index = max(maximumElement, heap[i], max_index, i)
        maximumElement = heap[max_index]
    return max_index

def kTopWords(alist, k):
    """
    An algorithm for finding the k largest words in a list, using a min-heap data structure
    @complexity: O(nlogk) Building heap takes log(n) time, and we build an heap of size k, n times thus nlogk
    :param alist: A list with words at index 0 and numbers at index 1
    :param k: The number for how many largest words you want to find
    :return: A list with the k largest words in the alist
    """
    heap = []
    max_num = alist[0][1]
    for x in range(0, k):
        if alist[x][1] > max_num:
            max_num = alist[x][1]
        heapPush(heap, alist[x])

    for x in range(k+1, len(alist)):
        if alist[x][1] > heap[0][1]:
            heapPop(heap)
            heapPush(heap, alist[x])
        if alist[x][1] > max_num:
            max_num = alist[x][1]

    heap = wordSort2(heap)
    heap = countSort(heap, max_num)
    return heap


def runProgram():
    lists = preprocess('Writing.txt')
    print("Words are preprocessed..")
    usr_input = input("Do I need to display the remaining words: ").capitalize()
    if usr_input == "Y":
        for x in lists:
            print(x)

    lists = wordSort(lists)
    print("\nThe remaining words are sorted in alphabetical order")
    usr_input = input("Do you want to see: ").capitalize()
    if usr_input == "Y":
        for x in lists:
            print(x)

    lists = wordCount(lists)
    print("\nThe total number of words in the writing:", lists[0])
    print("The frequencies of each word:")
    for x in range(1, len(lists)):
        print(lists[x][0], ":", lists[x][1])

    usr_input = input("\nHow many top-most frequent words do I display: ")
    print(usr_input, "top most words appear in the writing are:")
    lists.pop(0)
    lists = kTopWords(lists, int(usr_input))
    for x in range(len(lists)):
        print(lists[x][0], ":", lists[x][1])


