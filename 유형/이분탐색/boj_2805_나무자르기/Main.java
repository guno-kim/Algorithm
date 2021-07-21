package 유형.이분탐색.boj_2805_나무자르기;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Collections;
import java.util.StringTokenizer;
import java.util.*;

public class Main {
    static int n,m;
    static int[] trees;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        n=Integer.parseInt(st.nextToken());
        m=Integer.parseInt(st.nextToken());
        st=new StringTokenizer(br.readLine());
        trees=new int[n];

        int max=0;
        for (int i = 0; i < n; i++) {
            trees[i]=Integer.parseInt(st.nextToken());
            max=Math.max(max,trees[i]);
        }
        long l=0,r=max,mid=0,answer=0;
        while(true){
            mid=(l+r)/2;
            long nowValue=calc(mid);
            if(nowValue<m){
                r=mid-1;
            }
            else if(nowValue==m){
                answer=mid;
                break;
            }
            else{
                l=mid+1;
                answer=mid;
            }
            if(l>r)
                break;

        }
        System.out.println(answer);


    }

    static long calc(long v){
        long result=0;
        for (int tree : trees) {
            if(tree>v)
                result+=tree-v;
        }
        return result;
    }


}
