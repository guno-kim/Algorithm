package 유형.투포인터.re_boj_2143_두배열의합;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;
import java.util.*;

public class Main {
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        int T=Integer.parseInt(br.readLine());
        StringTokenizer st;
        int n=Integer.parseInt(br.readLine());
        st=new StringTokenizer(br.readLine());
        int[] a=new int[n];
        for (int i = 0; i < n; i++) {
            a[i]=Integer.parseInt(st.nextToken()) ;
        }
        
        int m=Integer.parseInt(br.readLine());
        st=new StringTokenizer(br.readLine());
        int[] b=new int[m];
        for (int i = 0; i < m; i++) {
            b[i]=Integer.parseInt(st.nextToken()) ;
        }

        List<Long> suba=new ArrayList<>();
        List<Long> subb=new ArrayList<>();

        for (int i = 0; i < n; i++) {
            long sum=0;
            for (int j = i; j < n; j++) {
                sum+=a[j];
                suba.add(sum);
            }
        }
        for (int i = 0; i < m; i++) {
            long sum=0;
            for (int j = i; j < m; j++) {
                sum+=b[j];
                subb.add(sum);
            }
        }
        Collections.sort(suba);
        Collections.sort(subb,Collections.reverseOrder());
        long cnt=0;
        int al=0,bl=0;

        while(al<suba.size()&&bl<subb.size()){
            long nowA=suba.get(al),nowB=subb.get(bl);
            long sum=nowA+nowB;
            if(sum==T){
                long cntA=0,cntB=0;//long 으로해야 오류안남
                while(al<suba.size() && suba.get(al)==nowA){
                    al++;
                    cntA++;
                }
                while(bl<subb.size() && subb.get(bl)==nowB){
                    bl++;
                    cntB++;
                }
                cnt+=cntA*cntB;
            }else if(sum<T){
                al++;
            }else if(sum>T){
                bl++;
            }

        }
        System.out.println(cnt);
    }
}
