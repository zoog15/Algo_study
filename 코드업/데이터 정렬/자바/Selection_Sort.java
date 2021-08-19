package sort;

import java.util.Scanner;

public class Selection_Sort {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		int n = sc.nextInt();
		int[] arr = new int[n];
		int temp = 0;
		
		for(int i = 0; i < n; i++) {
			arr[i] = sc.nextInt();
		}
		
		for(int i =0; i < n; i++) {
			int min = i;
			for(int j = i+1;  j < n; j++) {
				if(arr[j] < arr[min]) min = j;
			}			
			temp = arr[i];
			arr[i] = arr[min];
			arr[min] = temp;
		}
		
		for(int i = 0; i < n; i++) {
			System.out.print(arr[i] + " ");
		}
	}
}
