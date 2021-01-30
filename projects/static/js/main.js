function getCookie(c_name) {
    if(document.cookie.length > 0) {
        c_start = document.cookie.indexOf(c_name + "=");
        if(c_start != -1) {
            c_start = c_start + c_name.length + 1;
            c_end = document.cookie.indexOf(";", c_start);
            if(c_end == -1) c_end = document.cookie.length;
            return unescape(document.cookie.substring(c_start,c_end));
        }
    }
    return "";
}

function Ajax(url, method, data, callback){
    $.ajax({
        url: url,
        type: method,
        data: data,
        headers: {
            "X-CSRFToken": getCookie("csrftoken")
        },
        cache: false,
        contentType: false,
        processData: false,
        error: function(response){
            callback(response);
        },
        success: function (response) {
            callback(response);
        }
    });
}