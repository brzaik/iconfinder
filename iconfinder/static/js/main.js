$(document).ready(function() {
  $("***REMOVED***trigger_addSource").click(function(e) {
    e.preventDefault();
    $("***REMOVED***dialog_addSource").addClass("active");
  });

  $("***REMOVED***dialog_addSource .trigger_addSource_close").click(function(e) {
    e.preventDefault();
    $("***REMOVED***dialog_addSource").removeClass("active");
  });

  $(".icon-card-link").on("click", function(e) {
    e.preventDefault();
    var icon_id = $(this).attr("data-icon-id");
    $("***REMOVED***icon-sidebar").load('/icon/' + icon_id);
    $(".icon-grid .card").removeClass("active");
    $(this).children(".card").addClass("active");
  });
});
