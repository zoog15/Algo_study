package 백준;

import java.io.BufferedReader;
import java.io.InputStreamReader;

/** 3040번 백설공주와 일곱 난장이 */
public class B3040 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int[] hat = new int[9]; // 난쟁이 9명의 모자 숫자 넣기
		int sum = 0;
		
		for(int i = 0; i< 9; i++) {
			hat[i] = Integer.parseInt(br.readLine());
			sum += hat[i];
		}
		
//		System.out.println(sum);
		
		int one = 0;
		int two = 0;
		/** 
		 * 1. 전체합 - 빠질 2명의 합 = 100이 되게하는 i,j 2개를 찾아주기
		 * */
		for(int i = 0; i < 8; i++) {
			for(int j = i+1; j < 9; j++) {
				int dif = hat[i] + hat[j];
				if(sum - dif == 100) {
					one = hat[i];
					two = hat[j];
				}		
			}
		}
		
		// 출력할때 위에서 찾은 2개의 숫자는 빼고 출력
		for(int i = 0; i< 9 ; i++) {
			if(hat[i] == one || hat[i] == two)
				continue;
			System.out.println(hat[i]);
		}
	} // end main
} // end class
