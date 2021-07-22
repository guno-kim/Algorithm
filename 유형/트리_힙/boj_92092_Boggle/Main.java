package 유형.트리_힙.boj_92092_Boggle;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.List;

public class Main {
    static int S =1;
    static TrieNode root=new TrieNode();
    static List<TrieNode> endNodes=new ArrayList<>();

    static int[] dx={0,0,1,1,1,-1,-1,-1};
    static int[] dy={1,-1,1,0,-1,1,0,-1};

    static int[] scores={0,0,0,1,1,2,3,5,11};
    static char[][] board;
    static boolean[][] visited;

    static int score;
    static String longest;
    static int cnt;

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuilder sb=new StringBuilder();
        int w=Integer.parseInt(br.readLine());
        while (w-->0){
            insert(br.readLine());
        }
        br.readLine();

        int b=Integer.parseInt(br.readLine());
        while (b-- > 0) {

            score=0;cnt=0;longest="";// 초기화
            for(TrieNode t:endNodes){
                t.isHit=false;
            }

            String s=br.readLine();
            board=new char[4][s.length()];
            visited=new boolean[4][s.length()];
            board[0]=s.toCharArray();
            for (int i = 1; i < 4; i++) {
                board[i]=br.readLine().toCharArray();
            }
            if(b!=0)
                br.readLine();

            for (int i = 0; i < 4; i++) {
                for (int j = 0; j < board[0].length; j++) {
                    dfs(i,j,root,"");
                }
            }
            sb.append(score).append(" ").append(longest).append(" ").append(cnt).append("\n");

        }
        System.out.println(sb);



    }
    static class TrieNode {
        TrieNode[] children=new TrieNode[26];
        boolean isEnd;
        boolean isHit;
    }
    static void insert(String word){
        TrieNode current=root;
        for (int i = 0; i < word.length(); i++) {
            int idx=word.charAt(i)-'A';
            if(current.children[idx]==null){
                current.children[idx]=new TrieNode();
            }
            current=current.children[idx];
        }
        current.isEnd=true;
        endNodes.add(current);
    }

    static void dfs(int x,int y,TrieNode current,String s){
        char c=board[x][y];
        if(current.children[c-'A']==null)
            return;
        current=current.children[c-'A'];
        s+=board[x][y];
        visited[x][y]=true;

        if(current.isEnd&&!current.isHit){
            current.isHit=true;
            int len=s.length();
            cnt++;
            score+=scores[len];
            if(longest.length()==len){
                longest=longest.compareTo(s)<0?longest:s;
            }else if(longest.length()<len){
                longest=s;
            }
        }

        for (int i = 0; i < 8; i++) {
            int nx=x+dx[i],ny=y+dy[i];
            if(0<=nx&&nx<4&&0<=ny&&ny<board[0].length&&!visited[nx][ny]){
                dfs(nx,ny,current,s);
            }
        }
        visited[x][y]=false;

    }


}
