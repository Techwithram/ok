const display = document.getElementById("display");
function appendToDisplay(input) {
  display.value += input;
}
function clearDisplay() {
  display.value = "";
}
function calculate() {
  try {
    if (display.value.slice(0, 3) === "cos") {
      display.value = Math.cos(Number(display.value.slice(3)));
    } else if (display.value.slice(0, 3) === "bin") {
      display.value = (Number(display.value.slice(3)) >>> 0).toString(2);
    } else if (display.value.slice(0, 3) === "sin") {
      display.value = Math.sin(Number(display.value.slice(3)));
    } else if (display.value.slice(0, 4) === "hexa") {
      display.value = Number(display.value.slice(4)).toString(36);
    } else if (display.value.slice(0, 3) === "tan") {
      display.value = Math.tan(Number(display.value.slice(3)));
    } else if (display.value.slice(0, 3) === "dec") {
      display.value = parseInt(display.value.slice(3), 2);
    } else if (display.value.slice(0, 4) === "sqrt") {
      display.value = Math.sqrt(Number(display.value.slice(4)));
    } else if (display.value.slice(0, 3) === "sin") {
      display.value = Math.sin(Number(display.value.slice(3)));
    } else if (display.value.slice(0, 3) === "log") {
      display.value = Math.log10(Number(display.value.slice(3)));
    } else if (display.value.slice(0, 3) === "exp") {
      display.value = Math.exp(Number(display.value.slice(3)));
    } else if (display.value.slice(0, 5) === "round") {
      display.value = Math.round(Number(display.value.slice(5)));
    } else {
      display.value = eval(display.value);
    }
  } catch (error) {
    display.value = "ERROR";
  }
}
function removeLast() {
  display.value = display.value.toString().slice(0, -1);
}
var icon = document.getElementById("Theme");
function changeTheme() {
  document.body.classList.toggle("dark-theme");
}
