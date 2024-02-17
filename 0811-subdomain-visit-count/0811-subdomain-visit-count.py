class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        count = {}

        for ele in cpdomains:
            rep, domain = ele.split(' ')
            rep = int(rep)

            if domain in count:
                count[domain] += rep
            else:
                count[domain] = rep
            
            i = 0
            while i < len(domain):
                if domain[i] == '.':
                    subdomain = domain[i+1: ]
                    if subdomain in count:
                        count[subdomain] += rep
                    else:
                        count[subdomain] = rep
                i+=1
            
        res = [f'{count[ele]} {ele}' for ele in count]

        return res
            
