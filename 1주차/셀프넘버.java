import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException{
        boolean[] arr = new boolean[10000];

        int m;
        for(int a=1; a<10; a++){
            m = 2*a;
            if(m >= 10){
                break;
            }
            arr[m] = true;
        }

        for(int a=0; a<10; a++){
            for(int b=0; b<10; b++){
                m = 11*a + 2*b;
                
                if(m >= 100){
                    break;
                }
                if(m >= 10){
                    arr[m] = true;
                }
            }
        }

        for(int a=0; a<10; a++){
            for(int b=0; b<10; b++){
                for(int c=0; c<10; c++){
                    m = 101*a + 11*b + 2*c;
                    if(m >= 1000){
                        break;
                    }
                    if(m >= 100){
                        arr[m] = true;
                    }
                }
            }
        }

        for(int a=0; a<10; a++){
            for(int b=0; b<10; b++){
                for(int c=0; c<10; c++){
                    for(int d=0; d<10; d++){
                        m = 1001*a + 101*b + 11*c + 2*d;
                        if(m >= 10000){
                            break;
                        }
                        if(m >= 1000){
                            arr[m] = true;
                        }
                    }
                }
            }
        }
        StringBuilder sb = new StringBuilder();
        for(int i=1; i<10000; i++){
            if(!arr[i]) sb.append(Integer.toString(i)).append("\n");
        }
        System.out.println(sb);
    }
}
/*
    문제 요구 : 10,000 보다 작은 셀프 넘버를 찾아라

    셀프 넘버란? : 생성자가 없는 숫자

    생성자란? : d(n) = m 이라고 할 때, m의 생성자는 n이다.

    즉 d(n)을 통해 만들 수 없는 10,000 보다 작은 숫자를 찾아라..  

    자릿수 기준으로 계산
 
    1자리(a): m = 2a 
    2자리(ab): m = 11a + 2b 
    3자리(abc): m = 101a + 11b + 2c
    4자리(abcd): m = 1001a + 101b + 11c + 2d

*/
