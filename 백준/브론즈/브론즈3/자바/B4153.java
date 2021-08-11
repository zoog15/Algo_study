package b3;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 4153번 직각삼각형 */
public class B4153 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		int[] arr = new int[3];
		
		while(true) {
			int max = 0;
			int sum = 0;
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			for(int i = 0; i < 3; i++) {
				arr[i] = Integer.parseInt(st.nextToken());
				if(arr[i] > max) {
					max = arr[i]; // 그때그때 최댓값 갱신
				}
			}
			
			for(int i = 0; i < 3; i++) {
				if(arr[i] == max) continue;
				sum += Math.pow(arr[i], 2);
			}
			
			if(sum == 0) break;
			
			if(sum == Math.pow(max, 2)) System.out.println("right");
			else System.out.println("wrong");
		}

	}
}
