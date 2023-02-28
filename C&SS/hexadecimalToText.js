function hexToText(hex) {
    hex = hex.replace(/\s/g,"");
    let result = "";
    for (let i = 0; i < hex.length; i += 2) {
        let decimalValue = parseInt(hex.substr(i, 2), 16);
        result += String.fromCharCode(decimalValue);
    }
    return result;
}

function textToHex(text) {
  let hex = '';
  for (let i = 0; i < text.length; i++) {
    hex += text.charCodeAt(i).toString(16);
  }
  return hex;
}

const ans = hexToText("");
console.log(ans);