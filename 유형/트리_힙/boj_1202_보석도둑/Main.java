package 유형.트리_힙.boj_1202_보석도둑;

import java.io.*;
import java.util.Arrays;
import java.util.Comparator;
import java.util.PriorityQueue;
import java.util.StringTokenizer;

public class Main {

    static class Jewelry{
        public int w;
        public int v;
        Jewelry(int w,int v){
            this.w=w;
            this.v=v;
        }
    }

    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int n=Integer.parseInt(st.nextToken()),k=Integer.parseInt(st.nextToken());

        Jewelry[] jewelries=new Jewelry[n];
        for (int i = 0; i < n; i++) {
            st=new StringTokenizer(br.readLine());
            jewelries[i]=new Jewelry(Integer.parseInt(st.nextToken()), Integer.parseInt(st.nextToken()));
        }
        Arrays.sort(jewelries,Comparator.comparingInt(o -> o.w));
        PriorityQueue<Jewelry> pq=new PriorityQueue<>(Comparator.comparingInt(o -> -o.v));

        int[] bags=new int[k];
        for (int i = 0; i < bags.length; i++) {
            bags[i]=Integer.parseInt(br.readLine());
        }
        Arrays.sort(bags);

        Long answer=0L;
        int j=0;
        for (int bag : bags) {
            while (j < n && jewelries[j].w <= bag) {
                pq.add(jewelries[j]);
                j++;
            }
            if (!pq.isEmpty())
                answer += pq.poll().v;
        }

        System.out.println(answer);

    }

}
