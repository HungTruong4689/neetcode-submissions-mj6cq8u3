class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        def convertMail(mail):
            s = ""
            atIndex = mail.find("@")
            local = mail[:atIndex]
            domain = mail[atIndex:]
            plusIndex = local.find('+')
            print(plusIndex)
            if plusIndex != -1:
                local = local[:plusIndex]
            
            tLocal = ""
            for i in local:
                if i == ".":
                    continue
                else:
                    tLocal += i
            return tLocal + domain
        dic = {}
        for mail in emails:
            key = convertMail(mail)
            if key in dic:
                dic[key] +=1
            else:
                dic[key] = 1
        return len(dic)