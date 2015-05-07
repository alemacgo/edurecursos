Handlebars.registerHelper('link', function(number) {
  number = Handlebars.Utils.escapeExpression(number);
  var result = ("0" + number).slice(-2);
  return new Handlebars.SafeString(result);
});

// Compile the Handlebars template
var HRTemplate = Handlebars.compile($('#hr-template').html());

// Load data from the spreadsheet
$('#hr').sheetrock({
  url: spreadsheetUrl,
  query: "select A,B,C",
  rowTemplate: HRTemplate
});

$(document).ready(loadSpreadsheetName);
function loadSpreadsheetName() {
      $.getJSON(spreadsheetUrl, function(data) {
         if (data && data != null && typeof data == "object" && data.contents && data.contents != null && typeof data.contents == "string") {
            if (data.length > 0) {
               if (ContentLocationInDOM && ContentLocationInDOM != null && ContentLocationInDOM != "null") {
                  $("#unit-name").html($("#docs-title-inner", data));
               }
               else {
                  $("#unit-name").html(data);
               }
            }
         }
      });
}
