#include <bits/stdc++.h>
using namespace std;
int main()
{
	for(int x=0; x<=20; x++)
	{
		for(int y=0; y<34; y++)
		{
			int z=100-x-y; // 减少z的枚举数，使用消元法 
			if(x+y+z==100&&5*x+3*y+z/3==100&&z%3==0)
			{
				cout<<"x="<<x<<endl<<"y="<<y<<endl<<"z="<<z<<endl<<endl;
			}
		}
	}


	return 0;
}

