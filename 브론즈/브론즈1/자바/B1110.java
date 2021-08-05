package b1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 1110번 더하기 사이클 */
public class B1110 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(br.readLine());
		int first = n;
		int cnt = 0;
		
		while(true) {
			int a = n/10;
			int b = n%10;
			int s = a+b;
			
			if(s>=10) s -= 10;
			
			n = (b*10) + s;
			cnt += 1;
			if(n == first) break;
		}
		
		System.out.println(cnt);
	}
}
