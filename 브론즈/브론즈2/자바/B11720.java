package b2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 11720번 숫자의 합 */
public class B11720 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

		int n = Integer.parseInt(br.readLine());
		char[] arr = new char[n];
		int sum = 0;

		StringTokenizer st = new StringTokenizer(br.readLine());
		String s = st.nextToken();

		for (int i = 0; i < arr.length; i++) {
			arr[i] = s.charAt(i);
			sum += arr[i]-'0';
		}
		
		System.out.println(sum);
	}
}
