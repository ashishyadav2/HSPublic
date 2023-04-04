var num1 = 37;
var num2 = 49;
if(num1<num2) {
	let temp = num1;
	num1 = num2;
	num2 = temp;
}
var matrixAi = [[1,0,num1]];
var matrixBi = [[0,1,num2]];
var matrixTi = [[]];
var qi = [];
var i = 0;
var temp = [];
var ans = 0;
while(matrixBi[i][2]!=0) {
    qi[i] = Math.trunc(matrixAi[i][2]/matrixBi[i][2]);
    matrixTi[i] = [ matrixAi[i][0] - qi[i]*matrixBi[i][0], 
                    matrixAi[i][1] - qi[i]*matrixBi[i][1], 
                    matrixAi[i][2] - qi[i]*matrixBi[i][2]   ];
    
    matrixAi[i+1] = [   matrixBi[i][0],     
                        matrixBi[i][1], 
                        matrixBi[i][2]  ];
                        
    matrixBi[i+1] = [   matrixTi[i][0], 
                        matrixTi[i][1], 
                        matrixTi[i][2]];
    i++;
}
console.log("_A1, A2, A3   B1, B2, B3  Q  T1, T2, T3");
for(let j=0;j<i;j++) {
    console.log(matrixAi[j],matrixBi[j],qi[j],matrixTi[j]);
}
ans = matrixBi[matrixBi.length-2][1];
if(ans<0) {
    ans += num1;
}
console.log(`${num1}^-1 mod ${num2} = ${ans}`);



