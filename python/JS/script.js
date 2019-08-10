/*document.write("这个一个JS文件");
document.getElementById("p1").style.color='blue';

var myage = 18;
if(myage>=18)
{document.write("你是成年人")}
else
{document.write("你是未成年人")}

document.write(myage)
*/
function rec() {

    var score;
    score = prompt("请输入分数：");
    if (score >= 90) {
        document.write("你真棒！！");
    }
    else if (score >= 75) {
        document.write("加油！！");
    }
    else if (score >= 60) {
        document.write("再接再厉！！");
    }
    else {
        document.write("努力！！");
    }
}

function info() {
    confirm("请输入要提交的内容！！");
}

function message() {
    confirm("你真的要离开吗？");
}