class Solution {
private:
int getPivot(vector<int>arr,int s,int e)
{
    int mid=s+(e-s)/2;
    while(s<e)
    {
        if(arr[mid]>=arr[0])
        {
            s=mid+1;
        }
        else
        {
            e=mid;
        }
        mid=s+(e-s)/2;
    }
return e; 
}

int binarySearch(vector<int>arr,int s,int e, int key)
{
    int mid=s+(e-s)/2;
    while(s<=e)
{
    if(key<arr[mid])
{
    e=mid-1;
}
if(key>arr[mid])
{
    s=mid+1;
}
if(arr[mid]==key)
{
    return mid;
}
mid=s+(e-s)/2;
}
return -1;
}

public:
    int search(vector<int>& nums, int target) {
        int pivot=getPivot(nums,0,nums.size()-1);

        if(target>=nums[pivot] && target<=nums[nums.size()-1])
        {
            return binarySearch(nums,pivot,nums.size()-1,target);
        }
        else
        {
            return binarySearch(nums,0,pivot-1,target);
        }

    }
};