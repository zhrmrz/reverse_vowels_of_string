class Sol:
    def reverse_vowels_of_string(self,string):
        vowels=['a','e','i','o','u']
        str=[]
        s=''
        left=0
        right=len(string)-1
        for char in string:
            str.append(char)
        for i in range(len(string)//2):
            if str[left] in vowels and str[right] in vowels:
                str[left],str[right]=str[right],str[left]
            elif str[left] in vowels and  str[right] not in vowels:
                right-=1
            elif str[left] not in vowels and str[right] in vowels:
                left+=1
            elif str[left] not in vowels and str[right] not in vowels:
                right-=1
                left += 1
        for i in str:
            s+=i
        return s


if __name__ == '__main__':
    p1=Sol()
    print(p1.reverse_vowels_of_string('hello'))
