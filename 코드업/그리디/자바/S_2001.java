package greedy;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/** 그리디 2001번 최소 대금 */
public class S_2001 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int min_p = 2000;
		int min_s = 2000;
		
		for(int i = 0; i < 3; i++) {
			int p = Integer.parseInt(br.readLine());
			if(p<min_p) min_p = p;
		}
		
		for(int i = 0; i < 2; i++) {
			int s = Integer.parseInt(br.readLine());
			if(s<min_s) min_s = s;
		}
		
		System.out.printf("%.1f",(min_p+min_s)*1.1);
	}
}
