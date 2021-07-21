package 유형.정렬.boj_1713_후보추천하기;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.List;
import java.util.ArrayList;
import java.util.Collections;
import java.util.Comparator;
import java.util.StringTokenizer;
import java.io.IOException;

public class Main {
    
    public static void main(String[] args) throws IOException{
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int n=Integer.parseInt(br.readLine());
        int k=Integer.parseInt(br.readLine());
        StringTokenizer st=new StringTokenizer(br.readLine());
        StringBuilder sb=new StringBuilder();
        Person[] people=new Person[101];
        List<Person> list=new ArrayList<>();
        for (int i = 0; i < k; i++) {
            int id=Integer.parseInt(st.nextToken());
            if(people[id]==null){
                people[id]=new Person(id,0,0,false);
            }
            
            if(people[id].isIn){
                people[id].cnt++;
            }
            else{
                if(list.size()==n){
                    Collections.sort(list);
                    Person p=list.remove(0);
                    p.isIn=false;
                }
                people[id].isIn=true;
                people[id].cnt=1;
                people[id].timeStamp=i;
                list.add(people[id]);
            }
        }
        Collections.sort(list,new Comparator<Person>(){
            public int compare(Person p1,Person p2){
                return Integer.compare(p1.id, p2.id);
            }
        });

        for(Person p:list){
            sb.append(p.id+" ");
        }
        System.out.println(sb);
    }
}


class Person implements Comparable<Person>{
    int id;
    int cnt;
    int timeStamp;
    boolean isIn;
   Person(int id,int cnt,int timeStamp,boolean isIn){
       this.id=id;
       this.cnt=cnt;
       this.timeStamp=timeStamp;
       this.isIn=isIn;
   }
   public int compareTo(Person person){
       int result=cnt-person.cnt;
       if(result==0){
           return timeStamp-person.timeStamp;
       }
       else return result;
   }
}