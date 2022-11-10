function removeDuplicates(s: string): string {
    for (var i: number = 1; i < s.length; i++) {
        if (s[i] == s[i - 1]) {
            s = s.slice(0, i-1) + s.slice(i + 1);
            if (i != 0) {
                i -= 2;
            }
        }
    }
    return s;
};