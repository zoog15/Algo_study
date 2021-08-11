package b4;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 1330번 두 수 비교하기 */
public class B1330 {
	public static void main(String[] args) throws IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		String[] strs = in.readLine().split(" ");
		int n1 = Integer.parseInt(strs[0]);
		int n2 = Integer.parseInt(strs[1]);
		
		if(n1 > n2)
			System.out.println(">");
		else if(n1 < n2)
			System.out.println("<");
		else
			System.out.println("==");
	}
}
