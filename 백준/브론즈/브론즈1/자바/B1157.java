package b1;

import java.util.Scanner;

/** 단어공부 */
public class B1157 {
	public static void main(String[] args) {
		Scanner sc = new Scanner(System.in);

		String s = sc.nextLine().toUpperCase();
		int[] arr = new int[26]; // 영문자 26개 갯수 확인용

		for (int i = 0; i < s.length(); i++) {
			arr[s.charAt(i) - 65]++;
		}

		int max = -1;
		char ch = '?';

		for (int i = 0; i < 26; i++) {
			if (arr[i] > max) {
				max = arr[i];
				ch = (char)(i+65); // 대문자로 바꿔주기
			}
			else if(arr[i] == max) {
				ch = '?';
			}
		}

		System.out.println(ch);
		sc.close();
	}
}
