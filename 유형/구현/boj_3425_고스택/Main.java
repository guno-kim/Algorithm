package 유형.구현.boj_3425_고스택;
import java.io.*;
import java.util.*;

public class Main {
	public static	Stack<Long> st;
    public static Long MAX=1000000000L;
        
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		BufferedWriter bw = new BufferedWriter(new OutputStreamWriter(System.out));
		List<String> list = new ArrayList<>();
		int N;
		boolean order = true, isSuccess;
		String oder;
		while (order) {
			oder = br.readLine();
			if (oder.equals("END")) {
				N = Integer.parseInt(br.readLine());
				while (N-- > 0) {
					isSuccess = true;
					st = new Stack<>();
					st.push(Long.parseLong(br.readLine()));
					for (int i = 0; i < list.size() && isSuccess; i++) {
						try {
							switch (list.get(i).split(" ")[0]) {
                                case "NUM":isSuccess=num(Long.parseLong(list.get(i).split(" ")[1]));break;
                                case "POP":isSuccess=pop();break;
                                case "INV":isSuccess=inv();break;
                                case "DUP":isSuccess=dup();break;
                                case "SWP":isSuccess=swp();break;
                                case "ADD":isSuccess=add();break;
                                case "SUB":isSuccess=sub();break;
                                case "MUL":isSuccess=mul();break;
                                case "DIV":isSuccess=div();break;
                                case "MOD":isSuccess=mod();break;
							}
							if (st.size() != 0) {
								if (Math.abs(st.peek()) > 1000000000) {
									isSuccess = false;
								}
							}
						} catch (Exception e) {
							isSuccess = false;
						}
					}
					bw.write(!isSuccess || st.size() != 1 ? "ERROR\n" : st.pop() + "\n");
				}
				bw.write("\n");
				list.removeAll(list);
			} else if (oder.equals("QUIT")) {
				break;
			} else {
				list.add(oder);
			}
		}
		bw.flush();
		bw.close();
		br.close();
	}
    public static boolean num(Long l){
        st.add(l);
        return true;
    }
    public static boolean pop(){
        st.pop();
        return true;
    }

    public static boolean inv(){
        st.add(-st.pop());
        return true;
    }

    public static boolean dup(){
        st.add(st.peek());
        return true;
    }

    public static boolean swp(){
        Long a=st.pop();
        Long b=st.pop();
        st.add(a);
        st.add(b);
        return true;
    }
    public static boolean add(){
        Long a=st.pop();
        Long b=st.pop();
        st.add(a+b);
        return true;
    }
    public static boolean sub(){
        Long a=st.pop();
        Long b=st.pop();
        Long result=b-a;
        if(Math.abs(result)>MAX)
            return false;
        else
            st.add(result);
        return true;
    }
    public static boolean mul(){
        Long a=st.pop();
        Long b=st.pop();
        
        Long result=a*b;
        if(Math.abs(result)>MAX)
            return false;
        st.add(result);
        return true;
    }
    public static boolean div(){
        Long a=st.pop();
        Long b=st.pop();
        if(a==0)
            return false;
        
        Long result=Math.abs(b)/Math.abs(a);
        if((a<0&&b>=0)||(a>=0&&b<0))
            st.add(-result);
        else
            st.add(result);
        return true;
    }
    public static boolean mod(){
        Long a=st.pop();
        Long b=st.pop();
        if(a==0)
            return false;
        
        Long result=Math.abs(b)%Math.abs(a);
        if(b<0)
            st.add(-result);
        else
            st.add(result);
        return true;
    }

}