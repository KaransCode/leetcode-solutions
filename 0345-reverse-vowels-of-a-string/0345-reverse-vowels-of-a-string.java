class Solution {
    void reverse(char[] chArr) {
        int n = chArr.length;
        int i = 0, j = n - 1;
        while (i < j) {
            while (i < j && (chArr[i] != 'a' & chArr[i] != 'A'
                    & chArr[i] != 'e' & chArr[i] != 'E'
                    & chArr[i] != 'i' & chArr[i] != 'I'
                    & chArr[i] != 'o' & chArr[i] != 'O'
                    & chArr[i] != 'u' & chArr[i] != 'U'))
                i++;
            while (i < j && (chArr[j] != 'a' & chArr[j] != 'A'
                    & chArr[j] != 'e' & chArr[j] != 'E'
                    & chArr[j] != 'i' & chArr[j] != 'I'
                    & chArr[j] != 'o' & chArr[j] != 'O'
                    & chArr[j] != 'u' & chArr[j] != 'U'))
                j--;
            char temp = chArr[i];
            chArr[i] = chArr[j];
            chArr[j] = temp;
            i++;
            j--;
        }
    }

    public String reverseVowels(String s) {
        char[] res = s.toCharArray();
        reverse(res);
        return new String(res);
    }
}