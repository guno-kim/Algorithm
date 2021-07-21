package 유형.BFS.boj_3055_탈출;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.LinkedList;
import java.util.Queue;
import java.io.IOException;
import java.util.StringTokenizer;

public class Main {
    public static class Point{
        public int x;
        public int y;
        public char c;
        public int cnt=0;
        Point(int x,int y,char c,int cnt){
            this.x=x;
            this.y=y;
            this.c=c;
            this.cnt=cnt;
        }
    };
    
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringTokenizer st=new StringTokenizer(br.readLine());
        int R=Integer.parseInt(st.nextToken()),C=Integer.parseInt(st.nextToken());
        char[][] map=new char[R][C];

        Queue<Point> q=new LinkedList<Point>();
        for (int i = 0; i < R; i++) {
            String s=br.readLine();
            for (int j = 0; j < C; j++) {
                char c=s.charAt(j);
                if(c=='*')
                    q.add(new Point(i,j,'*',0));
                map[i][j]=c;
            }
        }
        for (int i = 0; i < R; i++) {
            for (int j = 0; j < C; j++) {
                char c=map[i][j];
                if(c=='S'){
                    q.add(new Point(i,j,'S',0));
                }
            }
        }
        int[] dx=new int[]{0,0,1,-1};
        int[] dy=new int[]{1,-1,0,0};
        int answer=0;

        while(!q.isEmpty()){
            Point p=q.poll();
            int x=p.x,y=p.y,cnt=p.cnt;
            char c=p.c;
            Boolean finished=false;
            for (int i = 0; i < 4; i++) {
                int nx=x+dx[i],ny=y+dy[i];
                if(0<=nx && nx<R && 0<=ny && ny<C){
                    if(map[nx][ny]=='D'){
                        if(c=='S'){
                            finished=true;
                            answer=cnt+1;
                            break;
                        }
                        else continue;
                    }
                    else if(map[nx][ny]=='.'){
                        map[nx][ny]=c;
                        q.add(new Point(nx, ny, c,cnt+1));
                    }
                }
            }
            if(finished)
                break;
        }
        if(answer>0)
            System.out.println(answer);
        else
            System.out.println("KAKTUS");

    }
}
