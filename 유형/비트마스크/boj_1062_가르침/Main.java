package 유형.비트마스크.boj_1062_가르침;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.StringTokenizer;
import java.io.IOException;

public class Main {
    public static boolean[][] words;
    public static boolean[] learned=new boolean[26];
    public static List<Integer> base=new ArrayList<Integer>(Arrays.asList(0,2,8,13,19));
    public static int k;
    public static int answer=0;
    public static void comb(int s,int cnt){
        if(cnt==k-5){
            count();
            return;
        }
        
        for (int i = s+1; i < 26; i++) {
            if(base.contains(i)){
                continue;
            }
            learned[i]=true;
            comb(i,cnt+1);
            learned[i]=false;
            
        }
    }
    public static void count(){
        int cnt=0;
        for (boolean[] word : words) {
            boolean flag=true;
            for (int i = 0; i < 26; i++) {
                if(word[i]&&!learned[i]){
                    flag=false;
                    break;
                }
            }
            if(flag)
                cnt++;
        }
        answer=Math.max(answer, cnt);
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken());
        k=Integer.parseInt(st.nextToken());
        words=new boolean[n][26];

        for(int i:base)
            learned[i]=true;

        for (int i = 0; i < n; i++) {
            String s=br.readLine();
            for (int j = 0; j < s.length(); j++) {
                int a=(int)s.charAt(j);
                words[i][a-97]=true;
            }
        }
        comb(0, 0);
        System.out.println(answer);
            
    }
}