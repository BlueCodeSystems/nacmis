//daca validation acknowledgement
var dacaValidationStatus = document.getElementById('id_dacavalidation_set-0-validation_status');
var hideMe = document.getElementById('id_dacavalidation_set-0-daca_initials');

dacaValidationStatus.onchange = function name(event) {
    var showOptions = ['approved','submitted','needs_review']
    var selectedOption = event.target['value'];

    if (showOptions.indexOf(selectedOption) >= 0){
       // console.log('event object from dacaValidationStatus',event.target['value']);
        hideMe.classList.add("show_acknowledgement");
    } else {
        hideMe.classList.remove("show_acknowledgement");
    }

    
}
