import java.util.*;
import java.lang.*;
import java.io.*;

// The main method must be in a class named "Main".
class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());

        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());

        Map<String, Integer> wordsMap = new HashMap<>();
        
        for(int i=0; i<N; i++){
            String word = br.readLine();
            if(word.length() >= M){
                if (wordsMap.containsKey(word)){
                    wordsMap.put(word, wordsMap.get(word) + 1);
                }
                else{
                    wordsMap.put(word, 1);
                }
            }
        }

        PriorityQueue<String> pq = new PriorityQueue<>((o1, o2) ->{
            // 자주 나오는 단어일수록 앞에 배치
            if(wordsMap.get(o1) != wordsMap.get(o2)){
                return wordsMap.get(o2) - wordsMap.get(o1);
            }
            else{
                if(o1.length() != o2.length()){
                    return o2.length() - o1.length();
                }
                else{
                    return o1.compareTo(o2);
                }
            }
        });

        for(String key: wordsMap.keySet()){
            pq.offer(key);
        }
        
        StringBuilder sb = new StringBuilder();
        
        while(!pq.isEmpty()){
            sb.append(pq.poll()).append("\n");
        }

        System.out.println(sb);
        br.close();
    }
}