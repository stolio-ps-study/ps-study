import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        
        int N = Integer.parseInt(br.readLine());
        List<Integer> cranes = new ArrayList<>();
        
        // 크레인 입력 받기
        StringTokenizer st = new StringTokenizer(br.readLine());
        for(int i=0; i<N; i++){
            cranes.add(Integer.parseInt(st.nextToken()));
        }
        
        int M = Integer.parseInt(br.readLine());
        List<Integer> boxes = new ArrayList<>();
        
        // 박스 입력 받기
        st = new StringTokenizer(br.readLine());
        for(int i=0; i<M; i++){
            boxes.add(Integer.parseInt(st.nextToken()));    
        }

        Collections.sort(cranes, Collections.reverseOrder());
        Collections.sort(boxes, Collections.reverseOrder());

        // 가장 무거운 걸 드는 크레인보다 더 큰 박스가 있으면 -1 
        if(boxes.get(0) > cranes.get(0)){
            System.out.println(-1);
            return ;
        }

        int cnt = 0;
        while(!boxes.isEmpty()){
            // 크레인 찾기
            int craneIdx = 0; // 박스 인덱스 시작 부분)
            int boxIdx = 0;
            while(craneIdx < N){
                if(boxIdx >= boxes.size()) break;
                
                if(cranes.get(craneIdx) >= boxes.get(boxIdx)){
                    boxes.remove(boxIdx);
                    craneIdx++;
                }
                else{
                    boxIdx++;
                }
            }
            cnt++;
        }
        System.out.println(cnt);
    }
}