package String;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class S_1408 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		
		char[] c = new char[s.length()];
		
		for(int i = 0; i < s.length(); i++) {
			c[i] = s.charAt(i);
		}
		
		for(int i = 0; i < c.length; i++) {
			System.out.print((char)(c[i]+2));
		}
		System.out.println();
		for(int i = 0; i < c.length; i++) {
			System.out.print((char)(c[i]*7%80+48));
		}
	}
}
