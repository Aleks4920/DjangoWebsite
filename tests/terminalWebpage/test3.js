{
  // Instantiate the Shell object and invoke its execute method.
  var oShell = new ActiveXObject("Shell.Application");

  var commandtoRun = "";
  if (inputparms != "") {
    var commandParms = document.Form1.filename.value;
  }

  // Invoke the execute method.
  oShell.ShellExecute(commandtoRun, commandParms, "", "open", "1");

}
