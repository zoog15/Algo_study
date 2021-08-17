package Array1;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class S_1407 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		
		for(int i = 0; i < s.length(); i++) {
			if(s.charAt(i) == ' ') continue;
			System.out.print(s.charAt(i));
		}
	}
}
