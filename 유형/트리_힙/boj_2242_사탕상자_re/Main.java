package 유형.트리_힙.boj_2242_사탕상자_re;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int S =1;
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        while (S <1000000) S *=2;
        IndexTree indexTree=new IndexTree();
        int n=Integer.parseInt(br.readLine());
        StringBuilder sb=new StringBuilder();
        StringTokenizer st;
        while (n-->0){
            st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken());
            if(a==2){
                int b=Integer.parseInt(st.nextToken()),c=Integer.parseInt(st.nextToken());
                indexTree.update(b,c);
            }
            else{
                int b=Integer.parseInt(st.nextToken());
                int result=indexTree.query(1,S,1,b);
                indexTree.update(result,-1);
                sb.append(result).append("\n");
            }
        }
        System.out.println(sb);

    }

    static class IndexTree{
        int[] tree;
        IndexTree(){
            tree=new int[S *2];
        }
        void update(int i,int diff){
            i+= S -1;
            while (i!=0){
                tree[i]+=diff;
                i/=2;
            }
        }
        int query(int left,int right,int node,int value){
            if(left==right)
                return node-S+1;
            int mid=(left+right)/2;

            if(value<=tree[node*2])
                return query(left,mid,node*2,value);
            else
                return query(mid+1,right,node*2+1,value-tree[node*2]);
        }

    }
}
