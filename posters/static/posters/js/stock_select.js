for(var i=1; i<=99; i++){
    var select = document.getElementById("stock");
    var option = document.createElement("SELECTION");
    select.options.add(option);
    option.text = i;
    option.value = i;
    };

$('#desc_sel').click(function(){ 
    $(this).text(function(i,old){
        return old=='More ...' ?  'Less ...' : 'More ...';
    });
});