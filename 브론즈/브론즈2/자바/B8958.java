package b2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 8958번 : OX퀴즈 */
public class B8958 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int tc = Integer.parseInt(br.readLine());
		int[] answer = new int[tc];
		
		for(int i = 0 ; i < tc; i++) {
			String str = br.readLine();
			int cnt = 0;
			int sum = 0;
			char[] c = new char[str.length()];
			
			for(int j = 0 ; j < str.length(); j++) { // 문자열을 문자배열에 나눠서 넣어주기
				c[j] = str.charAt(j);
			}
			
			for(int j=0; j< c.length;j++) { // ox 확인
				if(c[j] == 'X') {
					cnt = 0;
					continue;
				}
				cnt += 1;
				sum += cnt;
			}
			answer[i] = sum;
		}
		
		for(int i = 0; i<answer.length; i++) {
			System.out.println(answer[i]);
		}
	} // end of main
} // end of class
