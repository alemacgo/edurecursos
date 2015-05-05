Handlebars.registerHelper('link', function(number) {
  number = Handlebars.Utils.escapeExpression(number);
  var result = ("0" + number).slice(-2);
  return new Handlebars.SafeString(result);
});

// Compile the Handlebars template for HR leaders.
var HRTemplate = Handlebars.compile($('#hr-template').html());

// Load top five HR leaders.
$('#hr').sheetrock({
  url: spreadsheetUrl,
  query: "select A,B,C",
  rowTemplate: HRTemplate
});
