var resource_number = 1;
$(".resource-number").each(function() {
    if (resource_number < 10) {
        $(this).html("0" + resource_number);
    }
    else {
        $(this).html(resource_number);
    }
    resource_number++;
});
