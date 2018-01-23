$(document).ready(function() {
  $("#trigger_addSource").click(function(e) {
    e.preventDefault();
    $("#dialog_addSource").addClass("active");
  });
  $("#dialog_addSource .trigger_addSource_close").click(function(e) {
    e.preventDefault();
    $("#dialog_addSource").removeClass("active");
  });

  $(".trigger_addCategory").click(function(e) {
    e.preventDefault();
    $("#dialog_addCategory").addClass("active");
  });
  $("#dialog_addCategory .trigger_addCategory_close").click(function(e) {
    e.preventDefault();
    $("#dialog_addCategory").removeClass("active");
  });

  $(".trigger_uploadFiles").click(function(e) {
    e.preventDefault();
    $("#dialog_uploadFiles").addClass("active");
  });
  $("#dialog_uploadFiles .trigger_uploadFiles_close").click(function(e) {
    e.preventDefault();
    $("#dialog_uploadFiles").removeClass("active");
  });

  $(".icon-category_header.toggle_controls").hover(
    function () {
      $(this).children(".btn").removeClass("hide");
    },
    function () {
      $(this).children(".btn").addClass("hide");
    }
  );

  $(".icon-card-link").on("click", function(e) {
    e.preventDefault();
    var icon_id = $(this).attr("data-icon-id");
    $("#icon-sidebar").load('/icon/' + icon_id);
    $(".icon-grid .card").removeClass("active");
    $(this).children(".card").addClass("active");
  });

  $(".dropzone").on("dragover dragenter", function() {
    $(this).addClass("dragover");
  });
  $(".dropzone").on("dragleave dragend drop", function() {
    $(this).removeClass("dragover");
  });
});
