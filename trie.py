class TrieNode:
    def __init__(self):
        self.children = {}
        self.value = None


class Trie:
    def __init__(self):
        self.root = TrieNode()
        self.size = 0

    def put(self, key: str, value=None):
        if not isinstance(key, str) or not key:
            raise TypeError(
                f"Illegal argument for put: key = {key} must be a non-empty string")
        node = self.root
        for ch in key:
            node = node.children.setdefault(ch, TrieNode())
        if node.value is None:
            self.size += 1
        node.value = value

    def get(self, key: str):
        if not isinstance(key, str) or not key:
            raise TypeError(
                f"Illegal argument for get: key = {key} must be a non-empty string")
        node = self.root
        for ch in key:
            node = node.children.get(ch)
            if node is None:
                return None
        return node.value

    def delete(self, key: str) -> bool:
        if not isinstance(key, str) or not key:
            raise TypeError(
                f"Illegal argument for delete: key = {key} must be a non-empty string")

        def _delete(node: TrieNode, depth: int) -> bool:
            if depth == len(key):
                if node.value is not None:
                    node.value = None
                    self.size -= 1
                    # if leaf, signal upward to delete this node
                    return len(node.children) == 0
                return False
            ch = key[depth]
            child = node.children.get(ch)
            if child is None:
                return False
            should_remove = _delete(child, depth + 1)
            if should_remove:
                del node.children[ch]
                return len(node.children) == 0 and node.value is None
            return False

        return _delete(self.root, 0)

    def is_empty(self) -> bool:
        return self.size == 0

    def longest_prefix_of(self, s: str) -> str:
        if not isinstance(s, str) or not s:
            raise TypeError(
                f"Illegal argument for longest_prefix_of: s = {s} must be a non-empty string")
        node = self.root
        longest = ""
        current = ""
        for ch in s:
            node = node.children.get(ch)
            if node is None:
                break
            current += ch
            if node.value is not None:
                longest = current
        return longest

    def _get_node(self, prefix: str):
        node = self.root
        for ch in prefix:
            node = node.children.get(ch)
            if node is None:
                return None
        return node

    def keys_with_prefix(self, prefix: str) -> list:
        if not isinstance(prefix, str):
            raise TypeError(
                f"Illegal argument for keys_with_prefix: prefix = {prefix} must be a string")
        node = self._get_node(prefix)
        if node is None:
            return []
        results = []
        self._collect(node, list(prefix), results)
        return results

    def _collect(self, node: TrieNode, path: list, results: list):
        if node.value is not None:
            results.append("".join(path))
        for ch, child in node.children.items():
            path.append(ch)
            self._collect(child, path, results)
            path.pop()

    def keys(self) -> list:
        results = []
        self._collect(self.root, [], results)
        return results


if __name__ == "__main__":
    # Пример использования
    trie = Trie()
    for word, idx in [("apple", 1), ("app", 2), ("banana", 3), ("bat", 4)]:
        trie.put(word, idx)

    print("All keys:", trie.keys())
    print("Keys with prefix 'ba':", trie.keys_with_prefix("ba"))
    print("Get 'app':", trie.get("app"))
    print("Longest prefix of 'application':",
          trie.longest_prefix_of("application"))
    print("Delete 'app':", trie.delete("app"),
          "— remaining keys:", trie.keys())
    print("Is empty?:", trie.is_empty())
