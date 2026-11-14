class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        res = len(students)
        stu = Counter(students) #adds occurances of students into hashmap

        #for s in students:
        #   if s not in stu:
        #      stu[s] = 0
        # else:
        #    stu[s] += 1

        for f in sandwiches:
            if stu[f] > 0:
                stu[f] -= 1
                res -= 1
            else: 
                return res

        return res
        
        

         
        