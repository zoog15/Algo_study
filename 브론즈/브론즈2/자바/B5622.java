package b2;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;

/** 5622번 다이얼 */
public class B5622 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		String s = br.readLine();
		
		char[][] arr = {{'A','B','C'}, {'D','E','F'},{'G','H','I'},{'J','K','L'},{'M','N','O'},{'P','Q','R','S'},
				{'T','U','V'},{'W','X','Y','Z'}};
		String[] word = s.split(""); // 입력받은 문자열을 문자 하나하나 단위로 쪼개서 넣음
		int ans = 0;
		 
		for(int i = 0; i < word.length; i++) {
			for(int j = 0; j < arr.length; j++) {
				String arr_s = Arrays.toString(arr[j]); // arr의 각 행을 하나의 문자열로 arr_s에 넣기
				if(arr_s.contains(word[i])) {		    // arr_s안에 word[i]가 있으면 그때의 arr의 행 index
					ans += j+2;
					break;
				}
			}
		}
		
		System.out.println(ans+word.length);
	}
}
