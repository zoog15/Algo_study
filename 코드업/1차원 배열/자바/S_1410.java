package Array1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

/** 1410번 올바른 괄호1(괄호 개수 세기) */
public class S_1410 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack<Character> stack = new Stack<Character>();
		
		String s = br.readLine();
		
		int cnt1 = 0;
		int cnt2 = 0;
		
		for(int i = 0; i < s.length(); i++) {
			stack.push(s.charAt(i));
		}
		
		for(int i = 0; i < s.length(); i++) {
			char c = stack.pop();
			if(c == '(') cnt1++;
			if(c == ')') cnt2++;
		}
		
		System.out.println(cnt1+" "+cnt2);
	}
}
