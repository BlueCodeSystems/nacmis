//daca validation acknowledgement
var dacaValidationStatus = document.getElementById('id_dacavalidation_set-0-validation_status');
var hideMePlease = document.getElementById('id_dacavalidation_set-0-daca_initials');

// pitmeo/daca validation acknowledgement
var pitmeoValidationStatus = document.getElementById('id_pitmeovalidation_set-0-validation_status');
var hideMePlease2 = document.getElementById('id_pitmeovalidation_set-0-pitmeo_initials');

dacaValidationStatus.onchange = function name(event) {
    var showOptions = ['approved','submitted','needs_review']
    var selectedOption = event.target['value'];

    if (showOptions.indexOf(selectedOption) >= 0){
       // console.log('event object from dacaValidationStatus',event.target['value']);
       hideMePlease.classList.add("show_acknowledgement");
    } else {
        hideMePlease.classList.remove("show_acknowledgement");
    }
}

pitmeoValidationStatus.onchange = function name(event) {
    var showOptions = ['approved','submitted','needs_review']
    var selectedOption = event.target['value'];

    if (showOptions.indexOf(selectedOption) >= 0){
        // console.log('event object from dacaValidationStatus',event.target['value']);
        hideMePlease2.classList.add("show_acknowledgement");
    } else {
        hideMePlease2.classList.remove("show_acknowledgement");
    }
}


