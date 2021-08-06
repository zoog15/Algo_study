package b1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

/** 4344번 : 평균은 넘겠지 */
public class B4344 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int tc = Integer.parseInt(br.readLine());
		
		for(int testCase = 0; testCase < tc; testCase++) {
			int sum = 0;
			int cnt = 0;
			
			StringTokenizer str = new StringTokenizer(br.readLine()," ");
			int st = Integer.parseInt(str.nextToken());
			int[] score = new int[st];
			
			for(int i = 0;i<score.length;i++) {
				score[i] = Integer.parseInt(str.nextToken());
				sum += score[i];
			}
			
			double avg = (double)sum/st;
			
			for(int i = 0; i<score.length;i++) {
				if(score[i] > avg) cnt++;
			}
			
			double answer = (double)cnt/st;
			String ans = String.format("%.3f",(answer*100));
			System.out.println(ans+"%");
		}
	}
}
