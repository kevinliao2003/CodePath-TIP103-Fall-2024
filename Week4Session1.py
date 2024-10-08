class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from collections import defaultdict

def lengthOfLongestSubstring(self, s: str) -> int:
        """
        U - Can the string be empty? Will it also include numbers, symbols, uppercase letters?
        M - Sliding window, two pointers
        P - We start at index 0 and keep track of a visited set to track characters that have already been visited. If the character hasn't been visited, we increment the right pointer. Otherwise, we update the length of the longest substring and move the left pointer until no repeating characters are left in the window.
        I - 
        initialize an empty visited set
        initialize the left pointer to be 0
        initialize res (length of longest substring) to be 0
        iterate through the string, keeping track of the right pointer
            if the character hasn't been visited
                add it to the visited set
            otherwise
                update res
                while the left pointer is less than the right pointer and the character at the left pointer is not equal to the character at the right pointer
                    remove the character at the left pointer from the visited set
                    increment the left pointer
                increment the left pointer to skip the character at the right index
        return res
        E - The time complexity is O(2N) with N being the number of characters in the string since in the worst case scenario, each character in the string will be visted twice. The space complexity would be O(N) due to the visited set.
        """
        
        """
        a b c b
        """
        
        if len(s) == 0: # edge case
            return 0
        
        visited = set()
        l = 0
        res = 1
        for r in range(len(s)):
            if s[r] not in visited:
                visited.add(s[r])
                res = max(res, r - l + 1)
            else:
                while l < r and s[l] != s[r]:
                    visited.remove(s[l])
                    l += 1
                l += 1
                   
        return res

def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Will all the strings contain just lowercase English characters? Can a string be empty?
        2. String - likely, Dictionary - likely
        3. If 2 words were angrams, they would be the same if sorted in alphabetical order. USe a dictionary to map each sorted string to the corresponding strings. At the end, return the values of the dictionary.
        4.
        initialize a dictionary
        loop through all the strings
            get the sorted string in alphabetical order
            add that pair (sorted string, original string) to the dictionary
        return the values of the dictionary
        5. See code below.
        """
        
        dic = defaultdict(list)
        for word in strs:
            sorted_word = ''.join(sorted(word))
            dic[sorted_word].append(word)
        return dic.values()

def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        """
        U - 
        given a head of a linked list, we want to partition it in a way that all nodes less than x come before and all nodes greater than or equal to come after
        we need to preserve the relative order of the nodes
        
        edge case: the number of nodes in the list is empty
        the node values and x and be positive or negative
        
        is x guaranteed to be in the list?
        M - linked list, two pointers
        P/I - 
        Example 1: head = [1,4,3,2,5,2], x = 3
        less than x: 1 -> 2 -> 2
        >= x: 4 -> 3 -> 5
        we join these 2 lists at the end, preserving the original order of the nodes
        
        we want to create 2 lists, the first one containing values less than x and the second one containing values greater than or equal to x
        
        Pseudocode:
        # create temporary heads to avoid edge cases
        set less to ListNode(0)
        set ref to less # we will return this pointer later
        set greater to ListNode(0)
        
        set curr to head # current pointer in the linked list
        while curr:
            if curr.val < x:
                append the node to less
                increment the less pointer
            otherwise
                append the node to greater
                increment the greater pointer
                
            increment the curr pointer
            
        set the next pointer of less to the next pointer of greater (less.next = greater.next)
        returrn ref.next # avoid returning the temporary head
        R - 
        E - 
        Time complexity: O(n) where n is the size of the list since we're iterating over the linked list once
        Space complexity: O(1)
        """
        
        """
        Example 1: 
        head = [1,4,3,2,5,2], x = 3
        less: 0 -> 1 -> 2 -> 2
        greater: 0 -> 4 -> 3 -> 5
        less_ref = 0
        greater_ref = 0
        curr = 2
        """
        
        # create temporary heads to avoid edge cases
        less, greater = ListNode(0), ListNode(0)
        less_ref = less # we will return this pointer later
        greater_ref = greater # use this reference to connec the 2 lists
        
        curr = head # current pointer in the linked list
        while curr:
            if curr.val < x:
                less.next = curr
                less = less.next
            else:
                greater.next = curr
                greater = greater.next
                
            curr = curr.next
            
        greater.next = None # avoid cycles
        less.next = greater_ref.next
        return less_ref.next