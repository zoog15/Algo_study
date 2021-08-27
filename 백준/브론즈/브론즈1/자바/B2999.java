package b1;

import java.util.Arrays;
import java.util.Scanner;

/** B2999 비밀 이메일 */
public class B2999 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);
		
		String s = sc.nextLine();
		int l = s.length();
		char[] arr = new char[l];
		
		int gizun = (int) Math.sqrt(l);
		
		
		for(int i = 0; i < l; i++) {
			arr[i] = s.charAt(i);
		}
		
		int x = 1;
		int y = 1;
		for(int i = 0; i <= gizun; i++) {
			for(int j = 0; j <= l; j++) {
				if(i*j == l) {
					x = i;
					y = j;
				}
			}
		}
		char[][] arr2 = new char[x][y];
		int num = 0;
		for(int i = 0; i < y; i++) {
			for(int j = 0; j < x; j++) {
				arr2[j][i] = arr[num++];
			}
		}
		
		for(int i = 0; i < x; i++) {
			for(int j = 0; j < y; j++) {
				System.out.print(arr2[i][j]);
			}
		}
	}
}
