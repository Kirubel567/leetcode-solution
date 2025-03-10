class Solution {
public:
    bool isVowel(char inputChar)
    {
        if(inputChar == 'a' || inputChar == 'e' || inputChar == 'i' || inputChar =='o' || inputChar == 'u' || inputChar == 'A' || inputChar == 'E' || inputChar == 'I' || inputChar == 'O' || inputChar == 'U')
        {
            return true;
        }
        return false;
    }
    
    string reverseVowels(string s) 
    {
        int leftPointer = 0;
        int rightPointer = s.size() - 1;
        while(leftPointer < rightPointer)
        {
            while(leftPointer < rightPointer && !isVowel(s[leftPointer]))
            {
                leftPointer++;
            }

            while(leftPointer < rightPointer && !isVowel(s[rightPointer]))
            {
                rightPointer--;
            }
            char temp = s[leftPointer];
            s[leftPointer] = s[rightPointer];
            s[rightPointer] = temp;
            leftPointer++;
            rightPointer--;
        }    
        return s;
    }
};