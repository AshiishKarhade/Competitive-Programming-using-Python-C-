#include <iostream>
using namespace std;

int main(){

  int a[10] = {1,2,3,4,5,6,7,8,9,10};

  for(int i=0; i<10;i++){
    for(int j=i; j<10; j++){
      for(int k=i; k<=j; k++){
        cout << a[k] << ",";
      }
    }
  }

  return 0;
}