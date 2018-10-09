$(document).ready(function(){
   $(".grey_out_checkbox").on("click", function(){
      if(this.checked){
	      sibling_div = $(this).siblings(".tabular, .around_stacked")
	      overlay = $("<div class='overlay'></div>")
	      sibling_div.prepend(overlay)
	      overlay.height(sibling_div.height())

	    $(sibling_div).find(':input').each(function() {
	    switch(this.type) {
		case 'password':
		case 'text':
		case 'textarea':
		case 'file':
		case 'select-one':
		case 'select-multiple':
		case 'date':
		case 'number':
		case 'tel':
		case 'email':
		    $(this).val('');
		    break;
		case 'checkbox':
		case 'radio':
		    this.checked = false;
		    break;
	    }
	  })
      } else {
       $(this).siblings(".tabular, .around_stacked").children('.overlay').remove()
      }

    })
});
