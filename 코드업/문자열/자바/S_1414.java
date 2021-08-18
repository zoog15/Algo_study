package String;

import java.io.BufferedReader;
import java.io.InputStreamReader;

public class S_1414 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		String c = s.toUpperCase();
		
		int cnt1 = 0;
		int cnt2 = 0;
		
		
		
		for(int i = 0; i < c.length(); i++) {
			if(c.charAt(i) == 'C')
				cnt1 += 1;
		}
		
		for(int i = 0; i < c.length()-1; i++) {
			if(c.charAt(i) == 'C' && c.charAt(i+1) == 'C')
				cnt2 += 1;
		}
		
		System.out.println(cnt1);
		System.out.println(cnt2);
	}
}
