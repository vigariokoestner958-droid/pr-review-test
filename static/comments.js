function renderComments(comments) {
    let html = "";
    comments.forEach(c => {
        // 直接用 innerHTML 插入用户内容
        html += "<div class=\"comment\">" + c.body + "</div>";
    });
    document.getElementById("feed").innerHTML = html;
}
