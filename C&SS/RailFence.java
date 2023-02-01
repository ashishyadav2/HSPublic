import java.util.Scanner;
public class RailFence {
    public static void main(String[] args) {
	Scanner input = new Scanner(System.in);
	System.out.print("Plain Text: ");
	String plainText = input.next();
	System.out.print("\nKey: ");
	int key = input.nextInt();
	String cipherText = encipher(format(plainText),key);
	System.out.println("Cipher Text: "+cipherText);
	String pT = decipher(format(cipherText),key);
	System.out.println("Plain Text: "+ pT);	
    }
    public static String format(String string) { // to remove spaces and make string to uppercase
        return string.replaceAll("\\s","").toUpperCase();
    }
    public static String encipher(String text,int depth) {
        float len = text.length();
        int n = (int) len;
        int c = (int) Math.ceil(len/depth);
        char[][] matrix = new char[depth][c];
        int k=0;
        String ans = "";
        for(int i=0;i<c;i++){
            for(int j=0;j<depth;j++) {
                if(k<n) {
                    matrix[j][i] = text.charAt(k++);
                }
                else {
                    matrix[j][i] = '_';
                }
            }
        }
	//printing the matrix
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
                    matrix[i][j] = '_';
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