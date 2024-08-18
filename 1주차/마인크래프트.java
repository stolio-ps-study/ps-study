import java.io.BufferedReader;
import java.util.StringTokenizer;
import java.io.IOException;
import java.io.InputStreamReader;

// The main method must be in a class named "Main".
class 마인크래프트 {
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st = new StringTokenizer(br.readLine());
        
        int N = Integer.parseInt(st.nextToken());
        int M = Integer.parseInt(st.nextToken());
        int B = Integer.parseInt(st.nextToken());

        // 배열 입력 받기
        int[][] arr = new int[N][M];
        
        int min = 256;
        int max = 0;
        for(int i=0; i<N; i++){
            st = new StringTokenizer(br.readLine());
            for(int j=0; j<M; j++){
                arr[i][j] = Integer.parseInt(st.nextToken());
                if (max < arr[i][j]) max = arr[i][j];
                if (min > arr[i][j]) min = arr[i][j];
            }
        }

        // min부터 max까지 완전 탐색
        int answerTime = Integer.MAX_VALUE;
        int answerHeight = 0;
        for(int height=min; height<=max; height++){
            int block = B;
            int enough = 0;
            int lack = 0;
            // height로 땅고르기
            for(int i=0; i<N; i++){
                for(int j=0; j<M; j++){
                    // height 보다 높은 경우: 삭제(2초) -> 현재 가진 블록 수에 남은 높이만큼 추가
                    if(arr[i][j] > height){
                        enough += (arr[i][j] - height);
                    }
                    // height 보다 낮은 경우: 추가(1초) -> 현재 가진 블록 수에서 사용 블럭만큼 차감
                    if(arr[i][j] < height){
                        lack += (height - arr[i][j]);
                    }
                }
            }
            block += enough;
            // 남은 block이 부족한 block 보다 크거나 같은 경우만 해당 높이의 땅을 만들 수 있음
            if(block >= lack){
                if( answerTime >= 2*enough + lack){
                    answerTime = 2*enough + lack;
                    answerHeight = height;
                }
            }
        }
        System.out.println(answerTime +" " + answerHeight);
    }
    
}