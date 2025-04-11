class Solution {
public:
    bool strongPasswordCheckerII(string password) {
        if (password.length() < 8) return false; 

        bool hasLower = false, hasUpper = false, hasDigit = false, hasSpecial = false; 
        string hasChar = "!@#$%^&*()-+"; 

        for (int i = 0; i < password.length(); i++){
            if (i > 0 && password[i] == password[i - 1]) return false; 

            if (islower(password[i])) hasLower = true; 
            if (isupper(password[i])) hasUpper = true; 
            if (isdigit(password[i])) hasDigit = true;
            if(hasChar.find(password[i]) != string::npos) hasSpecial = true;  
        }
        return hasLower && hasUpper && hasDigit && hasSpecial; 
    }
};