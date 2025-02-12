class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        count = -1
        for i in operations:
            if i == \C\:
                record.pop()
                count -= 1
            elif i ==\D\:
                temp = record[count]
                record.append(2*temp)
                count +=1
            elif i == \+\:
                record.append(record[count] + record[count-1])
                count +=1
            else:
                record.append(int(i))
                count +=1
        return sum(record)

            
        