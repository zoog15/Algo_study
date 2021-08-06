package b2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** B2675 문자열 반복 */
public class B2675 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int tc = Integer.parseInt(br.readLine());

		for (int i = 0; i < tc; i++) {
			StringBuilder sb = new StringBuilder();
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			int n = Integer.parseInt(st.nextToken());
			String s = st.nextToken();
			
			for(int j = 0; j<s.length();j++) {
				for(int k = 0; k< n; k++) {
					sb.append(s.charAt(j));
				}
			}
			System.out.println(sb);
		}
	}
}
