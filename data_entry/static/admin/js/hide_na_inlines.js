jQuery(document).ready(function(){
  jQuery(".grey_out_checkbox").on("click", function(){
      if(this.checked){
	      sibling_div = jQuery(this).siblings(".tabular, .stacked_inline")
		  overlay = jQuery("<div class='overlay'></div>")
		  
	      sibling_div.prepend(overlay)
	      overlay.height(sibling_div.height())
	      overlay.width(sibling_div.width())

	    jQuery(sibling_div).find(':input').each(function() {
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
		    jQuery(this).val('');
		    break;
		case 'checkbox':
		case 'radio':
		    this.checked = false;
		    break;
	    }
	  })
      } else {
       jQuery(this).siblings(".tabular, .stacked_inline").children('.overlay').remove()
      }

    })
});
