function isSubsequence(s: string, t: string): boolean {
    var j: number = 0;
    for (var i = 0; i < t.length; i++) {
        if (s[j] == t[i]) { j++; }
    }
    return j == s.length;
};