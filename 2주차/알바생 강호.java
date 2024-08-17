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
