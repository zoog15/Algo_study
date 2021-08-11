package b2;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

/** 2562번 최댓값 */
public class B2562 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int max = -1;
		int max_cnt = 1;
		int[] arr = new int[9];
		
		for(int i = 0; i<arr.length; i++) {
			int num = Integer.parseInt(in.readLine());
			if(num > max) {
				max = num;
				max_cnt = i+1;
			}
		}
		
		System.out.println(max);
		System.out.println(max_cnt);
	}
}
