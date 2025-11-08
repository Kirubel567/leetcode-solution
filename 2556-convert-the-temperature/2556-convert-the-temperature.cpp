class Solution {
public:
    vector<double> convertTemperature(double celsius) {
        double Kelvin = celsius + 273.15; 
        double Fahrenheit = celsius * 1.80 + 32.00; 
        vector<double> ans = {Kelvin, Fahrenheit};
        // double ans[2] = {Kelvin, Fahrenheit};
        
        return ans; 

        
    }
};