def int_to_string(num,base):
    convertString = "0123456789ABCDEF"
    if num < base:
        return convertString[num]
    else:
        return int_to_string(int(num/base),base)+convertString[(num%base)]

def reverse(string):
    string=list(string)
    if len(string)==0:
        return ""
    else:
        return string.pop() + reverse(string)

print(reverse("hello"))
print(reverse("l"))
print(reverse("follow"))
print(reverse(""))
#Base Case
#Reduction
#Calling itself
def find_palindrome(string):
    remove_dict={' ':'',',':'','.':'',';':'',"’":'',"'":'','-':'','–':''}
    string=''.join((remove_dict.get(ch,ch) for ch in string))
    string=string.lower()
    if len(string)==0:
        return True
    else:
        if string[0]==string[-1]:
            return find_palindrome(string[1:-1])
        else:
            return False


print(find_palindrome('Kanakanak'))
