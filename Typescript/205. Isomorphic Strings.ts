function isIsomorphic(s: string, t: string): boolean {
    var keys: string[] = [];
    var vals: string[] = [];
    var values = new Set();

    for (var i = 0; i < s.length; i++) {
        var a = s[i];
        var b = t[i];

        if (keys.includes(a)) {
            if (vals[keys.indexOf(a)] != b) {
                return false;
            }
        }
        else {
            if (values.has(b)) {
                return false;
            }
            keys.push(a);
            vals[keys.indexOf(a)] = b
            values.add(b);
        }
    }
    return true;
};