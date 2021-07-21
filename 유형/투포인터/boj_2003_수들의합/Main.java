package 유형.투포인터.boj_2003_수들의합;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Stack;
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
        int l=0,r=0,sum=arr[0],cnt=0;
        while(true){
            if(sum<m){
                if(r<n-1){
                    r++;
                    sum+=arr[r];
                }
                else break;
            }
            else if(sum==m){
                cnt++;
                if(r<n-1){
                    r++;
                    sum+=arr[r];
                }
                else break;
            }
            else if(sum>m){
                if(l<n-1){
                    sum-=arr[l];
                    l++;
                }
                else break;
            }
        }
        System.out.println(cnt);
    }
}
