function editCus(e, id) {
    e.preventDefault();
    console.log(id)
    editableQuestion = $('[data-id=question-' + id + ']')
    editableAnswer = $('[data-id=answer-' + id + ']') 
    console.log(editableQuestion.text(), editableAnswer.text())
    $.ajax({
        url: "/customer/edit"+id,
        type: "POST",
        dataType: "json",
        data: { "id": id},
        success: function(response) {
            // set updated value as old value 
            alert("Updated successfully")            
        },
        error: function() {
            console.log("errr");
            alert("An error occurred")
        }
    });
    return false;
}
function showAddPopup(triggeringLink, id) {
    
    var name = triggeringLink.id.replace(/^add_/, '');
    href = triggeringLink.href;
    var win = window.open(href, name, 'height=500,width=800,resizable=yes,scrollbars=yes');
    win.focus();
    return false;
}
