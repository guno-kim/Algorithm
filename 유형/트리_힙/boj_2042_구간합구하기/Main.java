package 유형.트리_힙.boj_2042_구간합구하기;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class Main {
    static int N;
    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());

        int n =Integer.parseInt(st.nextToken()), m=Integer.parseInt(st.nextToken()),k=Integer.parseInt(st.nextToken());
        N=1;
        while (N<n){
            N*=2;
        }
        long[] nums=new long[N];
        for (int i = 0; i < n; i++) {
            nums[i]=Long.parseLong(br.readLine());
        }

        IndexTree indexTree=new IndexTree();
        indexTree.init(nums);
        while (m+k-->0){
            st=new StringTokenizer(br.readLine());
            int a=Integer.parseInt(st.nextToken()),b=Integer.parseInt(st.nextToken());
            long c=Long.parseLong(st.nextToken());
            if(a==2) {
                System.out.println(indexTree.query(1, N,1,b,Math.toIntExact(c) ));
            }
            else {
                indexTree.update(1, N,1,b,c-indexTree.tree[(int) (b+ N -1)]);
            }
        }
    }

    static class IndexTree{
        long[] tree;
        void init(long[] nums){
            tree=new long[2* N];
            if (N >= 0) System.arraycopy(nums, 0, tree, N + 0, N);
            for (int i = N -1; i >=1; i--) {
                tree[i]=tree[i*2]+tree[i*2+1];
            }
        }
        long query(int left,int right,int node, int queryleft,int queryright){
            if(queryright<left||right<queryleft)
                return 0;
            else if(queryleft<=left&&right<=queryright)
                return tree[node];
            else{
                int mid=(left+right)/2;
                long sum=0;
                sum+=query(left,mid,node*2,queryleft,queryright);
                sum+=query(mid+1,right,node*2+1,queryleft,queryright);
                return sum;
            }
        }

        void update(int left,int right,int node, int target,long diff) {
            tree[node]+=diff;
            if(target==node-N+1){
                return;
            }
            int mid=(left+right)/2;
            if(target<=mid)
                update(left,mid,node*2,target,diff);
            else
                update(mid+1,right,node*2+1,target,diff);


        }

    }
}
