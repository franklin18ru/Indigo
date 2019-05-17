$(document).ready(function() {
    $("body").on("click",".add-more",function(){ 
        var html = $(".after-add-more").first().clone();
      
        //  $(html).find(".change").prepend("<label for=''>&nbsp;</label><br/><a class='btn btn-danger remove'>- Remove</a>");
      
          $(html).find(".change").html("<label for=''>&nbsp;</label><br/><a class='btn btn-danger remove'>- Fjarlægja mynd</a>");
      
      
        $(".after-add-more").last().after(html);
      
     
       
    });

    $("body").on("click",".remove",function(){ 
        $(this).parents(".after-add-more").remove();
    });
});

form_count = Number($("[name=extra_field_count]").val());
// get extra form count so we know what index to use for the next item.

$("#add-another").click(function() {
    form_count ++;

    element = $('<input type="text"/>');
    element.attr('name', 'extra_field_' + form_count);
    $("#forms").append(element);
    // build element and append it to our forms container

    $("[name=extra_field_count]").val(form_count);
    // increment form count so our view knows to populate
    // that many fields for validation
});
