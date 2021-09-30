package b3;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.StringTokenizer;

public class B10250 {
	public static void main(String[] args) throws NumberFormatException, IOException {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		
		int testCase = Integer.parseInt(br.readLine());
		
		for (int tc = 0; tc < testCase; tc++) {
			StringTokenizer st = new StringTokenizer(br.readLine()," ");
			int h = Integer.parseInt(st.nextToken()); // 호텔 높이
			int w = Integer.parseInt(st.nextToken()); // 호텔 너비
			int n = Integer.parseInt(st.nextToken()); // 몇번째 손님?
			int count = 0; // 현재가 몇번째방인지 카운팅
			String answer = ""; // 정답을 저장할 문자열
			
			for (int i = 1; i <= w; i++) {
				for (int j = 1; j<= h; j++) {
					count++;
					if (count == n) {
						if (i < 10) {
							answer += j + "0" + i;
						}
						else {
							answer += ""+ j + i;
						}
					}
				}
			}
			System.out.println(answer);
		} // end for tc
	} //end main
} // end class
