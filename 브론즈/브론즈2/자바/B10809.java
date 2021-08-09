package b2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 10809번 알파벳 찾기 */
public class B10809 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		StringBuilder sb = new StringBuilder();
		
		int[] word = new int[26];  // 전부 0으로 초기화되어있음
		int[] flag = new int[26];
		
		StringTokenizer st = new StringTokenizer(br.readLine());
		
		String s = st.nextToken();
		char[] c = new char[s.length()];
		
		
		for(int i = 0; i < s.length(); i++) {
			c[i] = s.charAt(i);
		}
		
		for(int i = 0; i < c.length;i++){
			if(flag[c[i]-'a'] == 1)
				continue;
			word[c[i]-'a'] = i;
			flag[c[i]-'a'] = 1;
		}
		
		for(int i = 0; i < flag.length; i++) {
			if(flag[i] == 0)
				word[i] = -1;
		}
		
		for(int i = 0; i < word.length; i++) {
			sb.append(word[i]).append(" ");
		}
		
		
		System.out.println(sb.toString().trim());
	}
}
