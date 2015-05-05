// Compile the Handlebars template for HR leaders.
console.log($('#hr-template').html());
var HRTemplate = Handlebars.compile($('#hr-template').html());

// Load top five HR leaders.
$('#hr').sheetrock({
  url: spreadsheetUrl,
  query: "select A,B,C",
  fetchSize: 5,
  rowTemplate: HRTemplate
});
