#include<iostream>

using namespace std;

char a[3][3];

bool win(char c){
	for(int i=0;i<3;i++){
		if(a[i][0] == c && a[i][1] == c && a[i][2] == c)
			return true;
		if(a[0][i] == c && a[1][i] == c && a[2][i] == c)
			return true;
	}
	
	if(a[0][0] == c && a[1][1] == c && a[2][2] == c)
		return true;
	if(a[0][2] == c && a[1][1] == c && a[2][0] == c)
		return true;
	
	return false;
}


int main(){
	int xct = 0, oct=0;
 
 
    for (int i = 0; i < 3; i++)
        for (int j = 0; j < 3; j++) {
        	cin>>a[i][j];
            xct += a[i][j] == 'X';
            oct += a[i][j] == '0';
        }
 
    if (xct<oct or xct-oct>1 or (win('X')&&xct-oct!=1) or (win('0') && xct!=oct)) {
        printf("illegal");
    }
 
    else if (win('X'))
        printf("the first player won");
 
    else if (win('0'))
        printf("the second player won");
 
    else if (xct + oct == 9)
        printf("draw");
 
    else if (xct == oct)
        printf("first");
 
    else
        printf("second");
       
 
    return 0;
}

