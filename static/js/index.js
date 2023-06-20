$(function() {
    const input = $("#input");
    const output = $("#output");
    const sendButton = $("#send-button");

    input.on("input", function () {
        if (input.val().length === 0) {
            sendButton.addClass("disabled");
        } else {
            sendButton.removeClass("disabled");
        }
    });

    sendButton.on("click", function () {
        const message = input.val();
        const array = {message: message};

        console.log(JSON.stringify(array));

        $.ajax({
            url: "/analysis",
            type: "POST",
            dataType: "text",
            data: JSON.stringify(array),
            headers: {
                "Content-Type": "application/json"
            }
        }).done(function(data) {
            output.val(data);
        }).fail(function (a, b, c) {
            output.val(`a: ${a},\nb: ${b},\nc: ${c}`);
        });
    });
});