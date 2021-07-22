package 유형.정수론.boj_14476_최대공약수하나빼기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb = new StringBuilder();
        int n=Integer.parseInt(br.readLine());
        int[] nums=new int[n];
        int[] forward=new int[n];
        int[] backward=new int[n];

        StringTokenizer st=new StringTokenizer(br.readLine());
        for (int i = 0; i < n; i++) {
            nums[i]=Integer.parseInt(st.nextToken());
        }
        forward[0]=nums[0];
        for (int i = 1; i < n; i++) {
            if(forward[i-1]>nums[i])
                forward[i]=gcd(forward[i-1],nums[i]);
            else
                forward[i]=gcd(nums[i],forward[i-1]);
        }
        backward[n-1]=nums[n-1];
        for (int i = n-2; i >=0; i--) {
            if(backward[i+1]>nums[i])
                backward[i]=gcd(backward[i+1],nums[i]);
            else
                backward[i]=gcd(nums[i],backward[i+1]);
        }

        int max=-1,answerNum=0;

        for (int i = 0; i < n; i++) {
            int nowGcd,nowNum=nums[i];
            if(i==0)
                nowGcd=gcd(backward[1],0);
            else if(i==n-1)
                nowGcd=gcd(forward[n-2],0);
            else{
                nowGcd=gcd(forward[i-1],backward[i+1]);
            }
            if(nowNum%nowGcd!=0 && max<nowGcd){
                max=nowGcd;
                answerNum=nowNum;
            }
        }
        if(max==-1)
            System.out.println(max);
        else
            System.out.println(max+" "+answerNum);

    }

    static int gcd(int a,int b){
        if(b==0)
            return a;
        else
            return gcd(b,a%b);
    }

}
