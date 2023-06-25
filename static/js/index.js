$(function() {
    const input = $("#input");
    const output = $("#output");
    const sendButton = $("#send-button");
    const z = $("#zundamon")

    input.on("input", function () {
        if (input.val().length === 0) {
            sendButton.addClass("disabled");
        } else {
            sendButton.removeClass("disabled");
        }
    });

    sendButton.on("click", function () {
        let message = input.val();
        // message = message.replaceAll("\n", ",");
        const array = {message: message};

        // console.log(JSON.stringify(array));

        $.ajax({
            url: "/analysis",
            type: "POST",
            dataType: "text",
            data: JSON.stringify(array),
            headers: {
                "Content-Type": "application/json"
            }
        }).done(function(data) {
            const json = JSON.parse(data);
            let representative = "None";

            if (json["representative"] !== undefined)
                representative = json["representative"][0];

            z.attr("src", `img/${representative}.png`);

            output.val(data);
        }).fail(function (a, b, c) {
            output.val(`a: ${a},\nb: ${b},\nc: ${c}`);
            z.attr("src", `img/None.png`);
        });
    });
});