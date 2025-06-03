class Solution:
    # O(N K log K)
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        families = {}
        for s in strs: # O(N)
            family_id = "".join(sorted(s)) # O(K log K) to sort a string
            if family_id not in families: # O(1) hash lookup
                families[family_id] = []
            families[family_id].append(s)
        return list(families.values()) # O(N) data copy

"""
- a sorted string allows all anagrams to match
- use dictionary of the sorted string -> list of anagrams
- return the values of the dictionary as a list
- NOTE: needs "".join() to turn a list of char into a string, or just tuplify the list for hashing

"""