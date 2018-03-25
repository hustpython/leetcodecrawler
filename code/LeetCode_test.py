# -*- coding:utf-8 -*-
'''
Created on  
2017年6月27日   下午8:21:08
@author: yzw
'''
a =u'class Solution:\u000D\u000A    def twoSum(self, nums, target):\u000D\u000A        \u0022\u0022\u0022\u000D\u000A        :type nums: List[int]\u000D\u000A        :type target: int\u000D\u000A        :rtype: List[int]\u000D\u000A        \u0022\u0022\u0022\u000D\u000A        '
c =a.encode("UTF-8")  
'''with open('test.txt','w') as f:
    f.write(c)
f.close()'''
#print(c)
a ='()1'
a =a.replace('(', '')
a =a.replace(')', '')
#print(a)
a = [2,4,8,3,2,3,1,8]
a = reversed(a)
for x in a:
    print(x)
a ='Powx,-n'
if ',' in a:
    print('dd')
    
a = ('r`q')
def main():
    """ """
for atrr in [0,1,4,5,7]:
    print "attribute %d ------------------------------" % atrr
    for fore in [30,31,32,33,34,35,36,37]:
        for back in [40,41,42,43,44,45,46,47]:
            color = "\x1B[%d;%d;%dm" % (atrr,fore,back)
            print "%s %d-%d-%d\x1B[0m" % (color,atrr,fore,back),
        print ""
if __name__ == "__main__":
    """ """
    main()
a = [1,0,3]
a.pop(0)
print(a)