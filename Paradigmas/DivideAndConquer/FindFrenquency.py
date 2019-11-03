"""
#include <iostream>
#include <unordered_map>
using namespace std;

// Function to find frequency of each element in a sorted array
void findFrequency(int arr[], int n, unordered_map<int, int> &count)
{
	// if every element in the subarray arr[0..n-1] is equal,
	// then increment the element count by n
	if (arr[0] == arr[n - 1])
	{
		count[arr[0]] += n;
		return;
	}

	// divide array into left and right sub-array and recur
	findFrequency(arr, n/2, count);
	findFrequency(arr + n/2, n - n/2, count);
}

// Find Frequency of each element in a sorted array containing duplicates
int main()
{
	int arr[] = { 2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9 };
	int n = sizeof(arr) / sizeof(int);

	// find frequency of each element of the array and store it in map
	unordered_map<int, int> map;
	findFrequency(arr, n, map);

	// print the frequency
	for (auto &p: map) {
		cout << p.first << " occurs " << p.second << " times\n";
	}

	return 0;
}
"""

def findFrequency(arr, n, count):
    print(arr, n)
    if arr[0] == arr[n-1]:
        print("dd", arr[0], arr[n-1])
        print("igual",arr)
        count[arr[0]] = count[arr[0]] +  n
        #print(count)
        return  count
    else:
        findFrequency(arr[:int(n/2)], int(n/2), count)
        findFrequency(arr[int(n/2):], int(n/2), count)

arr = [ 2, 2, 2, 4, 4, 4, 5, 5, 6, 8, 8, 9 ]
count = [0,0,0,0,0,0,0,0,0,0,0,0]
print(findFrequency(arr, int(len(arr)), count))