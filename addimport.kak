define-command addimport -docstring "add given import to current file" -params 1..2 %sh{
  echo execute-keys -draft "\% | addimport <space> --lang <space> %opt{filetype} <space> - <space> %arg{1} <space> %arg{2} <space> <ret>"
  echo execute-keys "g."
}
