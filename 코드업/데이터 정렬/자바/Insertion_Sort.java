package sort;

import java.util.Scanner;

public class Insertion_Sort {
	static int i, j;

	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		int n = sc.nextInt();
		int[] arr = new int[n];

		for(int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}

		for(int i = 1; i < n; i++) {
			// 타겟 넘버
			int target = arr[i];

			int j = i - 1;

			// 타겟이 이전 원소보다 크기 전 까지 반복
			while(j >= 0 && target < arr[j]) {
				arr[j + 1] = arr[j];	// 이전 원소를 한 칸씩 뒤로 미룬다.
				j--;
			}

			/*
			 * 위 반복문에서 탈출 하는 경우 앞의 원소가 타겟보다 작다는 의미이므로
			 * 타겟 원소는 j번째 원소 뒤에 와야한다.
			 * 그러므로 타겟은 j + 1 에 위치하게 된다.
			 */
			arr[j + 1] = target;
		}

		for(int i = 0; i < n; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}
