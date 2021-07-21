package 유형.투포인터.boj_1806_부분합;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken()),m=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        int[] arr=new int[n];
        for (int i = 0; i < n; i++) {
            arr[i]=Integer.parseInt(st.nextToken());
        }
        int l=0,r=0,sum=arr[0],answer=Integer.MAX_VALUE;
        while(true){
            
            if(sum<m){
                r++;
                if(r==n)
                    break;
                sum+=arr[r];
            }
            else if(sum>=m){
                answer=Math.min(answer, r-l+1);
                sum-=arr[l++];
            }
        }
        System.out.println(answer!=Integer.MAX_VALUE?answer:0);
    }
}
