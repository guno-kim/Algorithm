package 유형.트리.boj_1927_최소힙;

import java.io.BufferedReader;
import java.io.BufferedWriter;
import java.io.InputStreamReader;
import java.io.OutputStreamWriter;
import java.io.IOException;
import java.util.ArrayList;
import java.util.List;
import java.util.StringTokenizer;

public class Main {
    static List<Long> heap=new ArrayList<>();

    public static void main(String[] args) throws IOException{
        BufferedReader br=new BufferedReader(new InputStreamReader(System.in));
        BufferedWriter bw=new BufferedWriter(new OutputStreamWriter(System.out));
        StringBuilder sb=new StringBuilder();
        heap.add(0L);

        int n=Integer.parseInt(br.readLine());
        while(n-->0){
            Long num=Long.parseLong(br.readLine());
            if(num==0){
                sb.append(pop()+"\n");
            }else {
                push(num);
            }
        }
        System.out.println(sb);


    }
    static void swap(int i,int j){
        Long temp=heap.get(i);
        heap.set(i,heap.get(j));
        heap.set(j,temp);
    }
    static Long pop(){
        if(heap.size()==1)
            return 0L;
        if(heap.size()==2)
            return heap.remove(1); 
        long a=heap.get(1);
        heap.set(1,heap.remove(heap.size()-1));
        int i=1;
        while(true){
            int childIdx=getMinChild(i);
            if(childIdx==-1)
                break;
            if(heap.get(i)>heap.get(childIdx))
                swap(i,childIdx);
            i=childIdx;
        }
        return a;
    }

    static int getMinChild(int i){
        int size=heap.size();
        if(size-1<i*2){
            return -1;
        }
        else if(size-1<i*2+1){
            return i*2;
        }
        else {
            return heap.get(i*2)<heap.get(i*2+1)?i*2:i*2+1;
        }
    }

    static void push(Long num){
        heap.add(num);
        int i=heap.size()-1;
        while (i!=1){
            int pi=i/2;
            if(heap.get(pi)>num){
                swap(i,pi);
                i=pi;
            }
            else break;
        }
    }


}
