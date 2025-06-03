class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        families = {}
        for s in strs:
            family_id = "".join(sorted(s))
            if family_id not in families:
                families[family_id] = []
            families[family_id].append(s)
        return list(families.values())

"""
- a sorted string allows all anagrams to match
- use dictionary of the sorted string -> list of anagrams
- return the values of the dictionary as a list


"""