class Solution {
public:

int firstOccurence(vector<int>&arr,int key)
{
    int s=0;
    int e=arr.size()-1;
    int mid=s+(e-s)/2;
    int ans=-1; 
    while(s<=e)
    {
        if(arr[mid]==key)
        {
            ans=mid;
            e=mid-1;
        }
        if(key<arr[mid])
        {
            e=mid-1;
        }
        if(key>arr[mid])
        {
            s=mid+1;
        }
        mid=s+(e-s)/2;
    }
    return ans;
}


int lastOccurence(vector<int>&arr,int key)
{
    int s=0;
    int e=arr.size()-1;
    int mid=s+(e-s)/2;
    int ans=-1; 
    while(s<=e)
    {
        if(arr[mid]==key)
        {
            ans=mid;
            s=mid+1;
        }
        if(key<arr[mid])
        {
            e=mid-1;
        }
        if(key>arr[mid])
        {
            s=mid+1;
        }
        mid=s+(e-s)/2;
    }
    return ans;
}

    vector<int> searchRange(vector<int>& nums, int target) {
        vector<int>answer;
        answer.push_back(firstOccurence(nums,target));
        answer.push_back(lastOccurence(nums,target));
        return answer;
    }
};