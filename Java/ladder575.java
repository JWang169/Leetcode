public class Solution {
    /**
     * @param s: an expression includes numbers, letters and brackets
     * @return: a string
     */
    public String expressionExpand(String s) {
        Stack<Object> stack = new Stack<>();
        int number = 0;
        for (char c: s.toCharArray()){
            if(Character.isDigit(c)){
                number = number * 10 + (c - '0');
            }
            else{
                if(c == '['){
                    stack.push(Integer.valueOf(number));
                    number = 0;
                }
                else{
                    if(c == ']'){
                        String newStr = popStack(stack);
                        //pop all chars until we got a number 
                        Integer count = (Integer)stack.pop();
                        for(int i = 0; i < count; i++){
                            stack.push(newStr);
                        }
                    }    
                    else{
                        // char 
                        stack.push(String.valueOf(c));  //convert char to string so it can be pushed to the stack 
                    }
                }
            }
        }
        return popStack(stack);
    }
    private String popStack(Stack<Object> stack){
        Stack<String> buffer = new Stack<>();
        while(!stack.isEmpty() && (stack.peek() instanceof String)){
            buffer.push((String) stack.pop());
        }
        
        StringBuilder sb = new StringBuilder();  // String is read only, so we use StringBuilder here  
        while (!buffer.isEmpty()){
            sb.append(buffer.pop());
        }
        return sb.toString();
    }
}




