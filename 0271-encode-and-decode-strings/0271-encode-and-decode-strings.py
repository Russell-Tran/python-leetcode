class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        if not strs:
            return ""
        result = ""
        for s in strs:
            result += str(len(s))
            result += ","
            result += s
        return result


    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        if not s:
            return []
        result = []
        while s:
            delimit_idx = s.find(",")
            start_idx = delimit_idx + 1
            length = int(s[:delimit_idx])
            _, packet, remainder = s[:start_idx], s[start_idx:start_idx + length], s[start_idx + length:]
            
            result.append(packet)
            s = remainder
        return result


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

"""

ANKI
- This is a party trick
- You need a delimiter, but you can't use characters as the delimiter
- So instead this is an exercise in networking, where you should define packet lengths in between each word
- ALT 1: Not ASCII delimiter (easiest but has drawback, use a Unicode like pi)
- ALT 2: Escaping: use a 2-char delimiter but escape coincidences in the native string with an extra / 
(then you have to do the work of editing each string and also unwinding those but at least
it protects the thing, just like HTML)

NOTES
- Oh this is a good one i think i had an interview question as this
- also it's kind of just a party trick
- you need a delimiter, but you can't use characters as the delimiter
- so instead this is an exercise in networking, where you should define packet lengths in between each word
"""