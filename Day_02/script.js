
function factorial(){
    let num=prompt("enter any number for its factorial: ")
    let output=num
    if(num==0 || num==1){
        return 1
    }
    else{
        for(let i=1;i<num;i++)
        {
            output*=i;
        }
    }
    return output;
}
console.log(factorial());
console.log("siva".concat("raju"))