function format(string) {
    return string.replace(/\s/g, "").toLowerCase();
}
let data = format("hello world");
let key = format("java is cool");
console.log(cipher(data,key,"encrypt"));
console.log(cipher("qeglwoqfzo",key,"decrypt"));
function cipher(data,key,mode) {
    let ans = "";
    if (mode==="encrypt") {
        for(let i=0;i<data.length;i++) {
            let temp = (data.charCodeAt(i)-97+key.charCodeAt(i)-97)%26;
            ans += String.fromCharCode(temp+97);
        }
    }
    if (mode==="decrypt") {
        for(let i=0;i<data.length;i++) {
            let a = data.charCodeAt(i)-97;
            let b = key.charCodeAt(i)-97;
            if ((a-b)<0) {
                ans += String.fromCharCode(a-b+26+97);
            }
            else {
                ans += String.fromCharCode(a-b+97);
            }
        }
    }
    return ans;
}