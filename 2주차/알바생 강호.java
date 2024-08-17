import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int N = Integer.parseInt(br.readLine());

        List<Integer> tips = new ArrayList<>();
        for(int i=0; i<N; i++){
            tips.add(Integer.parseInt(br.readLine()));
        }
        
        Collections.sort(tips,Collections.reverseOrder());
        
        long result = 0L;
        int tip;
        for(int i=0; i<N ; i++){
            tip = tips.get(i) - i;
            if (tip <= 0) break;
            result += tip;
        }
        System.out.println(result);
    }
}
/*
    8시 까지 줄 세우기 -> 8시 되는 순간 커피 하나씩 받고 자리로 가기

    몇 번째로 커피 받는 지에 따라 다른 액수의 팁을 준다.

    tip = 원래 주려고 생각했던 돈 - (받은 등수 -1) if( tip<0 ) 돈 받을 수 없음

    손님의 순서를 바꿨을 때 받을 수 있는 tip의 최대 값을 구해라

*/