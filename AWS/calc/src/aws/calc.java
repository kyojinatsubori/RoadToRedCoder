package aws;

import java.util.ArrayDeque;
import java.util.Arrays;
import java.util.Deque;
import java.util.List;

public class calc {

	public calc() {

	}
	public String chkFormula(String formula) {
		String res;
		if (!formula.matches("[0-9+*/()-]*")) {
			res = "ERROR";
		}
		else {
			res =formula;
		}
		return res;
	}

	public String calclation(String formula) {
		String[] stringArray = getRpn(formula).split("");
		Deque<Integer> que = new ArrayDeque<>();
        int a = 0;
        int b = 0;
        for (int i = 0; i < stringArray.length; i++) {
            switch (stringArray[i]) {
            case "+":
                a = que.pollFirst();
                b = que.pollFirst();
                que.addFirst(b + a);
                break;
            case "-":
                a = que.pollFirst();
                b = que.pollFirst();
                que.addFirst(b - a);
                break;
            case "/":
                a = que.pollFirst();
                b = que.pollFirst();
                que.addFirst(b / a);
                break;
            case "*":
                a = que.pollFirst();
                b = que.pollFirst();
                que.addFirst(b * a);
                break;
            default:
            	System.out.println(stringArray);
                que.addFirst(Integer.parseInt(stringArray[i]));
            }

        }
        return que.pop().toString();
	}
	public static String getRpn(String formula) {
        char[] sequenceList  = formula.toCharArray();
        // 戻り値を格納するStringBuilder
        StringBuilder resultBuilder = new StringBuilder(sequenceList.length);
        Deque<Character> stack = new ArrayDeque<Character>();

        // 数式をすべて逆ポーランド記法に変換するまでループを続ける
        for(char token : sequenceList){
            switch (token) {
                case '+':
                case '-':
                    // スタックされた演算子の優先順位より低い場合は、スタックの演算子をバッファへ
                    while (!stack.isEmpty()) {
                        char c = stack.getFirst();
                        if (c == '*' || c == '/') {
                            resultBuilder.append(stack.removeFirst());
                        } else {
                            break;
                        }
                    }
                    stack.addFirst(token);
                    break;
                case '*':
                case '/':
                case '(':
                    stack.addFirst(token);
                    break;
                case ')':
                    // 「(」から「)」までの演算子をバッファへ
                    List<Object> list = Arrays.asList(stack.toArray());
                    int index = list.indexOf('(');

                    Deque<Character> workStack = new ArrayDeque<Character>();
                    for (int i = 0; i <= index; i++) {
                        char c = stack.removeFirst();
                        if (c != '(') {
                            workStack.addFirst(c);
                        }
                    }

                    while (!workStack.isEmpty()) {
                        resultBuilder.append(workStack.removeFirst());
                    }
                    break;
                default:
                    // 数値の場合
                    resultBuilder.append(token);
                    break;
            }
        }

        while (!stack.isEmpty()) {
            resultBuilder.append(stack.removeFirst());
        }
        return resultBuilder.toString();
    }

}
