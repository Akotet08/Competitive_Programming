class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        val = 0
        for opr in operations:
            if '--' in opr:
                val -= 1
            if '++' in opr:
                val += 1
        
        return val
        