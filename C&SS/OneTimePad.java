class HelloWorld {
    public static void main(String[] args) {
        String data = format("hello world");
        String key = format("java is cool");
        System.out.println(cipher(data,key,"encrypt"));
        System.out.println(cipher("qeglwoqfzo",key,"decrypt"));
    }
    public static String format(String string) {
        return string.replaceAll("\\s", "").toLowerCase();
    }
    public static String cipher(String data,String key,String mode) {
    String ans = "";
    if (mode.equals("encrypt")) {
        for(int i=0;i<data.length();i++) {
            int temp = (data.charAt(i)-97+key.charAt(i)-97)%26;
            ans += (char) (temp+97);
        }
    }
    if (mode.equals("decrypt")) {
        ans="";
        for(int i=0;i<data.length();i++) {
            int a = data.charAt(i)-97;
            int b = key.charAt(i)-97;
            if ((a-b)<0) {
                ans += (char) (a-b+26+97);
            }
            else {
                ans += (char) (a-b+97);
            }
        }
    }
    return ans;
}
}