public class RailFence {
    public static void main(String[] args) {
        System.out.println(encipher(format("Discover interesting projects and people to populate your personal news feed"),4));
        System.out.println(decipher(format("DOIRIRCNOTPTURAWEIVNENOTDPOUERSLSDSETSGJSPLPLYPONF-CRETPEAEEOAOENEE-"),4));
    }
    public static String format(String string) {
        return string.replaceAll("\\s","").toUpperCase();
    }
    public static String encipher(String text,int depth) {
        float len = text.length();
        int n = (int) len;
        int c = Math.round(len/depth);
        char[][] matrix = new char[depth][c];
        int k=0;
        String ans = "";
        for(int i=0;i<c;i++){
            for(int j=0;j<depth;j++) {
                if(k<n) {
                    matrix[j][i] = text.charAt(k++);
                }
                else {
                    matrix[j][i] = '-';
                }
            }
        }
        for (char[] ch: matrix) {
            System.out.print("[");
            for(char chr: ch) {
                System.out.print(" "+chr+" ");
                ans += chr;
            }
            System.out.println("]\n");
        }
        return ans;
    }
    public static String decipher(String cipherText,int depth) {
        float len = cipherText.length();
        int n = (int) len;
        int c = Math.round(len/depth);
        char[][] matrix = new char[depth][c];
        int k=0;
        String ans = "";
        for(int i=0;i<depth;i++){
            for(int j=0;j<c;j++) {
                if(k<n) {
                    matrix[i][j] = cipherText.charAt(k++);
                }
                else {
                    matrix[i][j] = '-';
                }
            }
        }
        for(int i=0;i<c;i++){
            for(int j=0;j<depth;j++) {
                System.out.print(matrix[j][i]);
            }
        }
        return ans;
    }
}