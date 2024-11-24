#include <bits/stdc++.h>
using namespace std;
int main()
{
	int n,x,y,min;
	cin>>n;
	cin>>x;
	min = x;
	
	for(int i=1;i<n;i++)
	{
		cin>>y;
		if(y<min)
			min=y;
	}
	cout<<min;

	return 0;
}

