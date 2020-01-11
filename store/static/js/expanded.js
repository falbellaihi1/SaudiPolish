
/*
$(document).ready(function(){

  //localStorage.clear();   // Uncomment to clear ALL storage.

  // Timer needed because of Bootstrap's animation delay.
  var timer;

  $("ul").on("click",function(e){
    console.log("Click!");
     var id = $(this).attr("id");
     console.log("id is " + id)

    // Clear previous timer if any.
    clearTimeout(timer);
    timer = setTimeout(function(){

      // Get expanded states for each ul.
      var expanded=[];
      $("ul").each(function(){
        var thisExpanded = $(this).attr("aria-expanded");
        console.log(thisExpanded);

        if(typeof(thisExpanded) != "undefined"){
          expanded.push( thisExpanded );
        }else{
          expanded.push("undefined");
        }
      });

      // Show it in console.
      var expandedString = JSON.stringify(expanded);
      console.log( expandedString );

      // Save it in Storage.
      localStorage.setItem("ULexpanded",expandedString);
    },600);


  });

  // On load, set ul to previous state.
  console.log("---- On Load.");
  
  // Parse the string back to an array.
  var previousState = JSON.parse(localStorage.getItem("ULexpanded"));
  console.log(previousState);

  // If there is data in locaStorage.
  if(previousState != null){
    console.log("Setting ul states on...");

    $("ul").each(function(index){
      
      // If the ul was expanded.
      if(previousState[index] == "true"){
        console.log("Index #"+index);
        $(this).addClass("show").attr("aria-expanded", previousState[index]);
      }
    });
  }

});

*/