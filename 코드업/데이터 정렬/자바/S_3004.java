// 2차배열 정렬 참고용, 문제는 못품
package sort;

import java.util.Arrays;
import java.util.Comparator;
import java.util.Scanner;

public class S_3004 {
	static int i, j;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[][] arr = new int[n][2];

		for (i = 0; i < n; i++) {
			arr[i][0] = sc.nextInt();
			arr[i][1] = i; // 입력받은 순서 0 부터 시작
		}
		
		Arrays.sort(arr, new Comparator<int[]>() {  // 2차원배열의 0열을 기준으로 오름차순
			@Override
				public int compare(int[] o1, int[] o2) {
					return o1[0] - o2[0]; // 내림차순할거면 반대로
			}
		});

		
		for(i = 0; i < n; i++) {
			for(int j = 0; j < 2; j++) {
				System.out.print(arr[i][j]+" ");
			}
			System.out.println();
		}
	}
}

