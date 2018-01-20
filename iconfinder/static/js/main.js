$(document).ready(function() {
  $("***REMOVED***trigger_addSource").click(function(e) {
    e.preventDefault();
    $("***REMOVED***dialog_addSource").addClass("active");
  });

  $("***REMOVED***dialog_addSource .trigger_addSource_close").click(function(e) {
    e.preventDefault();
    $("***REMOVED***dialog_addSource").removeClass("active");
  });
});
