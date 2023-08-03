#!/usr/bin/python3
"""
lockboxes
"""


def canUnlockAll(boxes):
    """
    lockboxes
    """
    visited = set()

    def dfs(boxNumber):
        """
        lockboxes
        """
        visited.append(boxNumber)
        for key in boxes[boxNumber]:
            if key not in visited:
                dfs(key)

    dfs(0)
    return len(boxes) == len(visited)
