package b1;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
//import java.util.Arrays;
import java.util.StringTokenizer;

/** 1546번 평균 */
public class B1546 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader in = new BufferedReader(new InputStreamReader(System.in));
		
		int n = Integer.parseInt(in.readLine()); // 몇개 받을지
		double sum = 0;
		double max = 0;
		double[] arr = new double[n];
		
		StringTokenizer st = new StringTokenizer(in.readLine()," ");
		for(int i = 0; i<n; i++) { // arr 배열에 입력받은 숫자 3개 저장
			arr[i] = Double.parseDouble(st.nextToken());
			if(arr[i]>max) max = arr[i];
		}
		
//		System.out.println(max);
//		System.out.println(Arrays.toString(arr));
		
		for(int i = 0; i<n; i++) {
			if(arr[i] < max) 
				arr[i] = arr[i]/max * 100;
			else if(arr[i] == max)
				arr[i] = 100;
			sum += arr[i];
		}
		
		System.out.println(sum/n);
	}
}
