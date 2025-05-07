from trie import Trie


class LongestCommonWord(Trie):

    def find_longest_common_word(self, strings) -> str:
        if not isinstance(strings, list) or not strings:
            raise TypeError(
                f"Illegal argument for longestPrefixOf: s = {strings} must be a non-empty list")

        for i, string in enumerate(strings):
            if not isinstance(string, str) or not string:
                raise TypeError(
                    f"Illegal argument for longestPrefixOf: s = {string} must be a non-empty string")

            self.put(string, i)

        # Пошук спільного префіксу між усіма словами у trie
        prefix = ""
        current = self.root

        while len(current.children) == 1 and current.value is None:
            char = next(iter(current.children))
            prefix += char
            current = current.children[char]

        return prefix


if __name__ == "__main__":
    # Тести
    trie = LongestCommonWord()
    strings = ["flower", "flow", "flight"]
    assert trie.find_longest_common_word(strings) == "fl"

    trie = LongestCommonWord()
    strings = ["interspecies", "interstellar", "interstate"]
    assert trie.find_longest_common_word(strings) == "inters"

    trie = LongestCommonWord()
    strings = ["dog", "racecar", "car"]
    assert trie.find_longest_common_word(strings) == ""
