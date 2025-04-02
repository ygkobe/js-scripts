const CryptoJS = require('crypto-js');

function I() {
    this.update = function (t) {
        // 创建一个 MD5 哈希对象
        const hash = CryptoJS.MD5(t);
        return {
            hex: function () {
                return hash.toString(CryptoJS.enc.Hex);
            }
        };
    };
}

function sign(t) {
    return new I(true).update(t)["hex"]();
};


const format_date = function (e, t) {
    if (!e)
        return "";
    var o = new Date(e);
    /YYYY/.test(t) && (t = t.replace(/YYYY/, o.getFullYear()));
    var l = o.getMonth() + 1;
    if (/MM/.test(t)) {
        var r = l < 10 ? "0" + l : l;
        t = t.replace(/MM/, r)
    } else
        /M/.test(t) && (t = t.replace(/M/, l));
    var n = o.getDate();
    if (/DD/.test(t)) {
        var c = n < 10 ? "0" + n : n;
        t = t.replace(/DD/, c)
    } else
        /D/.test(t) && (t = t.replace(/D/, n));
    var d = o.getHours();
    if (/HH/.test(t)) {
        var f = d < 10 ? "0" + d : d;
        t = t.replace(/HH/, f)
    } else if (/H/.test(t))
        t = t.replace(/H/, d);
    else if (/hh/.test(t)) {
        var h = d > 12 ? d - 12 : d
            , _ = h < 10 ? "0" + h : h;
        t = t.replace(/hh/, _)
    } else if (/h/.test(t)) {
        var m = d > 12 ? d - 12 : d;
        t = t.replace(/h/, m)
    }
    var x = o.getMinutes();
    if (/mm/.test(t)) {
        var w = x < 10 ? "0" + x : x;
        t = t.replace(/mm/, w)
    } else
        /m/.test(t) && (t = t.replace(/m/, x));
    var v = o.getSeconds();
    if (/ss/.test(t)) {
        var k = v < 10 ? "0" + v : v;
        t = t.replace(/ss/, k)
    } else
        /s/.test(t) && (t = t.replace(/s/, v));
    return t
};

const current_time = new Date
const sign_headers = sign("msgDt=".concat(format_date(current_time, "YYYY-MM-DD hh:mm:ss"), "&appSecret=a177d876cc7b42bea696d09e563004ee"))


const msgDate_headers = format_date(current_time, "YYYY-MM-DD hh:mm:ss")


// console.log(sign_headers.toUpperCase(), msgDate_headers)

function headers(){

    return {
        "Content-Type": "application/json",
        "sign": sign_headers.toUpperCase(),
        "msgdate": msgDate_headers,
        "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36"
    }

}

// console.log(headers('12'))