$(document).ready(function () {
  $("#people-data-table").DataTable({
    paging: false,
    ordering: true,
    info: false,
    searching: false,
    columnDefs: [
        { targets: [0, 4, 5, 6], orderable: true},
        { targets: '_all', orderable: false }
    ]
  });
});
