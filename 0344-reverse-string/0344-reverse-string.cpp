class Solution {
public:
    void reverseString(vector<char>& st) {

        int s=0;
        int e=st.size()-1;
        while(s<e)
        {
            swap(st[s++],st[e--]);
        }
        
    }
};