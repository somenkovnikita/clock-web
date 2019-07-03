function displayTime(jsonTime) {
    $("#time").text(jsonTime.data.time)
}

function updateTime() {
    $.ajax({
        url: "/api",
        dataType: "json",
    }).done(displayTime);
}

setInterval(updateTime, 1000);
