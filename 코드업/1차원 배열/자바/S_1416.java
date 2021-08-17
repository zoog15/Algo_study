package Array1;

import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Stack;

/** 1416번 2진수 변환 */
public class S_1416 {
	public static void main(String[] args) throws Exception {
		BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
		Stack<Integer> stack = new Stack<Integer>();
		
		int n = Integer.parseInt(br.readLine());
		
		if(n==0) stack.push(0);
		while(n!=0) {
			stack.push(n%2);
			n /= 2;
		}
		
		int l = stack.size();
		for(int i = 0; i < l; i++) {
			System.out.print(stack.pop());
		}
	}
}
