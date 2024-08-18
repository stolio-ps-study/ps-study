import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;

// The main method must be in a class named "Main".
class Main {
    
    // 상하좌우
    static int N;
    static int max =1;
    static char[][] graph;
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        graph = new char[N][N];
        
        for(int i=0; i<N; i++){
            String s = br.readLine();
            for(int j=0; j<N; j++){
                graph[i][j] = s.charAt(j);
            }
        }

        // 오른쪽과 교체
        for(int i=0; i<N; i++){
            for(int j=0; j<N-1; j++){
                swap(i, j, i, j+1);
                row_search();
                col_search();
                swap(i, j+1, i, j); 
            }
        }
        // 아래쪽과 교체
        for(int i=0; i<N; i++){
            for(int j=0; j<N-1; j++){
                swap(j, i, j+1, i);
                row_search();
                col_search();
                swap(j+1, i, j, i); 
            }
        }
        System.out.println(max);
        br.close();
    }
    
    static void swap(int y, int x, int target_y, int target_x){
        char temp = graph[y][x];
        graph[y][x] = graph[target_y][target_x];
        graph[target_y][target_x] = temp;
    }
    
    static void row_search(){
        for(int i=0; i<N; i++){
            int cnt = 1;
            for(int j=0; j<N-1; j++){
                // 색깔이 같으면 cnt + 1 
                if(graph[i][j] == graph[i][j+1]){
                    cnt += 1;
                    max = Math.max(max, cnt);
                }
                // 색깔이 다르면 cnt 초기화
                else{
                    cnt = 1;
                }
            }
        }    
    }
    static void col_search(){
        for(int i=0; i<N; i++){
            int cnt = 1;
            for(int j=0; j<N-1; j++){
                // 색깔이 같으면 cnt + 1 
                if(graph[j][i] == graph[j+1][i]){
                    cnt += 1;
                    max = Math.max(max, cnt);
                }
                // 색깔이 다르면 cnt 초기화
                else{
                    cnt = 1;
                }
            }
        }
    }
}