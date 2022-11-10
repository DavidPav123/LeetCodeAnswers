function defangIPaddr(address: string): string {
    for (var i: number = 0; i < address.length; i++) {
        console.log(i);
        if (address[i] == '.') {
            address = address.slice(0, i) + "[.]" + address.slice(i + 1);
            i += 2;
        }
        console.log(address.length);
    }
    return address;
};