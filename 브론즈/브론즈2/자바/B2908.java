package b2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 2908번 상수 */
public class B2908 {
	public static void main(String[] args) throws IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb1 = new StringBuilder();
		StringBuilder sb2 = new StringBuilder();
		StringTokenizer st = new StringTokenizer(br.readLine()," ");
		
		String a = st.nextToken();
		String b = st.nextToken();
		
		sb1.append(a);
		sb2.append(b);
		
		int r_a = Integer.parseInt(sb1.reverse().toString());
		int r_b = Integer.parseInt(sb2.reverse().toString());
		
		if( r_a > r_b)
			System.out.println(r_a);
		else
			System.out.println(r_b);
	}
}
