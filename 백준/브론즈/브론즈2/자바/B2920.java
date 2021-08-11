package b2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

/** 2920번 : 음계 */
public class B2920 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		StringTokenizer st = new StringTokenizer(br.readLine(), " ");
		int[] arr = new int[8];
		int flag = 0;
		
		for(int i = 0; i<arr.length; i++) {
			arr[i] = Integer.parseInt(st.nextToken());
		}
		
		for(int i = 0; i<arr.length-1; i++) {
			if(arr[0] == 1 && (arr[i]+1 == arr[i+1]))
				flag += 1;
			else if(arr[0] == 8 && (arr[i]-1 == arr[i+1]))
				flag += 2;
			else
				flag = 0;
		}
		
		if(flag == 7)
			System.out.println("ascending");
		else if(flag == 14)
			System.out.println("descending");
		else
			System.out.println("mixed");
	}
}
