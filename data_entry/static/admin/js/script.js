//daca validation acknowledgement
var dacaValidationInitails = (document.getElementsByClassName('field-daca_initials')[0]);
var   dacaValidationStatus = document.getElementById('id_dacavalidation_set-0-validation_status');
// pitmeo/daca validation acknowledgement
var pitmeoValidationInitails = (document.getElementsByClassName('field-pitmeo_initials')[0]);
var pitmeoValidationStatus = document.getElementById('id_pitmeovalidation_set-0-validation_status'); 

// hides both divs that contain labels
dacaValidationInitails.classList.add('hide_acknowledgement');
pitmeoValidationInitails.classList.add('hide_acknowledgement');

//toggle events here
dacaValidationStatus.onchange = function (event) {
    validationStatusToggle(event, dacaValidationInitails);  
};

pitmeoValidationStatus.onchange = function (event) {
    validationStatusToggle(event, pitmeoValidationInitails);
};

function validationStatusToggle(event, initials){
    var showOptions = ['approved','needs_review'];
    var selectedOption = event.target['value'];

    if (showOptions.indexOf(selectedOption) >= 0){
        //console.log('event object from dacaValidationStatus',event.target['value']);
        initials.classList.remove("hide_acknowledgement");
        initials.classList.add("show_acknowledgement");
    }
    else if(selectedOption === ""){
        initials.classList.remove("show_acknowledgement");
        initials.classList.add("hide_acknowledgement");
    }
}


