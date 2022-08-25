class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        en = 0 # Energy
        ex = 0 # Experience
        an = 0 # Added energy
        ax = 0 # Added experience
        for ener, exp in zip(energy, experience):
            if ener >= en:
                an += (ener - en + 1)
                en += (ener - en + 1)
            if exp >= ex:
                ax += (exp - ex + 1)
                ex += (exp - ex + 1)
            en -= ener
            ex += exp
        return max(0, (an - initialEnergy)) + max(0, (ax - initialExperience))
        
        
        # energy_need = sum(energy) + 1 - initialEnergy
        # experience_need = 0
        # sum_so_far = 0
        # for i in range(len(experience)):
        #     if experience_need > experience[i]:
        #         sum_so_far += experience[i]
        #         continue
        #     experience_need = max(experience_need, experience[i] + 1 - sum_so_far)
        #     sum_so_far += experience[i]
        # experience_need -= initialExperience
        # print(energy_need)
        # print(experience_need)
        # need = max(0, energy_need) + max(0, experience_need, experience[0] + 1 - initialExperience)
        # return need