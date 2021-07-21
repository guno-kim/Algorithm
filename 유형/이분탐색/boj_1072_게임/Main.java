package 유형.이분탐색.boj_1072_게임;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    static long x,y;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        x=Long.parseLong(st.nextToken());
        y=Long.parseLong(st.nextToken());
        long winrate=getWinrate(x, y);
        if(winrate<=98){
            long l=0,r=x,mid=0;
            while(true){
                mid=(l+r)/2;
                long changed=getWinrate(x+mid, y+mid);
                if(changed==winrate){
                    l=mid+1;
                }else{
                    r=mid;
                }
                if(l>=r)
                    break;

            }
            System.out.println(l);

        }
        else
            System.out.println(-1);

    }

    static long getWinrate(long x,long y){
        return y*100/x;
    }


}
