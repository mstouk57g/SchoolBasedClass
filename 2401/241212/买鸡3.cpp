#include <bits/stdc++.h>
using namespace std;
int main()
{
	for(int n=0; n<=3; n++)
	{
		// 换元法减少枚举数 
		int x=4*n; // 4*n==100
		int y=25-7*n; 
		int z=75+3*n; // z=100-x-y
		cout<<"x="<<x<<endl<<"y="<<y<<endl<<"z="<<z<<endl<<endl;
	}


	return 0;
}

