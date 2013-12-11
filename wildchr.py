def match(str1,str2):
    print '_'
    if str1=='*' and str2=='' :
        return True
    if str1=='' and str2=='' :
        return True
    
    if str1=='' or str2=='' :
        return False
    if str1[0] ==str2[0] :
        return match(str1[1:],str2[1:])
    if str1[0]=='*' and str2[0] != '':
        return match(str1[1:],str2) or match(str1,str2[1:])
    if str1[0]=='?' and str2[0] !=''  :
        return match(str1[1:],str2[1:])
    
    return False
print match("ge*ek*s*s*a","geeksfassa")

